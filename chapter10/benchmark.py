import random

from chapter10.timer import Timer

with Timer(verbose=True) as t:
    data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for c in range(10000):
        hoge = random.choice(data)

with Timer() as u:
    for d in range(10000):
        fuga = random.randint(1, 10)

pass