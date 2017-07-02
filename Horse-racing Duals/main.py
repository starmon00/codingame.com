import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


n = int(input())
power = []
diff = []
current_index = 0
future_index = 1
future = ''

for i in range(n):
    pi = int(input())
    power.append(pi)
power = sorted(power)
dup = sorted(list(set(power)))

if power != dup:
    print(0)
else:
    while(future != power[-1]):
        current = power[current_index]
        future = power[future_index]
        diff.append(abs(current-future))
        current_index += 1
        future_index += 1
    
    current = power[-2]
    future = power[-1]
    diff.append(abs(current-future))
    
    print(sorted(diff)[0])
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

