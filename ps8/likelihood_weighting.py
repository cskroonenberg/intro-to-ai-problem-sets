# likelihood weighting in Bayes Networks
# Caden Kroonenberg, 2022-04-03
# See: https://artint.info/2e/html/ArtInt2e.Ch8.S6.SS4.html
from random import random

TRIALS = 10**7

vars = {
    'B': [0.001],           # [P(B)]
    'E': [0.002],           # [P(E)]
    'A': [[0.001, 0.29],    # [[P(A | -B, -E), P(A | -B, +E)],
          [0.95, 0.98]],    #  [P(A | +B, -E), P(A | +B, +E)]]
    'J': [0.01, 0.95],      # [P(J | -A), P(J | +A)]
    'M': [0.01, 0.70]       # [P(M | -A), P(M | +A)]
}

def likelihood_weighting(B, e, Q, n):
    counts = [0,0] # [False count, True count]
    for trial in range(1,n+1):
        sample = {}
        weight = 1
        for x in B:
            if x in e:
                v = e[x]
                sample[x] = v
                if x == 'B' or x == 'E':
                    weight *= (B[x][0]) if sample[x] else (1 - B[x][0])
                elif x == 'A':
                    weight *= (B[x][sample['B']][sample['E']]) if sample[x] else (1 - B[x][sample['B']][sample['E']])
                elif x == 'J' or x == 'M':
                    weight *= (B[x][sample['A']]) if sample[x] else (1 - B[x][sample['A']])
            else:
                if x == 'A':
                    sample[x] = (random() < B[x][sample['B']][sample['E']])
                elif x == 'J' or x == 'M':
                    sample[x] = (random() < B[x][sample['A']])
                elif x == 'B' or x == 'E':
                    sample[x] = (random() < B[x][0])
        v = sample[Q]
        counts[v] += weight
    return [round(x / sum(counts), 3) for x in counts]

# P(-J, -M, B, E) = P(-J | -M, B, E)P(-M | B, E)P(B)P(E)

# P(B)
p_b = vars['B'][0]

# P(E)
p_e = vars['E'][0]

# P(-J | -M, B, E)
e = {
    'M': False,
    'B': True,
    'E': True
}
P_j = likelihood_weighting(vars, e, 'J', TRIALS)
print('P(+J | -M, B, E): {}'.format(P_j[0]))
p_j = P_j[0]

# P(-M | B, E, A)
e = {
    'B': True,
    'E': True
}
P_m = likelihood_weighting(vars, e, 'M', TRIALS)
print('P(+M | B, E): {}'.format(P_m[0]))
p_m = P_m[0]

joint_p = p_j*p_m*p_b*p_e

print('P(-J, -M, B, E) = {}'.format(joint_p))