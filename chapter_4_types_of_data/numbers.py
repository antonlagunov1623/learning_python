#################################################################
#### supported number types:
#### - int
#### - float
#### - rational numbers (two numbers - numerator and denominator)
#### - complex numbers
#### - fixed precision numbers
#################################################################

print("Operations:")
print("Result of addition of 123 and 222 - {}".format(123 + 222))
print("Result of multiplication of 1.5 and 4 - {}".format(1.5 * 4))
print("2 in power of 100 - {}".format(2 ** 100))
print("Number of cyphers in number 2 ** 100 - {}".format(len(str(2 ** 100))))
print()

print("Useful modules: math and random:")
import math
import random
print("PI number - {}".format(math.pi))
print("Second root of 85 - {}".format(math.sqrt(85)))
print("Random float number from 0 to 1 - {}".format(random.random()))
print("Random element of list - {}".format(random.choice([1, 2, 3, 4])))
print()
