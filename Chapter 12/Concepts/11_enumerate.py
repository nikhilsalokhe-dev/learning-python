number_list = [1, 4, 45, 3, 45]

# index = 0
# for item in number_list:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(number_list):
    print(f"The item number at index {index} is {item}")
