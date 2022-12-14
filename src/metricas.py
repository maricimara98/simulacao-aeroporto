#!/usr/bin/python
# -*- coding: utf-8-sig -*-

from src.globals import *


def separate_usage_by_id(data, field, qtd):
    response = [0] * qtd
    for d in data:
        if d[field] is not None:
            response[d[field]] += 1

    return response


def time_dif(data):
    return data[1] - data[0]


def tempo_solo(data, arriving_time, fueling_time):
    s = 0
    for d in data:
        s += time_dif(d['fila de desembarque']) + \
            arriving_time + time_dif(d['fila de decolagem'])
        if d['fila de abastecimento']:
            s += time_dif(d['fila de abastecimento']) + fueling_time
    avg = s / len(data)
    print('Tempo médio em solo: %.2f min' % avg)


def utilizacao_pistas(data, sim_time, landing_time, takeoff_time, n_airstrips):
    r_pouso = separate_usage_by_id(data, 'pista de pouso', n_airstrips)
    r_decolagem = separate_usage_by_id(data, 'pista de decolagem', n_airstrips)

    for i in range(n_airstrips):
        U1 = (r_pouso[i] * landing_time) / sim_time  # utilização para pouso
        U2 = (r_decolagem[i] * takeoff_time) / \
            sim_time  # utilização para decolagem
        print('Utilização da pista %d: %.2f' % (i, U1+U2))


def utilizacao_fingers(data, sim_time, arriving_time, n_fingers):
    r = separate_usage_by_id(data, 'finger', n_fingers)
    for i in range(n_fingers):
        U = (r[i] * arriving_time) / sim_time
        print('Utilização do finger %d: %.2f' % (i, U))


def utilizacao_bomba(data, sim_time, fueling_time, n_gas_pumps):
    r = separate_usage_by_id(data, 'bomba de combustivel', n_gas_pumps)
    for i in range(n_gas_pumps):
        U = (r[i] * fueling_time) / sim_time
        print('Utilização da bomba de combustivel: %.2f' % (U))


def tempo_medio_fila_pistas(data, qtd_avioes):
    s = 0
    for d in data:
        s += time_dif(d['fila de pouso'])
    avg_p = s / qtd_avioes
    print('Tempo médio de espera na fila de pouso: %.2f min' % avg_p)

    s = 0
    for d in data:
        s += time_dif(d['fila de decolagem'])
    avg_d = s / qtd_avioes
    print('Tempo médio de espera na fila de decolagem: %.2f min' % avg_d)

    avg = (avg_p + avg_d) / 2
    print('Tempo médio de espera na fila para acesso a pista: %.2f min' % avg)


def tempo_medio_fila_finges(data, qtd_avioes):
    s = 0
    for d in data:
        s += time_dif(d['fila de desembarque'])
    avg = s / qtd_avioes
    print('Tempo médio de espera na fila de desembarque: %.2f min' % avg)


def tempo_medio_fila_bomba(data):
    s = 0
    c = 0
    for d in data:
        if d['fila de abastecimento']:
            s += time_dif(d['fila de abastecimento'])
            c += 1

    avg = s / c
    print('Tempo médio de espera na fila de abastecimento: %.2f min' % avg)


def log_simulacao(data):
    global TEMPO_SIMULACAO
    global TEMPO_POUSO
    global TEMPO_ABASTECIMENTO
    global TEMPO_EMBARQUE_DESEMBARQUE
    global TEMPO_DECOLAGEM
    global QTD_PISTAS
    global QTD_FINGERS
    global QTD_BOMBAS

    qtd_avioes = len(data)
    throughput = qtd_avioes / (TEMPO_SIMULACAO/60)

    print('Aviões atendidos pelo sistema: %d' % qtd_avioes)
    print('Throughput do sistema: %.2f aviões/h' % throughput)

    tempo_solo(data, TEMPO_EMBARQUE_DESEMBARQUE, TEMPO_ABASTECIMENTO)

    utilizacao_pistas(data, TEMPO_SIMULACAO, TEMPO_POUSO,
                      TEMPO_DECOLAGEM, QTD_PISTAS)
    utilizacao_fingers(data, TEMPO_SIMULACAO, TEMPO_EMBARQUE_DESEMBARQUE, QTD_FINGERS)
    utilizacao_bomba(data, TEMPO_SIMULACAO, TEMPO_ABASTECIMENTO, QTD_BOMBAS)

    print('')
    tempo_medio_fila_pistas(data, qtd_avioes)
    tempo_medio_fila_finges(data, qtd_avioes)
    tempo_medio_fila_bomba(data)

    pass
