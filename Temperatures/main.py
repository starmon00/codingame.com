import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

lis = []
abs_lis = []

# Null Testcase
if temps == "":
    print(0)

#Converts str -> int
for i in temps.split(" "):
    lis.append(int(i))
    
#Converts int -> absolute value
for i in lis:
    abs_lis.append(abs(i))

#Sorts list of absolute values
sorte = sorted(abs_lis)


if (sorte[0] in lis):
    print(sorte[0])
else:
    print(-sorte[0])
