# -*- coding: utf-8 -*-

import random as random

n = int(10e5)
ref = [1, 2, 3]
first_c_wins , second_c_wins = 0 , 0

for i in range(n):
    win_index = int(random.random() * 3 + 1)
    first_choice = int(random.random() * 3 + 1)
    c = list(set(ref)-set([win_index,first_choice]))
    monty_choice = c[int(random.random() * len(c))]
    sec_choice = 6 - (monty_choice + first_choice)
    
    if win_index == first_choice:
        first_c_wins += 1
    elif win_index == sec_choice:
        second_c_wins += 1
        
print(f"Chance for winning without changing: {first_c_wins*100 / n}%")
print(f"Chance for winning with change: {second_c_wins*100 / n}%")
