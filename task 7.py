temperature = int(input("enter temperature in degrees celsius :"))
celsius = (temperature - 32) * 5
farhenheit = temperature * 9 / 5 + 32

print(celsius)
print(farhenheit)

def temperature(temp):
    convert_temperature_to_Fahrenheit = temp * 9/ 5 + 32
    covert_temperature_to_Celcius = (temp * 9) * 5 +32
    return convert_temperature_to_Fahrenheit
