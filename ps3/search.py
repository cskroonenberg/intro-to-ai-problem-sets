# Author: Caden Kroonenberg
# Date: 2-4-22
from queue import Queue
import numpy as np
import heapq

# Backtrack from child to parent to determine optimal path
def path(closed, x_i):
    # Start at X_g
    i = len(closed) - 1
    current = closed[i]
    parent = closed[i][1]
    path = []
    while parent != x_i: # While parent isn't x_i
        path.append(current[0])
        parent = current[1]
        for pair in closed:
            if pair[0] == parent:
                current = pair
                break
    path.append(current[0]) # Include x_i in optimal path
    return path
    
# Manhattan distance heuristic function
def h(x, X_g):
    return abs(x[0] - X_g[0]) + abs(x[1]-X_g[1])

# Add tuples (a, b) + (x, y) = (a + x, b + y)
def add_tuple(a,b):
    return tuple(map(lambda i, j: i + j, a, b))

# Return all possible moves from a given position on the grid
# Check for out-of-bounds & obstacles
def U(x, n, m, obs):
    moves = []
    # Right
    if (not (add_tuple(x, (1,0)))[0] >= n) and (not (add_tuple(x, (1,0))) in obs):
        moves.append((1,0))
    # Up
    if (not (add_tuple(x, (0, 1)))[1] >= m) and (not (add_tuple(x, (0, 1))) in obs):
        moves.append((0,1))
    # Left
    if (not (add_tuple(x, (-1,0)))[0] < 0) and (not (add_tuple(x, (-1,0))) in obs):
        moves.append((-1,0))
    # Down
    if (not (add_tuple(x, (0,-1)))[1] < 0) and (not (add_tuple(x, (0,-1))) in obs):
        moves.append((0,-1)) 
    return moves

def print_grid(x_i, X_g, n,m,obs,closed,fringe):
    for i in reversed(range(m)):
        for j in range(n):
            if (j,i) == x_i:
                print('S', end='')
            elif (j,i) == X_g:
                print('G', end='')
            elif (j,i) in obs:
                print('X', end='')
            elif (j,i) in ([c[0] for c in closed]):
                print('*', end='')
            elif (j,i) in fringe:
                print('F', end='')
            else:
                print('.',end='')
        print()
    print()

# 3.6a) Search routines

def Breadth_First(x_i, X_g, n, m, obs):
    print('Breadth-First Search')
    success = False
    closed = []
    fringe = []
    Q = Queue()
    fringe.append(x_i)
    Q.put(item=[x_i])
    visited = np.zeros(shape=(n,m))
    visited[x_i] = 1
    while not Q.empty():
        x = Q.get()
        # Include x in closed (expanded) states
        closed.append(x)
        # Remove x from fringe
        fringe.remove(x[0])
        x = x[0]
        # Check goal test
        if x == X_g:
            success = True
            break
        for u in U(x, n, m, obs):  # For each possible action
            _x = add_tuple(x,u)
            if not visited[_x]:  # Add child to Q if not yet visited
                visited[_x] = 1
                Q.put(item=[_x, x])
                fringe.append(_x)
            else: # Resolve duplicate 
                continue
    print('{} Closed Cells'.format(len(closed)))
    print('Closed Cells: {}'.format([c[0] for c in closed]))
    print('{} Fringe Cells'.format(len(fringe)))
    print('Path Length: {}'.format(len(path(closed, x_i))))
    print_grid(x_i, X_g, n, m, obs, closed, fringe)
    print()
    return success

def Greedy_Best_First(x_i, X_g, n, m, obs):
    print('Greedy Best-First Search')
    success = False
    closed = []
    fringe = []
    # Init Q, track parent
    Q = [[h(x_i, X_g), x_i, x_i]]
    fringe.append(x_i)
    heapq.heapify(Q)
    visited = np.zeros(shape=(n,m))
    visited[x_i] = 1
    while not len(Q) == 0:
        x = heapq.heappop(Q)
        # Inlcude x in closed (expanded states)
        closed.append([x[1], x[2]])
        # Remove x from fringe
        fringe.remove(x[1])
        x = x[1]
        # Check Goal Test
        if x == X_g:
            success = True
            break
        for u in U(x, n, m, obs):  # For each possible action
            _x = add_tuple(x,u)
            if not visited[_x]:   # Add child to Q if not yet visited
                visited[_x] = 1
                heapq.heappush(Q, [h(_x, X_g), _x, x])
                fringe.append(_x)
            else: # Resolve duplicate 
                continue
    print('{} Closed Cells'.format(len(closed)))
    print('Closed Cells: {}'.format([c[0] for c in closed]))
    print('{} Fringe Cells'.format(len(fringe)))
    print('Path Length: {}'.format(len(path(closed, x_i))))
    print_grid(x_i, X_g, n, m, obs, closed, fringe)
    print()
    return success

def A_star(x_i, X_g, n, m, obs):
    print('A*')
    success = False
    closed = []
    fringe = []
    # Init Q, track parent
    Q = [[h(x_i, X_g), x_i, x_i]]
    fringe.append(x_i)
    heapq.heapify(Q)
    visited = np.zeros(shape=(n,m))
    cost = np.full(shape=(n,m), fill_value=np.Infinity)
    visited[x_i] = 1
    cost[x_i] = 0
    while not len(Q) == 0:
        x = heapq.heappop(Q)
        # Include x in closed (expanded) states
        closed.append([x[1],x[2]])
        # Remove x from fringe
        fringe.remove(x[1])
        x=x[1]
        # Check goal test
        if x == X_g:
            success = True
            break
        for u in U(x, n, m, obs):  # For each possible action
            _x = add_tuple(x,u)
            if cost[x] + 1 < cost[_x]:  # Update cost if necessary
                cost[_x] = cost[x] + 1
            if not visited[_x]:  # Add child to Q if not yet visited
                visited[_x] = 1
                heapq.heappush(Q, [cost[_x] + h(_x, X_g), _x, x])
                fringe.append(_x)
            else: # Resolve duplicate 
                continue
    print('{} Closed Cells'.format(len(closed)))
    print('Closed Cells: {}'.format([c[0] for c in closed]))
    print('{} Fringe Cells'.format(len(fringe)))
    print('Path Length: {}'.format(len(path(closed, x_i))))
    print_grid(x_i, X_g, n, m, obs, closed, fringe)
    print()
    return success

# 3.6b) Example Grid
n = 8
m = 4
X_g = (6,0)
x_i = (2,0)
obs = [(5,0), (5,1), (5,2), (4,2), (3,2), (2,2)]
print('3.6 b')
Breadth_First(x_i, X_g, n, m, obs)
Greedy_Best_First(x_i, X_g, n, m, obs)
A_star(x_i, X_g, n, m, obs)
# 3.6c) Bug Trap Problem
n = 100
m = 100

x_i = (50,55)
X_g = (75,70)
# Create bug trap grid

obs=[]
for i in range(n):
  for j in range(m):
    if i<50:    # rear of bugtrap
        d=abs(i-51)+abs(j-50)
        if d==50:
            obs.append((i,j))
    else:        # front of bugtrap
        if j>50:  # upper lobe
            d=abs(i-50)+abs(j-75)
            if d==24:
                obs.append((i,j))
        if j<50:  # lower lobe
            d=abs(i-50)+abs(j-25)
            if d==24:
                obs.append((i,j))
print('3.6 c')
Breadth_First(x_i, X_g, n, m, obs)
Greedy_Best_First(x_i, X_g, n, m, obs)
A_star(x_i, X_g, n, m, obs)

# 3.6d) Reverse initial and goal points
temp = x_i
x_i = X_g
X_g = temp
print('3.6 d')
Breadth_First(x_i, X_g, n, m, obs)
Greedy_Best_First(x_i, X_g, n, m, obs)
A_star(x_i, X_g, n, m, obs)