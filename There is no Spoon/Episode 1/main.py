import sys
import math

# Don't let the machines win. You are humanity's last hope...


width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

matrix = []
list_of_nodes = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    matrix.append(line)

index_y = 0
for y in matrix:
    index_x = 0
    if y.count('0') == 1:
        answer = (str(y.find('0'))+ ' ' + str(index_y) + ' -1 -1 ')
        index_x = y.find('0')
        if index_y == len(matrix)-1:
            answer += '-1 -1'
        else:
            for z in range(index_y+1,len(matrix)):
                neighbor_below = matrix[z][index_x]
                if (neighbor_below == '0'):
                    answer += (str(index_x) + ' ' + str(z))
                    break
            else:
                answer += '-1 -1'
        print(answer)
    elif y.count('0') > 1:
        for x in y:
            if (x == '0'):
                answer = str(index_x) + ' ' + str(index_y)
                try:
                    neighbor_right = y[index_x+1:].find('0')
                    if neighbor_right != -1:
                        if index_x == 0 and neighbor_right == 0:
                            answer += ' ' + str(1) + ' ' + str(index_y) + ' '
                        else:
                            answer += ' ' + str(index_x+neighbor_right+1) + ' ' + str(index_y) + ' '
                    else:
                        answer += ' -1 -1 '
                except IndexError:
                    answer += ' -1 -1 '
                if index_y == len(matrix)-1:
                    answer += '-1 -1'
                else:
                    for z in range(index_y+1,len(matrix)):
                        neighbor_below = matrix[z][index_x]
                        if (neighbor_below == '0'):
                            answer += (str(index_x) + ' ' + str(z))
                            break
                    else:
                        answer += '-1 -1'
                print(answer)                
            index_x += 1    
    index_y += 1
                    
        
                    
    
