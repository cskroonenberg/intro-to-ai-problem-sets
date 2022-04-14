# Author: Caden Kroonenberg
# Value Iteration of 4x3 world shown in Fig. 17.1 of R&N

import numpy as np

R = -1

def actionRewardFunction(initialPosition, action):
    if initialPosition in termination_states:
        return initialPosition, 0
    
    # reward = R
    finalPosition = np.array(initialPosition) + np.array(action)

    if -1 in finalPosition or finalPosition[0] == gridSize[0] or finalPosition[1] == gridSize[1] or (finalPosition == [1,1]).all(): 
        finalPosition = initialPosition
        
    return finalPosition, R

def otherActions(action):
    if action == 0 or action == 2: # If Right or Left
        return 1, 3 # Return Up, Down
    else: # If Up or Down
        return 0, 2 # Return Right, Left

gamma = 1
gridSize = [4,3]
termination_states = [[3,2], [3,1]]
states = [[i,j] for i in range(gridSize[0]) for j in range(gridSize[1])]
states.remove([1,1]) # blocked state

actions = {0: [1,0], 1: [0,1], 2: [-1,0], 3: [0,-1]} # [Right, Up, Left, Down]

values = np.zeros((4,3))
values[3][2] = 1
values[3][1] = -1
# Print epoch 0 values (initial values)
print("Iteration 0 (Initial Values)")
print(values)
print("")

# Value Iteration
for i in range(100):
    copyValues = np.copy(values)
    for s in states:
        # Rewards for each action
        q_values = {a: 0 for a in actions}
        for a in actions:
            # intended direction
            s_, reward = actionRewardFunction(s, actions[a])
            q_values[a] += 0.8*(reward + gamma*values[s_[0], s_[1]])
            for a_ in otherActions(a): # unintended direction
                s_, reward = actionRewardFunction(s, actions[a_])
                q_values[a] += 0.1*(reward + gamma*values[s_[0], s_[1]])
        
        copyValues[s[0], s[1]] = np.max(list(q_values.values())) # util'[state] = max a in A(s)

    # Check for convergence
    comparison = values == copyValues

    # Update value array
    values = copyValues

    # Print values if convergence was reached
    if comparison.all():
        print("Iteration {} (Final Iteration)".format(i+1))
        print(values)
        print()
        # Stop iterating after convergence
        break
    
    # Print ever 10 iterations
    if (i+1) % 10 == 0:
        print("Iteration {}".format(i+1))
        print(values)
        print()