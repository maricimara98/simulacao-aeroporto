import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.metricas import time_dif


def test_time_dif_simple():
    assert time_dif([1, 4]) == 3
