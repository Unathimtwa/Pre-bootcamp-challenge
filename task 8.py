
def time(number):
    hour = number// 60
    minute = number % 60
    result = (str(hour) + " hours, " + str(minute) + " minutes")
    return result

print(time(40))




