#!/bin/python

with open("input", 'r') as input:
    lines = [x.strip() for x in input.readlines()] 
    for x in lines:
        x = int(x)
        for y in lines:
            y = int(y)
            if x + y == 2020:
                print(f"Found solution: x: {x}, y: {y}, result: {x*y}")
