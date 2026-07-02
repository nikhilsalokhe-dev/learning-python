# 7. Write a python function to remove a given word from a list and strip it at the same time.

random_list = ["Name", "Fruit", "Vegetable", "City", "State", "Country", "it"]


def remove(list, word):
    n = []
    for item in list:
        if not (item == word):
            n.append(item.strip(word))
    return n


print(remove(random_list, "it"))
