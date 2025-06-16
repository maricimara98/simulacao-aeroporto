import random
import math
from os import urandom


def getSeed(num: int) -> int:
    """Generate a pseudo-random seed based on the given number."""
    if type(num) != int:
        num = int(num)
    random.seed(urandom(num))
    return random.randint(0, 13) * math.pow(num, 3)
