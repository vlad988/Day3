import datetime
def GCD(x,y):
    if x == y:
        return x
    if x > y:
        return GCD(x-y, y)
    else:
        return GCD(x, y-x)
print(GCD(50,40))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")
