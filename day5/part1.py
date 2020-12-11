def find_column(bp):
    min_col = 0
    max_col = 7
    for i in range(7, 9):
        if (bp[i] == 'L'):
            max_col = (max_col + min_col) // 2
        else:
            min_col = (max_col + min_col) // 2 + 1
    if (bp[9] == 'L'):
        return min_col
    return max_col
    
def find_row(bp):
    min_row = 0
    max_row = 127
    for i in range(6):
        if (bp[i] == 'F'):
            max_row = (max_row + min_row) // 2
        else:
            min_row = (max_row + min_row) // 2 + 1
    if (bp[6] == 'F'):
        return min_row
    return max_row

def main():
    with open('input', 'r') as file:
        bps = file.readlines()

    max_seat = 0
    for bp in bps:
        row = find_row(bp)
        column = find_column(bp)
        seat = row * 8 + column
        if (seat > max_seat):
            max_seat = seat
    
    print(max_seat)

if (__name__ == '__main__'):
    main()
