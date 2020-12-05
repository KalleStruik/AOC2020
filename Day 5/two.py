#!/bin/python

with open("input", 'r') as input:
    possible_seats = dict(zip([i for i in range(127 * 8 + 8)], [True for _ in range(127 * 8 + 8)]))
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

        possible_seats[seat_id] = False

    for seat_id in possible_seats:
        try:
            if possible_seats[seat_id] and not possible_seats[seat_id - 1] and not possible_seats[seat_id + 1]:
                print(seat_id)
        except:
            pass
