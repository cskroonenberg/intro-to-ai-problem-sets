# Author: Caden Kroonenberg
# Date: 1-24-22
import time, random, sys

from scipy import rand

time.sleep(2 + random.random()) # Allow for 2-3 seconds to "type" first prompt
a_in = int(input("What is the first number?\n"))
a_digit_count = len(str(a_in))  # Number of digits in 'a'
a = []                          # Store a's digits in array

for i in range(a_digit_count):  # For each digit ...
    a.append(a_in % 10)         # Convert integer digit to array entry
    a_in//=10                   # Move to next digit
    # 0.1 - 0.25 seconds to process the digit, (mental note, write down the digit, etc.)
    time.sleep(0.1 + 0.15*random.random())

time.sleep(2 + random.random()) # Allow for 2-3 seconds to "type" second prompt
b_in = int(input("What is the second number?\n"))
b_digit_count = len(str(b_in))  # Number of digits in 'b'
b = []                          # Store b's digits in array

for i in range(b_digit_count):  # For each digit ...
    b.append(b_in % 10)         # Convert integer digit to array entry
    b_in//=10                   # Move to next digit
    time.sleep(0.1 + 0.15*random.random()) # Process the digit, (mental note, write down the digit, etc.)

time.sleep(1 + random.random()) # Allow 1-2 seconds to type ackowledgement
print('Let\'s see', end='')
for i in range(random.randint(1,5)): # Add variation to acknowledgement to seem less programmed
    print('.',end='')
print()

carry = 0 # Carry

small_len, large_len = (a_digit_count, b_digit_count) if a_digit_count < b_digit_count else (b_digit_count, a_digit_count)

c = [0] * large_len # Result array

for i in range(small_len):
    c[i] = (a[i] + b[i] + carry) % 10       # Denote one's digit of sum
    carry = a[i] + b[i] + carry >= 10       # Denote carry if necessary
    time.sleep(random.random()*0.25 + 0.25)  # Take 0.25-0.5 seconds for math operation
    # (0.5 * digit #)% chance that the carry is forgotten - This makes error more likely with larger numbers
    if carry and random.random() < (i+1)*0.005:
        carry = False
    elif carry: # If carry is remembered..
        time.sleep(random.random()*0.1 + 0.1) # .. take 0.1-0.2 seconds to process this 

# If one summand is longer than the other
for i in range(small_len, large_len):       # For each extra digit the larger summand has ...
    to_add = a[i] if a_digit_count == large_len else b[i] # Add digit from larger summand
    c[i] = (to_add + carry) % 10            # Add digit to carry if necessary
    time.sleep(random.random()*0.05 + 0.25)  # Take 0.25-0.3 seconds for math operation
    carry = to_add + carry >= 10            # Denote carry if necessary
    if carry and random.random() < (i+1)*0.005: # (0.5 * digit #)% chance that the carry is forgotten
        carry = False
    elif carry: # If carry is remembered..
        time.sleep(random.random()*0.1 + 0.1) # .. take 0.1-0.2 seconds to process this 

if carry: # Account for last carry
    c.append(1)

time.sleep(random.random()*0.5 + 0.15*len(c)) # Take 0.15 * number of digits +/- 0.5 seconds to type result
print('The answer is ', end='')
for i in reversed(range(len(c))):           # Print largest digit first in output
    print(str(c[i]), end="")
print("")
print(':)') # Display human emotions

