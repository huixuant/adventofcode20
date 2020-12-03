def parse_line(line):
    minmax_range, char, string = line.split(' ')
    min_char, max_char = minmax_range.split('-')
    char = char[0]
    return(int(min_char), int(max_char), char, string)

def check_valid(min_char, max_char, char, string):
    occurrences = string.count(char)
    return occurrences >= min_char and occurrences <= max_char

def main():
    with open('input', 'r') as file:
        lines = file.readlines()

    total_valid = 0
    for line in lines:
        min_char, max_char, char, string = parse_line(line)
        if check_valid(min_char, max_char, char, string):
            total_valid += 1

    print(total_valid)
        
if (__name__ == '__main__'):
    main()
