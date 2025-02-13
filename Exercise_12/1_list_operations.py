cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

# cheese += 'oke'  # it treats like the string 'Oke' as a sequence of characters and adds each letter separately.
# print(cheese)

# on the right
cheese += ['oke']  # adding 'oke' as a single element,because A list is an iterable collection of elements.
print(cheese)

# append() - adds a single item to the end of the list
cheese.append('oke')
print(cheese)

# extend()- Adds multiple elements to a list.
cheese.extend(['Brie','Mozzarella'])
print(cheese)

cheese += ['Cheshire','Devon Blue']  # same as extend
print(cheese)

