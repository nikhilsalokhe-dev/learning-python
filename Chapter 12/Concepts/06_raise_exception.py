while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")

        # If no error happened, break the loop
        print(f"Age successfully set to {age}.")
        break

    except ValueError as e:
        # This catches BOTH a negative number AND if they type letters like "abc"
        print(f"Invalid input: {e}. Please try again.\n")
