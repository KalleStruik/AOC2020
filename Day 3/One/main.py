#!/bin/python

slope_x = 3
slope_y = 1

with open("input", 'r') as input:
    lines = input.readlines()
    wrapping_point = len(lines[0].strip())
    trees = 0
    for i in range(1, int(len(lines) / slope_y) - 1):
        line = lines[i].strip()
        index = (i*slope_x) % wrapping_point
        char = line[index]
        if char == "#":
            print(line[:index] + "X" + line[index+1:])
            trees += 1
        else:
            print(line[:index] + "O" + line[index+1:])


    print(trees)

