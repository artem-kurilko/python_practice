from collections import Counter

temperature = str(input("Enter temperature: ")).casefold()

unique_symbols = ['c', 'f', 'k']

# Calc total occurrences of temperature symbols in string
counter = Counter(temperature)
total_count = sum(counter[char] for char in unique_symbols)


ABSOLUTE_ZERO = -273.15


def print_different_temperatures(temp: float, metric: str):
    if metric == 'c':
        print(f"Fahrenheit: {celcius_to_fahrenheit(temp)}:.2f")
        print(f"Kelvin: {celcius_to_kelvin(temp)}:.2f")
    elif metric == 'f':
        print(f"Celcius: {fahrenheit_to_celcius(temp)}:.2f")
        print(f"Kelvin: {fahrenheit_to_kelvin(temp)}:.2f")
    elif metric == 'k':
        print(f"Celcius: {kelvin_to_celcius(temp):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f}")
    else:
        print(f"Exception print_different_temperatures symbol {metric}")


def celcius_to_fahrenheit(temp: float):
    return temp * 9/5 + 32


def celcius_to_kelvin(temp: float):
    return temp + (ABSOLUTE_ZERO * -1)


def fahrenheit_to_celcius(temp: float):
    return (temp - 32) * 5/9


def fahrenheit_to_kelvin(temp: float):
    return (temp - 32) * 5/9 + (ABSOLUTE_ZERO * -1)


def kelvin_to_fahrenheit(temp: float):
    return (temp + ABSOLUTE_ZERO) * 9/5 + 32


def kelvin_to_celcius(temp: float):
    return temp + ABSOLUTE_ZERO


# If temperature symbols more than one, then string invalid
if total_count > 1:
    print("Жуй говна, ты ввел неправильно")
else:
    for symbol in unique_symbols:
        if symbol in temperature:
            temp = float(temperature.split(symbol)[0].strip())
            print_different_temperatures(temp, symbol)
