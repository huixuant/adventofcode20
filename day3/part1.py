def main():
    with open('input', 'r') as file:
        rows = file.readlines()
    length = len(rows[0])-1
    trees = 0
    count = 3
    for i in range(1, len(rows)):
        count %= length
        if (rows[i][count] == '#'):
            trees += 1
        count += 3
    print(trees)
    
if (__name__ == '__main__'):
    main()
