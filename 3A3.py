import datetime
def hala(x, n):
    if n == 0:
        return 1
    else:
        return x * hala(x, n-1)
print(hala(2,11))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

