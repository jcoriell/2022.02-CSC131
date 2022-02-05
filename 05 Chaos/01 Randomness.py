
from random import randint, seed

# Definition: A pseudo-random process is one that appears to be random but is technically deterministic
# in nature. This means that the process looks completely random, and yet its pattern is predictable and
# can be reproduced exactly

print(randint(0, 100))  # Will give a different value everytime this program is run
print(randint(0, 100))  # will also give a different value evertime this program is run
print()

# A seed is a number that is used to initialize a pseudo random
# number generator

seed(123456)
print(randint(0,100))
print(randint(0,100))
print()

from time import time
from datetime import datetime # <-- look into this

print(time())


