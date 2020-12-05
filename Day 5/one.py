#!/bin/python

with open("input", 'r') as input:
    seat_id_max = 0
    for line in input:
        line = line.strip()
        row_lower = 0
        row_upper = 127
        
        col_lower = 0
        col_upper = 7

        row_chars = line[:7]
        col_chars = line[7:]

        for char in row_chars:
            if char == 'F':
                row_upper = (row_lower + row_upper) // 2
            elif char == 'B':
                row_lower = (row_lower + row_upper) // 2

        for char in col_chars:
            if char == 'L':
                col_upper = (col_lower + col_upper) // 2
            elif char == 'R':
                col_lower = (col_lower + col_upper) // 2

        seat_id = row_upper * 8 + col_upper

        seat_id_max = max(seat_id, seat_id_max)

    print(seat_id_max)

