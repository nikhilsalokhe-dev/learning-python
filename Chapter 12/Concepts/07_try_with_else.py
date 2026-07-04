try:
    n = int(input("Enter a number: "))
    print(n)

except Exception as e:
    print(e)

else:
    print("You entered a valid number!")  # Executes only when try runs successfully
