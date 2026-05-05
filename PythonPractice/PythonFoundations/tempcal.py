# Temperature Converter

def fahrenheit_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):

    fahrenheit_to_celsius = (celsius * 9/5) + 32
    return fahrenheit_to_celsius

def celsius_to_kelvin(celsius):

    celsius_to_kelvin = celsius + 273.15
    return celsius_to_kelvin

def kelvin_to_celsius(kelvin):
    
    kelvin_to_celsius = kelvin - 273.15
    return kelvin_to_celsius

def main():
    while True:
        print("Temperature Converter")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Temperature in Celsius: {celsius:.2f}")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print(f"Temperature in Kelvin: {kelvin:.2f}")
        elif choice == "4":
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print(f"Temperature in Celsius: {celsius:.2f}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")