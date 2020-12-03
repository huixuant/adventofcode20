def calc_trees(rows, length, horizontal, vertical):
    trees = 0
    counter = horizontal 
    for i in range(vertical, len(rows), vertical):
        counter %= length
        if (rows[i][counter] == '#'):
            trees += 1
        counter += horizontal
    return trees

def main():
    with open('input', 'r') as file:
        rows = file.readlines()
    result = 1
    length = len(rows[0])-1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        result *= calc_trees(rows, length, slope[0], slope[1])
    print(result)
    
if (__name__ == '__main__'):
    main()
