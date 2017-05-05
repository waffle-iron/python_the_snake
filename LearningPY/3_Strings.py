# Single and double quotes

single_quote = 'I "really" like chocolate.'
double_quote = "I 'really' like chocolate."

# Escaping = mirroring symbols

single_escaping = 'I \'really\' like chocolate.'
double_escaping = "I \"really\" like chocolate."

# Triple quote strings can be used for placing a multiline paragraph string inside. Also they can be used as comments

paragraph = '''
This is a
multiline
paragraph.
'''

'''This is a comment within the triple code Strings.
   Such comments can be multiline unlike the #-comments.'''

# Python String API
# String methods documentation https://docs.python.org/3/library/stdtypes.html#string-methods
# String documentation https://docs.python.org/3/library/string.html
# To make the change in the string persistent save it in the variable.
upper_case = "UPPER_CASE_STRING"
lower_case = "lower_case_string"
upper_case = upper_case.lower()
lower_case = lower_case.upper()
print(upper_case, lower_case, sep='; ')

# Stripping white space - like sapces and tabs in the string from the left and from the right but not in the middle.
# Argument ('chars_to_ber_removed')

white_spaces = "          white         spaces               "
print(white_spaces.strip().upper())

# Concatenation methods
prefix = "This is the beginning of the sentence "
suffix = "and this is the ending of the same sentence."
whole_sentence = prefix + suffix
print(whole_sentence)

# Duplicating the string - hidden concatenation by multiplication

whole_sentence = whole_sentence * 2

# Replacing words. Count parameter says how many replacements should be done - here the first two.

whole_sentence = whole_sentence.replace("sentence", "string", 2)
print(whole_sentence)

# Count substring appearances

print(whole_sentence.count("ing"))

# Formatting different variable types. Format is put within the curly braces inside the string.
# e - exponential = scientific notation
# b - binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadesimal (base 16)
# f - float
# s - string (default when nothing is specified)

eleven = 11
ten_thousand = 10000
floating = 1.23456789
word = "a word"

print("my number is {:d}".format(eleven))
print("my number is {:b}".format(eleven))
print("my number is {:e}".format(ten_thousand))
print("{:f}".format(floating))
# Formatting for 3 digits after the point. The number is rounded mathematically.
print("{:.3f}".format(floating))
# Padding with zeroes. 10 is the total length of the final string so 5 zeroes will be added.
# https://pyformat.info
print("{:010.3f}".format(floating))
print("{0} {1} {2}".format(eleven, floating, word))
print("{name} own(s) {number} of {objects}".format(
    name='Galina',
    number=5,
    objects='apples'
))

# Input from the command line
first_name = input("Please, enter your first name: ").capitalize()
middle_name = input("Please, enter your middle name: ").capitalize()
last_name = input("Please, enter your last name: ").capitalize()

name_format = "{last}, {first} {middle:.1s}."
print(name_format.format(last=last_name, first=first_name, middle=middle_name))

# Practice: http://codingbat.com/python/String-1





