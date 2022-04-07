# approximate inference in Bayes Networks
# Caden Kroonenberg, 2022-04-03

# Example 2: Compute P(A | D)

from random import random

TRIALS = 10**6

evidence = 0
query = 0
pall = []
pdenomall = []

for trial in range(1,TRIALS+1):
    randA, randB, randC, randD = ( random() for i in range(4) )
    A = (randA < 0.5)
    if A:
        B = (randB < 1)
        C = (randC < 1)
    else:
        B = (randB < 0.5)
        C = (randC < 0.5)
    if B and C:  # +B and +C
        D = (randD < 1)
    elif B and not C:  # +B and -C
        D = (randD < 0.5)
    elif not B and C:  # -B and +C
        D = (randD < 0.5)
    else:   # -B and -C
        D = (randD < 0)

    # REJECTION SAMPLING: ONLY PROCESS IF EVIDENCE True
    if D:
        evidence += 1
        if A:
            query += 1
        p = query/evidence
        pall.append(p)
    pdenom = evidence/trial
    pdenomall.append(pdenom)

print("P(A|D) ~=", pall[-1])
print("P(D) ~=", pdenomall[-1])
print("P(A,D) ~=", pall[-1]*pdenomall[-1])
