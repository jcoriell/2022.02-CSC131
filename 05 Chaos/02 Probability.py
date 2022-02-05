
# Def:The probability of something occurring is 
# the number of ways of achieving success out of the 
# total number of possibilities.
# It is a value between 0 and 1.
# 0 means no chance of happening
# 1 means 100% chance of happening

# Ex: Probability of rolling a 2 on a 6 sided die
sides_with_2 = 1
total_sides = 6
prob_of_rolling_a_2 = sides_with_2 / total_sides
print(f"Rolling a two: {prob_of_rolling_a_2}")

# Ex: Probability of rolling an even value on a D20
sides_with_even_numbers = 10
total_sides = 20
prob_of_even = sides_with_even_numbers / total_sides
print(f"Rolling a even value: {prob_of_even*100}%")

# Simulating a die roll
from random import randint

probabilities = [0]*6   # list of length 6 with 0 in each spot

rolls = 1000
for i in range(rolls):
    value = randint(1,6)
    probabilities[value - 1] += 1

print(probabilities)
for i in range(len(probabilities)):
    probabilities[i] = probabilities[i]/rolls

print(probabilities)


# A script that shows the frequency/probability 
# of each sum of rolling two dice.

# Possible sums [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
freqs = [0]*11

print("Die1\tDie2\tSum")

for die1 in range(1,7):
    for die2 in range(1, 7):
        dice_sum = die1 + die2
        # Increment the appropriate item in the list
        # If the sum is 2, we increment index 0
        # If the sum is 3, we increment index 1
        # ..
        # If the sum is 12, we increment index 10
        freqs[dice_sum - 2] += 1
        print(f"{die1}\t{die2}\t{dice_sum}")

print(freqs)

print("\nSum\tFreq\tProb")
for i in range(len(freqs)):
    print(f"{i+2}\t{freqs[i]}\t{freqs[i] / sum(freqs)}")

# A dictionary way of doing the previous script
freqs = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
print("\nDie1\tDie2\tSum")
for die1 in range(1,7):
    for die2 in range(1,7):
        dice_sum = die1 + die2
        freqs[dice_sum] += 1
        print(f"{die1}\t{die2}\t{dice_sum}")


print("\nSum\tFreq\tProb")
for key, value in freqs.items():
    print(f"{key}\t{value}\t{value/sum(freqs.values())}")


# Probabilities are not always what they seem

# Imagine wanting to calculate the probs of each of the following
# Flipping two coins and getting...
    # The result being two heads
    # The result being two tails
    # The results being one heads and one tails

# The options
# Coin 1        Coin 2  
#   H             H
#   H             T
#   T             H
#   T             T



