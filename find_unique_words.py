# this function flattens a list that contain lists as well to only a single list


def flatten_list(flattenable_list):
    new_list = []
    for item in flattenable_list:
        if type(item).__name__.__contains__("list"):
            for i in item:
                new_list.append(i)
        else:
            new_list.append(item)
    return new_list


# this function checks if the list contains other lists


def is_flattenable(the_list):
    for item in the_list:
        if type(item).__name__.__contains__("list"):
            return True
    return False


# this function removes all the characters from a list of strings that are not letters or numbers


def reduce_to_words(the_list):
    the_list = [list(item) for item in the_list]
    # print(the_list)
    for item in the_list:
        for c in item:
            if not c.isalpha() and not c.isnumeric():
                # print(c + "is not a letter")
                item.remove(c)
        if not item[-1].isalpha() and not item[-1].isnumeric():
            item.pop(-1)

    for item in the_list:
        if len(item) == 0:
            the_list.remove(item)

    the_list = ["".join(item) for item in the_list]

    return the_list

# opening the input file for reading


with open("input.txt", "r") as rf:
    all_words = []
    lines = rf.readlines()
    words = []
    # print(lines)
    for line in lines:
        words.append(line.split())
    if is_flattenable(words):
        all_words = flatten_list(words)
    else:
        all_words = words
    set_of_all_words = set(reduce_to_words(all_words))
    # print(len(set_of_all_words))
    # print(set_of_all_words)
    # opening the output file for writing
    with open("output.txt", "w") as wf:
        for item in set_of_all_words:
            wf.write(item)
            wf.write("\n")
