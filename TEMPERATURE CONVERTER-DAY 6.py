def celsius_to_fahrenheit():
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius():
    return (fahrenheit - 32) * 5/9

def main():
    global celsius, fahrenheit
    print('Temperature Converter')
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    choice = input('Choose an option: ')
    if choice =='1':
        try:
            celsius = float(input('Enter temperature : '))
            fahrenheit = celsius_to_fahrenheit()
            print(f'Temperature in Fahrenheit is  {fahrenheit}')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')
    elif choice =='2':
        try:
            fahrenheit = float(input('Enter temperature : '))
            celsius = fahrenheit_to_celsius()
            print(f'Temperature in Celsius is  {celsius}')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

    else:
        print('Invalid choice.')

main()