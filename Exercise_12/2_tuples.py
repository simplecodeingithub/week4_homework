# Tuple is a collection which is ordered and immutable(unchangeable)
# tuple are created by adding comma separated values inside parentheses ( ,)
tup = 'Hello'
print(len(tup))  # Prints 5 because 'Hello' is a string, not a tuple.
print(tup)
print(type(tup))

print('#' * 50)

tup= 'Hello',    # The comma makes it a tuple
print(len(tup))  # Prints 1 because it's now a tuple with one element.
print(tup)
print(type(tup))

print('#' * 50)

tup = ('Hello',)  # The comma makes it a tuple
print(len(tup)) # Prints 1 because it's now a tuple with one element.
print(tup)
print(type(tup))