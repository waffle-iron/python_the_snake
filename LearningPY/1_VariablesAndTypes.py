name = "Galina Atamankina"

_name = "Galina"
camelCaseConvention = "camelCaseConvention"
underscore_convention = "underscore_convention"

# PEP8 - python best practices and naming conventions

string = "A string contains a sequence of Unicode characters. The variable name is not the data type!"

print(string)

# No restriction for integer size as long as it fits in the memory
postitive_integer = 123
negative_integer = -123

print(type(name))
print(type(postitive_integer))
print(negative_integer)

# Basic floating point numbers - the internal representation of them is restricted to the certain number of bits, so the precision is cut off - see the example.
# For more precision, there are other ways.

real_number = 3.1415
long_real_number = 3.1111111111111111111111111111111111111111111111111111

print(type(real_number))
print(long_real_number)

# Casting floating point numbers to integers: the numbers are always rounded down.
a = 3.4
b = 3.9
print(int(a))
print(int(b))

# Casting integer to float
c = 3
print(float(c))


