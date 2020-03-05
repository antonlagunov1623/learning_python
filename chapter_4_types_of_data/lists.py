################################
#### lists are mutable sequences
################################

l = [123, 'spam', 1.23]
print("Like for the strings we can get elements of lists by indexes and get slices:")
print(l[-1])
print(l[:-1])
print()

print("We can also concatenate two lists:")
print(l + ['xyz', 69])
print()

print("Methods:")
print("Appending new element at the end of the list l - {}".format(l.append('NI')))
print("Removing the third element of the list l - {}".format(l.pop(2)))
print("Or something like this:")
del l[2]
print(l)
abc = ['bbb', 'ccc', 'aaa']
print("Sorting elements of the list - {}".format(abc.sort()))
print("Reversing elements of the list - {}".format(abc.reverse()))
print()

print("Test on the index out of border:")
try:
    print(l[99])
except IndexError:
    print("IndexError: list assignment index out of range")
try:
    l[99] = 0
except IndexError:
    print("IndexError: list assignment index out of range")
print()

print("Lists in list:")
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print("Matrix M 3x3 - {}".format(M))
print("Second row of matrix M - {}".format(M[1]))
print("Element in third column and second row - {}".format(M[1][2]))
print()

