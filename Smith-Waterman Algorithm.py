#  File: Smith-Waterman Algorithm.py

#  Description: Performs the Smith-Waterman Algorithm on two sequences of DNA.
#               The purpose is to find the best way to align them.
#               One of the many ways to determine how similar two sequences of DNA are.

#  Name: Carlos Vazquez

#  Date Created: 10-25-23

#  Date Last Modified: 12-11-23

#  Notes: My curiousity was piqued after hearing this algorithm described in my Comp. Bio class.
#         To my disappointment, we were not told to implement it. I decided to do so on my own, which
#         turned out to be a bit easier than I anticipated. It was finished in a day.
#         Update note: Changed input method so that inputing the DNA sequences is simpler.

import math as m

def greatest_val(matrix, matching, coords):
    row, col = coords[0], coords[1]
    vals = []
    vals.append(0)
    vals.append(matrix[row][col - 1] - 2)
    vals.append(matrix[row - 1][col] - 2)
    if(matching):
        vals.append(matrix[row - 1][col - 1] + 3)
    else:
        vals.append(matrix[row - 1][col - 1] - 3)

    return max(vals)    

def initialize_matrix(DNA_a, DNA_b):
    matrix = []
    for i in range(len(DNA_a) + 1):
        matrix.append([])
        for q in range(len(DNA_b) + 1):
            matrix[i].append(0)

    for i in range(1, len(matrix)):
        for q in range(1, len(matrix[i])):
            if(DNA_a[i - 1] == DNA_b[q - 1]):
                matching = True
            else:
                matching = False
            matrix[i][q] = greatest_val(matrix, matching, [i,q])
    return matrix

def find_alignment_path(matrix):
    temp = []
    for i in range(len(matrix)):
        temp.extend(matrix[i])

    row, col = m.floor(temp.index(max(temp)) / len(temp) * len(matrix)), temp.index(max(temp)) % len(matrix[0]) # recreate index
    coords = [[row, col]]
    print(coords)
    if(row > col): loop_length = row - 1
    else: loop_length = col - 1
    for i in range(loop_length):
        vals = [] # List of adjacent values(left, top left, up) and corresponding coords
        if(row == 2 and col == 2):
            coords.append([1,1])
            break
        for i in range(3):
            vals.append([matrix[row - 1][col - 1], row - 1, col - 1])  # [value, row coordinate, col coordinate]
            vals.append([matrix[row - 1][col], row - 1, col])
            vals.append([matrix[row][col - 1], row, col - 1])
            vals.sort()
            vals.reverse()
        coords.append([vals[0][1], vals[0][2]])
        row, col = [vals[0][1], vals[0][2]]
    
    return coords

def align(coords, a, b):
    aligned = ['', '']
    coord = coords[0]
    
    for next_coord in coords:
        if(coord == next_coord):
            continue
        if(next_coord[0] == coord[0]):
            aligned[0] = ' ' + aligned[0]
            aligned[1] = b[coord[1] - 1] + aligned[1]
        elif(next_coord[1] == coord[1]):
            aligned[0] = a[coord[0] - 1] + aligned[0]
            aligned[1] = ' ' + aligned[1]
        else:
            aligned[0] = a[coord[0] - 1] + aligned[0]
            aligned[1] = b[coord[1] - 1] + aligned[1]
        coord = next_coord

    
    for i in aligned:
        print(i)

        
DNA_a = 'GGTTGACTA'
DNA_b = 'TGTTACGG'

f = open("DNA_Input.txt", "r")
temp = f.read().split('\n')
f.close()
DNA_a = temp[0]
DNA_b = temp[1]

matrix = initialize_matrix(DNA_a, DNA_b)

for i in matrix:
    print(i)

coord_list = find_alignment_path(matrix)
align(coord_list, DNA_a, DNA_b)








