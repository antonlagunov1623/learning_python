##################################################
#### all strings in python are immutable sequences
##################################################

# initialization of string
s = 'Spam'
print("String s - {}".format(s))
print("Length of string s - {}".format(len(s)))
print("First element of string s - {}".format(s[0]))
print("Second element of string s - {}".format(s[1]))
print("Last element of string s - {}".format(s[-1]))
print()

print("Slicing:")
print("All elements of string s from second to third - {}".format(s[1:3]))
print("All elements of string s from first to third - {}".format(s[:3]))
print("All elements of string s from second to the last - {}.".format(s[1:]))
print("All elements of string s except the last - {}".format(s[:-1]))
print()

s1 = 'xyz'
print("Operations:")
print("Concatination of strings s and s1 - {}".format(s + s1))
print("Repeating of string s 8 times - {}".format(s * 8))
print()

print("Strings in python are immutable:")
print("We can't do this:")
try:
    s[0] = 'a'
except TypeError:
    print("TypeError: ‘str’ object does not support item assignment")
print()

print("Helping:")
print("See methods for value of specific data type:")
print(dir(s))
print("See the description of methods:")
# print(help(s.upper))

print("Methods:")
print("Find an index of start of substring - {}".format(s.find('pa')))
print("Replace all substrings on another ones - {}".format(s.replace('pa', 'xyz')))
line = 'aaa,bbbb,ccc,dd'
print("Split line with divider and return list of substrings - {}".format(line.split(',')))
print("Up all characters in string s - {}".format(s.upper()))
print("Test of string s on character/string - {}".format(s.isalpha()))
print("Test of string s on digit - {}".format(s.isdigit()))
line = 'aaa,    bbbb,ccc  ,dd   \n'
print("Delete all gape and final characters in the end of line - {}".format(line.rstrip() + 'a'))
print()

print("Any other ways to represent strings:")
print("Number of symbol v in ASCII - {}".format(ord('v')))
msg = """rrrr  
kkkkk mmmmm     ''''
""""    hhh"""
print("Multistring literals:")
print(msg)
print("Raw strings:")
b = r"r\n\ny"
print(b)
print("See the difference:")
a = "r\n\ny"
print(a)
print()

print("Search with template:")
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
print(match.group(1))
print(match.groups())
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())
print()