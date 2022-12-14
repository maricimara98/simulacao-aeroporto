#!/usr/bin/python
# -*- coding: utf-8-sig -*-

import simpy  # biblioteca de simulação
from src.globals import *
from src.aeroporto import Aeroporto
from src.aviao import *
import src.metricas as metricas

"""
Simulação Aeroporto

Covers:

- Resources: Resource
- Condition events
- Shared events

Scenario:
	Considere um aeroporto onde os aviões, ao chegarem no horizonte, são escalonados para
	pouso, sendo designados para uma pista (queue_1), em seguida são direcionados para
	uma ponte de desembarque/finger (queue_2), podendo passar por uma fase de
	abastecimento de combustível opcional (queue_3) e, finalmente, têm sua decolagem
	programada através de uma das pistas disponíveis.

"""

if __name__ == '__main__':

    # Configurar e iniciar a simulação
    print('Simulador Aeroporto')
    random.seed(getSeed(RANDOM_SEED))   # semente do gerador de números aleatórios
    env = simpy.Environment()			# cria o environment do modelo
    
    aeroporto = Aeroporto(env, QTD_PISTAS, QTD_FINGERS, QTD_BOMBAS,
                          TEMPO_POUSO, TEMPO_EMBARQUE_DESEMBARQUE, TEMPO_ABASTECIMENTO, TEMPO_DECOLAGEM)
    env.process(configura_aeroporto(env, aeroporto, TEMPO_SPAWN,
                QTD_AVIOES, QTD_PISTAS, QTD_FINGERS, QTD_BOMBAS))

    # EXECUTAR ambiente
    env.run(until=TEMPO_SIMULACAO)

    # Log com as métricas da simulação
    metricas.log_simulacao(aeroporto.log_metricas)
