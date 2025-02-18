
# QUESTION 1
cheese = ['cheddar', 'stilton', 'cornish yarg']
print(cheese)

# cheese += 'oke'
# without [] it adds this as a separate elements - why?
# if we add [] and  print again that it adds correctly
# cheese += ['oke']
# print(cheese)

# add two cheeses with one command
cheese += ['Gorgonzola', 'red leicester']
print(cheese)

# add 'oke' at the end of the list
cheese.insert(9,'oke')
# index is the position starting from 0 from left
print(cheese)

# QUESTION 2
tup = 'Hello'
print(len(tup))
# prints the length of the string "hello' but it is not a tuple

tup = 'Hello',
print(len(tup))
# when we print this string the , makes a tuple of one element when we print it- the length will be 1.

