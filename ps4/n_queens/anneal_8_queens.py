# Author: Caden Kroonenberg
# Date: 2-15-22

from math import exp, inf
import numpy as np
import random

f = 0 # number of evaluations

# Return the number of queens conflicting in grid.
def fitness(queens, N):
    global f
    f += 1
    c = 0
    for q in range(len(queens)):
        for q_y in range(len(queens)):
            q_x = queens[q_y]
            if q_y != q:
                if q_x == queens[q]:
                    c += 1
                if abs(q - q_y) == abs(queens[q] - q_x):
                    c += 1
    return (N*(N-1))/2 - c

def print_grid(queens, N):
    grid = np.full(shape=(N, N), fill_value='-')
    q_x = 0
    for q_y in queens:
        grid[q_x][q_y] = '*'
        q_x += 1
    for row in np.flip(grid, 0):
        for cell in row:
            print(cell, end=' ')
        print()

def schedule(T):
    a = 0.998 # hyperparameter a
    # calculate temperature for current epoch
    # return 0.75*(pow(T,-0.5)-0.025)
    return a*T

def rand_successor(queens, N):
    q_copy = queens.copy()      # copy of queen positions
    q = random.randint(0,N-1)   # random queen, q
    q_y = q_copy[q]             # q position
    while q_y == q_copy[q]:     # choose new position for q
        q_y = random.randint(0,N-1)
    q_copy[q] = q_y
    return q_copy

reset = False
count = 0
for i in range(100):
    if reset == True:
        i-=1
        reset = False

    N = 8       # Grid size, number of queens
    queens = [] # list of queen x-coordinates; queen[y] = x

    # Random start state for queen n
    for n in range(N):
        queens.append(random.randint(0,N-1))

    T = 30 # Temperature
    t = 1  # Epoch
    while True:
        T = schedule(T)
        if T <= 0:
            reset = True
            print('T == 0. No more annealing to be done')
            print('There are {} conflicts.'.format((N*(N-1)/2) - fitness(queens,N)))
            print_grid(queens, N)
            break
        next = rand_successor(queens, N)
        delta = fitness(next,N) - fitness(queens,N)
        # print('{} - {}) C(q) = {}, C(n) = {}'.format(t,T,fitness(queens,N),fitness(next,N)))

        r = random.random()
        try:
            p = exp(delta/T)
        except OverflowError:
            p = 0

        if delta > 0:   # if next has higher fitness than current
            # print('\tdelta < 0; queens = next')
            queens = next.copy()
        elif r <= p:   # if next doesn't have higher fitness, set next to queens w/ probability e^(delta/T)
            # print('\tdelta < 0; probability {} <= {}'.format(r, p))
            queens = next.copy()

        # Break loop if solution has been found
        if fitness(queens,N) == N*(N-1)/2:
            print('SUCCESS in {} iterations.'.format(t))
            print(queens)
            break

        t += 1 # Iterate epoch
    count += t
    print(count)
print('final epoch: {}/100 = {}'.format(count, count/100))
print('final evals: {}/100 = {}'.format(f, f/100))