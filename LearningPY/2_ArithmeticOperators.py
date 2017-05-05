#!/cygdrive/c/Users/atamanki/AppData/Local/Programs/Python/Python36/python
# force using exactly this python version

sum = 1+2
substraction = 1-2
substract_negative = 1 - -2
multiplication = 3*2
exponentiation = 3**2
# Need brackets for the fractional exponent, otherwise it is power 1 divide by 3. Result is a float.
exponent_fractional = 8**(1 / 3)
# Division produces floats.
division_full = 4/2
division_float = 4.0/2
division_decimal = 7/3
# Full integer division. If a float number is divided, the result is a rounded down float number.
integer_full = 4 // 2
integer_float = 7.0 // 2
integer_decimal = 7 // 3
#Modulo = remainder from the division. The result is float if a float is divided.
modulo_full = 4%2
modulo_float = 7.0%2
modulo_decimal = 8%5

# No explicit casting to string like in Java when adding "\n" => leads to exception.
# Every new print prints its string in a new line.


print(sum)
print(substraction)
print(substract_negative)
print(multiplication)
print(exponentiation)
print(exponent_fractional)
print(division_full)
print(division_float)
print(division_decimal)
print(integer_full)
print(integer_float)
print(integer_decimal)
print(modulo_full)
print(modulo_float)
print(modulo_decimal)

