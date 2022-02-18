# Author: Caden Kroonenberg
# Date: 2-15-22

import numpy as np
import random

def fitness(queens, N):
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

def best_successor(queens, N):
    successors = []
    for i in range(N): # For each queen
        for j in range(N):
            qc = queens.copy()
            if qc[i] != j:
                qc[i] = j
                successors.append(qc)
    best_f = -1
    for s in successors:
        f = fitness(s,N)
        if f > best_f:
            best_s = s
            best_f = f
    if best_f == -1:
        return queens
    return best_s
    
N = 8       # Grid size, number of queens
i = 0       # Epoch count
total_i = 0 # Total epochs
success = False

while success == False:
    # Random initial state
    queens = []
    for n in range(N):
        queens.append(random.randint(0,N-1))
    i = 0
    while True and i < 50:
        i+=1
        total_i+=1
        next = best_successor(queens,N)
        # Plateau / no improvement
        if fitness(next,N) <= fitness(queens,N):
            break
        queens = next.copy()
        if fitness(queens,N) == (N*(N-1))/2:
            print(queens)
            print('{} epochs'.format(i))
            success = True
            break

print('average epochs: {}'.format(total_i))