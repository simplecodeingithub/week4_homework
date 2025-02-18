import random  # Importing the random module to generate random numbers
#help(random)

# numbers = [1, 2, 3, 4, 5]
# print(random.sample(numbers, 2))

#The random.sample() function generates a list of unique numbers,Selects 6 unique random numbers from the range 1 to 49.
lottery_numbers = random.sample(range(1,50),6)
print(f"List of unique random numbers are: {lottery_numbers}")

print('#' * 50)

lotto_numbers = set()
print(type(lotto_numbers))

while len(lotto_numbers) < 6:
    number = random.randint(1,50)
    # Check if the number is already in the list
    if number not in lotto_numbers:
        lotto_numbers.add(number)
print(f"List of random numbers: {sorted(lotto_numbers)}")

print('#' * 50)
# # Using set-The list produced by random.sample() is converted to a set,
# lottery_numbers = set(random.sample(range(1,51),6))
# print(lottery_numbers)
# lotto = list(lottery_numbers)
# print(lotto)

# lotto_numbers = range(1,51)
# print(f"Six Unique random numbers are: {random.sample(lotto_numbers,6)}")




