element = [120, 5.7, "Hello", 0, "WoRlD", "67", [1, 34, 0.9], {}]


def elements(list):
    count = 0
    for element in list:
        count += 1
    return count


print("Total elements in the list: ", elements(element))
