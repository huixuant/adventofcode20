def parse_line(line):
    pos, char, string = line.split(' ')
    pos_1, pos_2 = pos.split('-')
    char = char[0]
    return(int(pos_1), int(pos_2), char, string)

def check_valid(pos_1, pos_2, char, string):
    return (string[pos_1-1] == char and string[pos_2-1] != char or
            string[pos_2-1] == char and string[pos_1-1] != char)

def main():
    with open('input', 'r') as file:
        lines = file.readlines()

    total_valid = 0
    for line in lines:
        pos_1, pos_2, char, string = parse_line(line)
        if check_valid(pos_1, pos_2, char, string):
            total_valid += 1

    print(total_valid)
        
if (__name__ == '__main__'):
    main()
