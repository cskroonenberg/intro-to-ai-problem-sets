# Author: Caden Kroonenberg
# Date: 2-12-22

from math import sin, pow
import random

def F(x):
    return 4 + 2*x + 2*sin(20*x) - 4*pow(x,2)

def roulette_selection(population):
    while True: # continue until return
        max     = sum([F(x) for x in population])
        pick    = random.uniform(0, max)
        current = 0
        for x in population:
            current += F(x)
            if current > pick:
                return x

population = [i*0.01 for i in range(1,100)] # Initial population
N = 10
best = 0

for i in range(50): # For 50 generations
    # Roulette Selection
    select = []
    while len(select) < N:  # Ensure at least n individuals in population
        select.append(roulette_selection(population))
    population = select.copy()

    # Mutation
    mut = []
    epsilon = 0.01
    for x in population:
        r = random.random()
        if r <= 0.3:            # x-epsilon w/ probability 0.3
            if x-epsilon >= 0: mut.append(x-epsilon)
            else: mut.append(0) # Clip to remain in [0,1]
        elif 0.3 < r <= 0.7:    # x w/ probability 0.4
            mut.append(x)       # copy w/ probability 0.4
        else:                   # x+epsilon w/ probability 0.3
            if x+epsilon <= 1: mut.append(x+epsilon)
            else: mut.append(1) # Clip to remain in [0,1]
    population = mut.copy()

    for x in population:
        if F(x) > F(best):
            best = x
print('Best x = {}; F({}) = {}'.format(best,best,F(best)))