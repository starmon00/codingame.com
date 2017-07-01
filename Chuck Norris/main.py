import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#Convernts String to Bits
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

#Combine all Bits into one String
def combine_bits(bits_list):
    bit_string = ""
    for i in bit_list:
        bit_string += i[1:]
    return bit_string


bit_list = string2bits(message)
bit_string = combine_bits(bit_list)
solution = ""

count = 0
current_index = 0
future_index = 1
current = bit_string[current_index]
future = bit_string[future_index]

#Handles comparison to encode
while (current_index != len(bit_string)-2 and future_index != len(bit_string)-1):
    if current != future:
        count += 1
        if current == '1':
            solution += ("0 " + ("0" * count) + " ")
        elif current == '0':
            solution += ("00 " + ("0" * count) + " ")
        count = 0
        current_index += 1
        future_index += 1
        current = bit_string[current_index]
        future = bit_string[future_index]
    else:
        count += 1
        current_index += 1
        future_index += 1
        current = bit_string[current_index]
        future = bit_string[future_index]        


#Handles final comparison
current = bit_string[-2]
future = bit_string[-1]
count += 1
if current != future:
    if current == '1':
        solution += ("0 " + ("0" * count) + " 00 0")
    elif current == '0':
        solution += ("00 " + ("0" * count) + " 0 0")        
else:
    count +=1
    if current == '1':
        solution += ("0 " + ("0" * count))
    elif current == '0':
        solution += ("00 " + ("0" * count))
        
        
print(solution)
