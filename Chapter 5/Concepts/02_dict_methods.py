marks = {
    # keys: values
    "Student 1": 100,
    "Student 2": 78,
    "Student 3": 56,
}

print(f"The marks of students are respectively: {marks.items()}")

print(f"The students are: {marks.keys()}")
print(f"The marks are: {marks.values()}")

marks.update({"Student 1": 99})
print("The updated new marks of Student 1 are:", marks["Student 1"])

print(f"The marks of Student 3 is: {marks['Student 3']}")
