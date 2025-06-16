import os
import sys
import random
import simpy
from statistics import mean

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.aeroporto import Aeroporto
from src.aviao import configura_aeroporto
from src import globals as g


def run_short_simulation():
    params = {
        'TEMPO_SIMULACAO': 200,
        'QTD_AVIOES': 1,
        'TEMPO_SPAWN': 5,
        'QTD_PISTAS': 1,
        'QTD_FINGERS': 1,
        'QTD_BOMBAS': 1,
        'TEMPO_POUSO': 1,
        'TEMPO_EMBARQUE_DESEMBARQUE': 1,
        'TEMPO_ABASTECIMENTO': 1,
        'TEMPO_DECOLAGEM': 1,
    }
    for k, v in params.items():
        setattr(g, k, v)
    random.seed(0)

    env = simpy.Environment()
    aeroporto = Aeroporto(
        env,
        g.QTD_PISTAS,
        g.QTD_FINGERS,
        g.QTD_BOMBAS,
        g.TEMPO_POUSO,
        g.TEMPO_EMBARQUE_DESEMBARQUE,
        g.TEMPO_ABASTECIMENTO,
        g.TEMPO_DECOLAGEM,
    )
    env.process(
        configura_aeroporto(
            env,
            aeroporto,
            g.TEMPO_SPAWN,
            g.QTD_AVIOES,
            g.QTD_PISTAS,
            g.QTD_FINGERS,
            g.QTD_BOMBAS,
        )
    )
    env.run(until=g.TEMPO_SIMULACAO)
    return aeroporto.log_metricas, params


def test_short_run_metrics():
    logs, params = run_short_simulation()

    assert len(logs) == 4

    throughput = len(logs) / (params['TEMPO_SIMULACAO'] / 60)
    assert abs(throughput - 1.2) < 0.01

    avg_decolagem = mean(
        entry['fila de decolagem'][1] - entry['fila de decolagem'][0]
        for entry in logs
    )
    assert abs(avg_decolagem - 32.75) < 0.01
