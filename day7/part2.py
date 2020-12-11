def search(root, dicts):
    total = 0
    for i in root:
        contents = [item["contents"] for item in dicts if i == item["name"]]
        if (len(contents[0]) == 0):
            return 0
        else:
            for x in contents[0]:
                temp=[x["colour"]]
                total += x["quantity"] + x["quantity"] * search(temp, dicts)
    return total 

def main():
    with open('input', 'r') as file:
        data = file.readlines()

    dicts = []
    for d in data:
        d = d.rstrip('\n')
        bag_contents_list = []
        parsed = d.split(" bags contain ")
        bag_contents_raw_list = parsed[1].split(',')
        for i in bag_contents_raw_list:
            if (i != 'no other bags.'):
                temp = i.split()
                bag_colour = " ".join(temp[0:3])
                bag_contents_list.append(bag_colour)
        bag_contents_list_2 = []
        for i in bag_contents_list:
            bag_contents_dict = {}
            bag_contents_dict["colour"] = i.split(" ", 1)[1]
            bag_contents_dict["quantity"] = int(i.split(" ", 1)[0])
            bag_contents_list_2.append(bag_contents_dict)
        dicts.append({"name": parsed[0], "contents": bag_contents_list_2})

    print(search(["shiny gold"], dicts))

if __name__ == ('__main__'):
    main()
