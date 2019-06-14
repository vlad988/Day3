import datetime
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return x**n
    elif n % 2 == 0:
        return power(x, n/2)**2
    else:
        return x * power(x, n-1)

print(power(4,-1))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

