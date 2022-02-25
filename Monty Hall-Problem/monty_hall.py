# -*- coding: utf-8 -*-

import random as random
import numpy as np

n = int(10e6)
monty = []
win_index = [random.randint(1, 3) for x in range(0, n)]
first_choice = [random.randint(1, 3) for y in range(0, n)]

# Monty's choices
for k in zip(win_index, first_choice):
    ref = [1, 2, 3]
    c = list(set(ref) - set(k))
    monty.append(c[random.randint(0, len(c) - 1)])

# Second choice 
sec_choice = []
for x, y in zip(first_choice, monty):
    sec_choice.append(6 - (x + y))

# Wins 
first_c_wins = [1 if x == 0 else 0 for x in
                list(np.array(win_index) - np.array(first_choice))]
second_c_wins = [1 if x == 0 else 0 for x in
                 list(np.array(win_index) - np.array(sec_choice))]

print(f"Chance for winning without changing: {sum(first_c_wins)*100 / n}%")
print(f"Chance for winning with change: {sum(second_c_wins)*100 / n}%")
