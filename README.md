# Simulação: Aeroporto

## Objetivo

Avaliar o comportamento de um aeroporto em que aviões pousam, decolam e são abastecidos.

## Visão Geral

Considere um aeroporto onde os aviões, ao chegarem no horizonte, são escalonados para pouso, sendo designados para uma pista (queue_1), em seguida são direcionados para uma ponte de desembarque/finger (queue_2), podendo passar por uma fase de abastecimento de combustível opcional (queue_3) e, finalmente, têm sua decolagem programada através de uma das pistas disponíveis, conforme figura abaixo:

Simule a atividade do aeroporto, inicialmente, com uma pista e duas pontes de desembarque, considerando uma carga baixa (poucos aviões chegando, intervalo entre aviões longo, procedimentos de desembarque e abastecimento ágeis). A etapa de
abastecimento, caso aconteça, introduzirá um tempo adicional na permanência do avião em solo. Numa segunda fase, aumente a carga de trabalho (maior número de aviões, intervalo menor entre chegadas, desembarque e abastecimento demorados) e  verifique os resultados. 

Atenção: não varie todos os parâmetros simultaneamente!

Você deverá utilizar simulação a fim de planejar uma reforma no aeroporto, visando melhorar o baixo desempenho observado quando este opera com uma alta demanda de voos. Considere aumentar o número de pontes de desembarque e/ou de pistas de pouso.

Calcule as métricas de desempenho cabíveis: número de aviões atendidos/hora, tempo médio por avião no solo, utilização dos fingers e das pistas, dentre outras. Varie os parâmetros do sistema e da carga de trabalho e mostre os resultados também
graficamente.

## Requisitos

O cenário descrito deve ser simulado utilizando-se o SimPy.
Para exemplos e tutoriais sobre o simulador SimPy, acesse:
http://www.deinf.ufma.br/~mario/grad/avaldes/avaldes.html.# simulacao-aeroporto
