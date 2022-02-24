# Author: Caden Kroonenberg
# Date: 2-18-22

import numpy as np
import random

def fitness(queens, N):
    global total_f
    global f
    f += 1
    total_f += 1
    c = 0 # Number of conflicts
    # For each queen
    for q in range(len(queens)):
        for q_y in range(len(queens)):
            q_x = queens[q_y]
            if q_y != q: # Check all other queens
                if q_x == queens[q]: # If queens are in same column
                    c += 1
                if abs(q - q_y) == abs(queens[q] - q_x): # If queens share a diagonal
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

# choose successor based on min-conflict method
def successor(queens, N):
    global rand_choice
    global last_q
    if rand_choice:     # Random choice queen
        q = random.choice(queens)
    else:               # Cyclic choice queen
        last_q = (last_q + 1) % N
        q = last_q

    successors = []     # Successor states for queen q
    for i in range(N):  # Each possible positon for q
        qc = queens.copy()
        qc[q] = i
        successors.append(qc)
    best_f = -1         # Fitness of best successor
    for s in successors:
        f = fitness(s,N)
        if f > best_f:
            best_s = s  # Update best successor
            best_f = f  # Update best fitness
    return best_s

success = False
x = 0   # Iteration of function evaluation
total_f = 0 # Total number of evaluations
f = 0   # Number of evaluations per attempt
s_total_f = 0   # Successful number of evaluations
total_i = 0     # Total number of epochs
s_total_i = 0   # Successful number of epochs
while x < 1:
    rand_choice = False # Choose random queen to minimize conflict; cyclic if False
    last_q = -1 # Last evaluated queen (for cyclic queen selection)
    N = 8       # Grid size, number of queens
    i = 0       # Epoch count
    f = 0       # Evaluation count
    # Random initial state
    queens = []
    for n in range(N):
        queens.append(random.randint(0,N-1))

    for i in range(25): # Cutoff after 25 epochs
        total_i += 1
        queens = successor(queens,N) # Update queen positions
        # print('{}) F(q) = {}\t{}'.format(i,fitness(queens,N),queens))
        if fitness(queens,N) == (N*(N-1))/2: # Test for success
            print('{}) {} epochs'.format(x, i))
            print('\t{}'.format(queens))
            success = True
            s_total_i += i
            s_total_f += f
            break

    if success == True:
        success = False
        x+=1
print('average epochs: {}'.format(total_i/100))
print('average evaluations: {}'.format(total_f/100))
print('average successful epochs: {}'.format(s_total_i/100))
print('average successful evaluations: {}'.format(s_total_f/100))