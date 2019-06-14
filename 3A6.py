import datetime
def deus(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + deus(n // 2)
    else:
        return 1 + deus(3 * n + 1)
print(deus(45))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

