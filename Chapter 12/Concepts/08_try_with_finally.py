def main():

    try:
        n = int(input("Enter a number: "))
        print(n)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("The main function is executed.")  # Executes everytime

    print("Hey")  # This won't be printed when function is called


main()
