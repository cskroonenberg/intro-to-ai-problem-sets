from random import random
import matplotlib.pyplot as plt

# Example 1: P(-J, -M, B, E) 
# P(-J, -M, B, E) = P(-J | -M, B, E)*P(-M | B, E)*P(B | E)*P(E)
# P(-J, -M, B, E) = P(-J | B, E)*P(-M | B, E)*P(B)*P(E)

TRIALS = 10**6

B = ["B", "E", "A", "J", "M"]
WEIGHTS = {
    "B": {
        True: 0.001,
        False: 0.999
    },
    "E": {
        True: 0.002,
        False: 0.998
    },
    "A": {
        (True, True): {
            True: 0.98,
            False: 0.02
        },
        (True, False): {
            True: 0.95,
            False: 0.05
        },
        (False, True): {
            True: 0.29,
            False: 0.71
        },
        (False, False): {
            True: 0.001,
            False: 0.999
        }
    },
    "J": {
        True: {
            True: 0.95,
            False: 0.05
        },
        False: {
            True: 0.01,
            False: 0.99
        }
    },
    "M": {
        True: {
            True: 0.70,
            False: 0.30
        },
        False: {
            True: 0.01,
            False: 0.99
        }
    }
}

def likelihood_weighting(E, Q, N):
    counts = {True: 0.0, False: 0.0}
    for trial in range(1, N+1):
        sample = {}
        weight = 1
        for X in B:
            if X in E:
                sample[X] = e[X]
                if X == "B" or X == "E":
                    w = WEIGHTS[X][sample[X]]
                elif X == "A":
                    w = WEIGHTS[X][(sample["B"], sample["E"])][sample[X]]
                elif X == "J" or X == "M":
                    w = WEIGHTS[X][sample["A"]][sample[X]]
                weight = weight * w
            else:
                randX = random()
                if X == "B" or X == "E":
                    sample[X] = (randX < WEIGHTS[X][True])
                elif X == "A":
                    sample[X] = (randX < WEIGHTS[X][(sample["B"], sample["E"])][True])
                elif X == "J" or X == "M":
                    sample[X] = (randX < WEIGHTS[X][sample["A"]][True])
        v = sample[Q]
        counts[v] = counts[v] + weight
    sum = counts[True] + counts[False]
    return (counts[True] / sum, counts[False] / sum)

# Example 1: P(-J, -M, B, E) 
# P(-J, -M, B, E) = P(-J | -M, B, E)*P(-M | B, E)*P(B | E)*P(E)
# P(-J, -M, B, E) = P(-J | -M, B, E)*P(-M | B, E)*P(B)*P(E)
e = {"B" : True, "E" : True, "M" : False}
p1 = likelihood_weighting(e, "J", TRIALS)
e = {"B" : True, "E" : True}
p2 = likelihood_weighting(e, "M", TRIALS)
p3 = WEIGHTS["B"][True]
p4 = WEIGHTS["E"][True]
p5 = p1[1] * p2[1] * p3 * p4
print("P(-J, -M, B, E) = P(-J | -M, B, E)*P(-M | B, E)*P(B)*P(E)")
print("P(-J | -M, B, E) ~=", p1[1])
print("    P(-M | B, E) ~=", p2[1])
print("            P(B) ~=", p3)
print("            P(E) ~=", p4)
print(" P(-J, -M, B, E) ~=", p5)