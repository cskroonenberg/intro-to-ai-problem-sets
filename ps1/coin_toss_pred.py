# Author: Caden Kroonenberg
# Date: 1-25-22
import random

# Heads = True, Tails = False

def predict(actual, initial, HT_prob, TH_prob):
    correct = 0                         # Count # of correct predictions
    state = initial                     # State at toss 22 = Heads
    for i in range(10):                 # For 10 'tosses'
        if state:                       # If Prev state = Heads
            if random.random() <= HT_prob:  # HT_prob probability state changes (to tails), otherwise state is unchanged
                state = False
        else:                           # If Prev state = Tails
            if random.random() <= TH_prob:  # TH_prob probability state changes (to heads), otherwise state is unchanged
                state = True
        if state == actual[i]:     # Track correct predictions
            correct+=1
        if state:
            print('T', end=' ')
        else:
            print('F', end=' ')
    print()
    print(str(correct) + ' correct predictions\t(' + str(correct*10) + '%)')            # Print correct results
    print(str(10-correct) + ' incorrect predictions\t(' + str((10-correct)*10) + '%)')  # Print error
    print()

# Real coin
real_actual = [False, False, True, True, False, False, False, False, True, True] # Actual tosses 23-32
real_initial = True # Toss 22 result
real_HT_prob = 0.5  # P(T|H)
real_TH_prob = 0.4  # P(H|T)
print('Real Coin')
predict(real_actual, real_initial, real_HT_prob, real_TH_prob)

# Simulated coin
sim_actual = [True, True, False, True, True, False, False, True, True, True] # Actual tosses 23-32
sim_initial = False # Toss 22 result
sim_HT_prob = 0.6   # P(T|H)
sim_TH_prob = 0.5   # P(H|T)
print('Simulated Coin')
predict(sim_actual, sim_initial, sim_HT_prob, sim_TH_prob)
