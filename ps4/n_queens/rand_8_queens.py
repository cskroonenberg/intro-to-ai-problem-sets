# Author: Caden Kroonenberg
# Date: 2-15-22

import numpy as np
import random

# Return the number of queens conflicting in grid.
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

N = 8       # Grid size, number of queens
i = 0       # Epoch count

for x in range(1):
    count = 0
    success = False # Conflict exists
    while not success:
        queens = [] # list of queen x-coordinates; queen[y] = x
        count +=1
        i+=1
        # Random start state for queen n
        queens = []
        for n in range(N):
            queens.append(random.randint(0,N-1))
        # If a solution is found, break loop
        # print(fitness(queens, N))
        if fitness(queens, N) == N*(N-1)/2:
            print(queens)
            success = True
    print('{}): {}'.format(x,count))
print('Average: {}'.format(i/100))
print('SUCCESS in {} iterations'.format(i))