# 2. Write a python program using function to convert Celsius to Fahrenheit.


def celciusToFahrenheit(t):
    f = 9 * t / 5 + 32
    return f


t = int(input("Enter temperature in Celcius: "))

print(f"The temperature in Fahrenheit is: {round(celciusToFahrenheit(t), 2)}")
