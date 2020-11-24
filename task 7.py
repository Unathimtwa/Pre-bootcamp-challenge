def temperature(temp):
    convert_temperature_to_celcius = (int(temp) - 32) * 5/9
    convert_temperature_to_fahrenheit = int(temp) * (9 / 5) + 32
    print(convert_temperature_to_fahrenheit)
    print(convert_temperature_to_celcius)

    return temperature(temp)
temperature(30)
