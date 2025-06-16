import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.metricas import time_dif, separate_usage_by_id


def test_time_dif_simple():
    assert time_dif([2, 5]) == 3


def test_separate_usage_by_id_counts_correctly():
    data = [
        {"pista de pouso": 0},
        {"pista de pouso": 1},
        {"pista de pouso": None},
        {"pista de pouso": 0},
    ]
    # qtd includes ids 0,1,2
    result = separate_usage_by_id(data, "pista de pouso", 3)
    assert result == [2, 1, 0]

