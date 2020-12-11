bags = []

def search(leaf, dicts):
    global bags
    for i in leaf:
        if (i == None):
            return 
        else:
            leaf = [item["name"] for item in dicts if i in item["contents"]]
            for i in leaf:
                bags.append(i)
            search(leaf, dicts)

def main():
    with open('input', 'r') as file:
        data = file.readlines()

    dicts = []
    for d in data:
        d = d.rstrip('\n')
        bag_contents = []
        parsed = d.split(" bags contain ")
        bag_contents_raw = parsed[1].split(',')
        for i in bag_contents_raw:
            if (i != 'no other bags.'):
                temp = i.split()
                bag_colour = " ".join(temp[1:3])
                bag_contents.append(bag_colour)
        dicts.append({"name": parsed[0], "contents": bag_contents})

    search(["shiny gold"], dicts)
    global bags
    bags = list(dict.fromkeys(bags))
    print(bags)
            
if __name__ == ('__main__'):
    main()
