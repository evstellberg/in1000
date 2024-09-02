while True:
    temp_fahrenheit = input("Skriv inn temperaturen i fahrenheit: ")
    try:
        temp_fahrenheit = float(temp_fahrenheit)
        break
    except ValueError:
        print("Det er ikke ett tall, prøv på nytt.")


print(f"Temperatur i fahrenheit: {temp_fahrenheit}")

temp_celsius = (temp_fahrenheit - 32) * 5 / 9

print(temp_celsius)