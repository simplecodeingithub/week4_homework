# Set is a collection which is unordered, Immutable*, and unindexed. No duplicates.
# Set items are unchangeable, but can remove or add items - can't update or modify.
import random  # Importing the random module to generate random numbers
#help(random)
#sample(self, population, k, *, counts=None)

#The random.sample() function generates a list of unique numbers by selecting a specified number of elements from a given range (in this case, 6 numbers from range(1, 51)).
lottery_numbers = random.sample(range(1,51),6)
print(f"Six Unique random numbers are: {lottery_numbers}")

print('#' * 50)

# Using set-The list produced by random.sample() is converted to a set,
lottery_numbers = set(random.sample(range(1,51),6))
print(lottery_numbers)
# lotto = list(lottery_numbers)
# print(lotto)

print('#' * 50)

# lotto_numbers = range(1,51)
# print(f"Six Unique random numbers are: {random.sample(lotto_numbers,6)}")

lotto_numbers = [ ]
while len(lotto_numbers) < 6:
    number = random.randint(1,51)
    # Check if the number is already in the list
    if number not in lotto_numbers:
        lotto_numbers.append(number)
print(f"List of random numbers: {lotto_numbers}")




