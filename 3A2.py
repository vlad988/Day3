import datetime
def block(n):
    if n == 0:
        return 1
    else:
        return block(n-1)*2*(2*n-1)//(n+1)
print(block(8))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

