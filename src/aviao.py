#!/usr/bin/python
# -*- coding: utf-8-sig -*-

import random
import math
from os import urandom

from src.globals import *


def getSeed(num):
    if (type(num) != type(int)):
        num = int(num)
    random.seed(urandom(num))

    return random.randint(0, 13)*math.pow(num, 3)


def aviaoProc(env, nome, aeroporto):

    log_simulacao = {
        'fila de pouso': [],
        'fila de desembarque': [],
        'fila de abastecimento': [],
        'fila de decolagem': [],
        'pista de pouso': None,
        'pista de decolagem': None,
        'finger': None,
        'bomba de combustivel': None,
    }

    global LOG_VERBOSE

# ---------------- Pouso ----------------
    # FILA
    if LOG_VERBOSE:
        print('%s em primeiro contato com o aeroporto às %.2f. Aguardando autorização de pouso.' % (
            nome, env.now))
    log_simulacao['fila de pouso'].append(env.now)  # fila de pouso
    pista = yield aeroporto.pista.get()  # pista livre
    log_simulacao['fila de pouso'].append(env.now)  # fila de pouso

    # SERVIÇO
    if LOG_VERBOSE:
        print('%s chegou à pista de pouso. Pouso às %.2f.' % (nome, env.now))
    yield env.process(aeroporto.procedimento(nome, 'pousar'))
    if LOG_VERBOSE:
        print('%s saiu da pista de pouso às %.2f.' % (nome, env.now))

    # LOG
    log_simulacao['pista de pouso'] = pista['id']
    yield aeroporto.pista.put(pista)  # libera a pista

# ---------------- Abastecimento ----------------

    combustivel = random.randint(0, 100)
    if combustivel <= 65:
        # FILA
        if LOG_VERBOSE:
            print('%s requisitou reabastecimento às %.2f. Nível do combustível: %i/100.' %
                  (nome, env.now, combustivel))
        log_simulacao['fila de abastecimento'].append(env.now)
        bomba = yield aeroporto.bomba.get()  # bomba livre
        log_simulacao['fila de abastecimento'].append(env.now)

        # SERVIÇO
        if LOG_VERBOSE:
            print('%s chegou ao posto de abastecimento às %.2f. Abastecendo o tanque.' % (
                nome, env.now))
        yield env.process(aeroporto.procedimento(nome, 'abastecer'))
        if LOG_VERBOSE:
            print('%s está de tanque cheio. Saiu do posto de abastecimento às %.2f.' % (
                nome, env.now))

        # LOG
        log_simulacao['bomba de combustivel'] = bomba['id']
        yield aeroporto.bomba.put(bomba)  # libera a bomba

# ---------------- Desembarque/Embarque	----------------

    # FILA
    if LOG_VERBOSE:
        print('%s dirigindo-se à área de desembarque às %.2f.' % (nome, env.now))
    log_simulacao['fila de desembarque'].append(env.now)
    finger = yield aeroporto.finger.get()  # finger livre
    log_simulacao['fila de desembarque'].append(env.now)

    # SERVIÇO
    if LOG_VERBOSE:
        print('%s iniciou o embarque às %.2f.' % (nome, env.now))
    yield env.process(aeroporto.procedimento(nome, 'embarcar'))
    if LOG_VERBOSE:
        print('%s encerrou o embarque às %.2f.' % (nome, env.now))

    # LOG
    log_simulacao['finger'] = finger['id']
    yield aeroporto.finger.put(finger)  # libera o finger

# ---------------- Decolagem ----------------

    # FILA
    if LOG_VERBOSE:
        print('%s dirigindo-se à pista de decolagem às %.2f.' % (nome, env.now))
    log_simulacao['fila de decolagem'].append(env.now)
    pista = yield aeroporto.pista.get()  # pista livre
    log_simulacao['fila de decolagem'].append(env.now)

    # SERVIÇO
    if LOG_VERBOSE:
        print('%s chegou à pista de decolagem. Início da decolagem às %.2f.' %
              (nome, env.now))
    yield env.process(aeroporto.procedimento(nome, 'decolar'))
    if LOG_VERBOSE:
        print('%s saiu da pista de pouso. Último contato feito às %.2f.' %
              (nome, env.now))

    # LOG
    log_simulacao['pista'] = pista['id']
    yield aeroporto.pista.put(pista)  # libera a pista

    # Registrar métricas
    aeroporto.registrar_metrica(log_simulacao)
    pass


def configura_aeroporto(env, aeroporto, tempo_spawn, qtd_avioes, qtd_pistas, qtd_fingers, qtd_bombas):

    global TEMPO_POUSO
    global TEMPO_EMBARQUE_DESEMBARQUE
    global TEMPO_ABASTECIMENTO
    global TEMPO_DECOLAGEM

    # cria os aviões iniciais
    for i in range(qtd_avioes):
        env.process(aviaoProc(env, 'Avião %d' % i, aeroporto))

    # Cria os aviões durante a execução
    while True:
        yield env.timeout(random.randint(tempo_spawn-2, tempo_spawn+2))
        i += 1
        env.process(aviaoProc(env, 'Avião %d' % i, aeroporto))

    pass
