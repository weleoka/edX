#!/usr/bin/env python
s = "aabobhtelboboabcdefghijklmnopbsssarrcefghijabcdssssss"

""" 
Number 1:
Count up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: 5
"""
count = 0
for letter in s:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print "(1) Number of vowels %s " % count



"""
Number 2
Print the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print: 2
"""
li = [letter for letter in s]

# for letter in s:
   # li.append(letter)
i = 0
count = 0
for item in li:
    if len(li) - i < 3: break

    temp = li[i:i+3]

    string = ''.join(temp)

    if string == 'bob':
        count += 1

    i += 1

print "(2) Found %s instances of bob in the supplied string." % count



"""
Number 3
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print: abc
"""
sLi = [letter for letter in s]
alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]
dictionary = {y: x for x, y in enumerate(alphabet)}

temp = []
data =[]
last = 0

for item in sLi:
    
    current = dictionary[item]

    if current == last:
        temp.append(item)

    elif current > last:
        temp.append(item)

    elif current < last:
        data.append(''.join(temp))
        del temp[:]
        temp.append(item)

    last = current

data.append(''.join(temp))  # To include the last set.

i = 0
for substr in data:
    substr_len = len (substr)
    if substr_len > i:
        winner = substr
        i = substr_len


print "(3) Longest alphabetically ordered substring in s is: %s" % winner
