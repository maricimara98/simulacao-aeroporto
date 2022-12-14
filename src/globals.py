#!/usr/bin/python
# -*- coding: utf-8-sig -*-

RANDOM_SEED = 42

# Exibir na tela

LOG_VERBOSE = False     # Log do aeroporto de cada avião
VERBOSE_SERV = False    # Log do aeroporto de cada recurso utilizado

# ------------- Aeroporto -------------

# Ambiente/Geral

TEMPO_SIMULACAO = 60 * 24   # Intervalo de tempo decorrido durante a simulação (min, múltiplos de 60)
QTD_AVIOES = 6              # Quantidade de aviões inicial (no instante 0)
TEMPO_SPAWN = 20            # Intervalo para avistar novos aviões no horizonte (min)

# Pista(s)
QTD_PISTAS = 1 
TEMPO_POUSO = 7
TEMPO_DECOLAGEM = 8

# Ponte(s) de Embarque/Desembarque
QTD_FINGERS = 2
TEMPO_EMBARQUE_DESEMBARQUE = 20

# Bomba(s) de combustível
QTD_BOMBAS = 1
TEMPO_ABASTECIMENTO = 15


""" 
RANDOM_SEED = 42  # 10 15 5 2

LOG_VERBOSE = False
VERBOSE_SERV = True

TEMPO_SIMULACAO = 60
QTD_AVIOES = 3
TEMPO_SPAWN = 3 

QTD_PISTAS = 1  
TEMPO_POUSO = 5
TEMPO_DECOLAGEM = 4

QTD_FINGERS = 2
TEMPO_EMBARQUE = 3

QTD_BOMBAS = 1
TEMPO_ABASTECIMENTO = 3

"""
