# Author: Caden Kroonenberg
# Date: 2-12-22

from math import sin, pow
from random import random

def F(x):
    return 4 + 2*x + 2*sin(20*x) - 4*pow(x,2)

individuals = [i*0.01 for i in range(1,100)] # Initial population

N = 10
best = 0 # X with best fitness
for i in range(50): # For 50 generations
    # Roulette Selection
    all_fitness = sum([F(x) for x in individuals])
    population = []
    prev = 0
    while len(population) < N:  # Ensure at least n individuals in population
        for x in individuals:
            r = random()
            if r <= F(x)/all_fitness and not x in population:
                population.append(x)

    # Crossover
    cross = []
    combo = []
    for x in population:
        for y in population:
            combo.append((x,y))
    for (x,y) in combo:
        a = random()
        cross.append(a*x+(1-a)*y)

    population+=cross

    # Mutation
    mut = []
    epsilon = 0.01

    for x in population:
        if random() <= 0.3:         # x-epsilon w/ probability 0.3
            if x-epsilon >= 0: mut.append(x-epsilon)
            else: mut.append(0)     # Clip to remain in [0,1]
        if random() <= 0.4:
            mut.append(x)           # copy w/ probability 0.4
        if random() <= 0.3:         # x+epsilon w/ probability 0.3
            if x+epsilon <= 1: mut.append(x+epsilon)
            else: mut.append(1)     # Clip to remain in [0,1]

    population+=mut

    individuals = population.copy()

    for x in individuals:
        if F(x) > F(best):
            best = x
print('Best x = {}; F({}) = {}'.format(best,best,F(best)))