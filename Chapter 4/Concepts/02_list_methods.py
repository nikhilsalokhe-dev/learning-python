lists = ["String", 23, 63.8, False, "Name", True, "Fruit", "City", 900]

print(lists)

lists.append("New_String")

print(lists)

number_list = [8, 84, 36, 90, 1, 43]

number_list.sort()
print("Sorted list:", number_list)
number_list.reverse()
print("Reversed list:", number_list)

lists.insert(3, 12)  # Insert 12 at the index 3
print(lists)

value = lists.pop(3)
print("The value that will be removed is", value)
print(f"The new list is: {lists}")

lists.remove("New_String")
print(f"The original string is: {lists}")
