#!/usr/bin/python
# -*- coding: utf-8-sig -*-

import simpy
from src.globals import *


class Aeroporto:

    def __init__(self, env,
                 qtd_pistas, qtd_fingers, qtd_bombas,
                 tempo_pouso, tempo_embarque, tempo_abastecimento, tempo_decolagem):

        self.env = env  # Ambiente de simulação

        # Recursos
        # Pistas de pouso/decolagem
        self.pista = simpy.Store(env, capacity=qtd_pistas)
        # Pontes de desembarque
        self.finger = simpy.Store(env, capacity=qtd_fingers)
        # Bomba de abastecimento
        self.bomba = simpy.Store(env, capacity=qtd_bombas)

        # Tempo estipulado para cada procedimento
        self.tempo_pouso = tempo_pouso
        self.tempo_embarque = tempo_embarque
        self.tempo_abastecimento = tempo_abastecimento
        self.tempo_decolagem = tempo_decolagem

        self.log_metricas = []  # Registro de métricas

        # setup para iniciar filas
        self.init_queue(qtd_pistas, qtd_fingers, qtd_bombas)
        pass

    def init_queue(self, qtd_pistas, qtd_fingers, qtd_bombas):
        for i in range(qtd_pistas):
            self.pista.put({'id': i})

        for i in range(qtd_fingers):
            self.finger.put({'id': i})

        for i in range(qtd_bombas):
            self.bomba.put({'id': i})

        pass

    def registrar_metrica(self, entry):
        self.log_metricas.append(entry)
        pass

    def procedimento(self, aviao, proc):
        tempo = 0
        if proc == 'pousar':
            tempo = self.tempo_pouso

        elif proc == 'abastecer':
            tempo = self.tempo_abastecimento

        elif proc == 'embarcar':
            tempo = self.tempo_embarque

        elif proc == 'decolar':
            tempo = self.tempo_decolagem

        yield self.env.timeout(tempo)
        if VERBOSE_SERV:
            print('Avião %s em procedimento de %s.' % (aviao, proc))
        pass

    pass
