import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
extensions = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    extensions[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    k = fname.split(".")
    if ('.' not in fname):
        print("UNKNOWN")
    elif k[-1].lower() in extensions:
        print(extensions[k[-1].lower()])
    else:
        print("UNKNOWN")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
