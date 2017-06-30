import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()


alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']


p = []


for i in t:
    if i in alphabet_lower:
        p.append(alphabet_lower.index(i))
    elif i in alphabet_upper:
        p.append(alphabet_upper.index(i))
    else:
        p.append(26)

for i in range(h):
    row = input()
    letter = ''
    for i in p:
        letter += row[i*l:i*l+l]
    print(letter)
            



