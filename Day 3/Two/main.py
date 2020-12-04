#!/bin/python

def calculate_slope(lines, slope_x, slope_y):
    wrapping_point = len(lines[0].strip())
    lines_len = len(lines)
    trees = 0
    for i in range(1, int(lines_len/slope_y)):
        line = lines[i*slope_y].strip()
        index = (i*slope_x) % wrapping_point
        char = line[index]
        if char == "#":
            print(line[:index] + "X" + line[index+1:])
            trees += 1
        else:
            print(line[:index] + "O" + line[index+1:])

    return trees



with open("input", 'r') as input:
    lines = input.readlines()
    slopes = [(1,1),(3,1),(5,1), (7,1), (1,2)]
    total = 1
    for slope in slopes:
        trees = calculate_slope(lines, slope[0], slope[1])
        total *= trees
        print(f"Total: {total}, Trees: {trees}")
