# Lists can be multitype but the good practice is to keep them single type.
# There must be a whitespace between list items.
numbers = [1, -2, 3, -4, 5]
words = ["apple", "banana", "kiwi"]

# Access by using indexes like in Java: 0 to length-1; [length] = list index out of range error

print(words[2])
print(words)

# del is a keyword for delete. This operation deletes a specific index. After deletion, the list is shortened and the previous i+1 element becomes the i-th element.

del words[1]
print(words)
print(words[1])

# Strings can be accessed by using indexes too. BUT strings are immutable, you cannot delete a symbol from the string by using del.

my_string = "Galyush"
print(my_string[3])

# Appending elements to a list

words.append("plum")
words = words + ["orange", "grapefruit"]
print(words)

# Getting an index of an element in the list:
plum_index = words.index("plum")
print(plum_index)

# Converting int to string, otherwise error, no silent conversion like in Java, so print("string " + int) produces error
print("plum_index: " + str(plum_index))

# Removing the element from list. Searching for index and deleting this element. Or using remove command which removes the matching element from the list.
del words[plum_index]
print(words)

words.remove("orange")
print(words)

# What if "orange" twice? Remove deletes the first matching element and doesn't search the rest.
# Things like words.append().append() do not work here
words = words + ["orange", "pineapple", "orange"]
print(words)
words.remove("orange")
print(words)

# Python list API
# https://docs.python.org/3.4/tutorial/datastructures.html


