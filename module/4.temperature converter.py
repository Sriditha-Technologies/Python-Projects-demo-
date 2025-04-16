def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = 25
print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
fahrenheit = 77
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")