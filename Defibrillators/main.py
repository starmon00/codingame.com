import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def dist(long_A, lat_A, long_B, lat_B):
    x = (long_B - long_A) * math.cos((lat_A + lat_B)/2)
    y = (lat_B - lat_A)
    return math.sqrt((x**2) + (y**2)) * 6371

lon = input()
lat = input()
n = int(input())
list_of_defib = []
answer = ''
best = 10000
for i in range(n):

    
    defib = input()
    if n == 1:
        print(defib.split(";")[1])
    else:
        lon_b = defib.split(";")[4].replace(",", ".")
        lat_b = defib.split(";")[5].replace(",", ".")
        d = dist(float(lon_b), float(lat_b), float(lon.replace(",", ".")), float(lat.replace(",", ".")))
        if d < best:
            best = d
            answer = defib.split(";")[1]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer)
