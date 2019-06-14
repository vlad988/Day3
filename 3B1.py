n = int(input("Введіть висоту: "))
def lis(n):
    r = []
    for i in range(n):
        lis = len(r)
        r = [1 if i == 0 or i == lis else r[i-1]+r[i] for i in range(lis+1)]
        yield r
def pyramid(n):
    pyr = list(lis(n))
    max = len('   '.join(map(str, pyr[-1])))
    for i in pyr:
        print('   '.join(map(str, i)).center(max)+'\n')
pyramid(n)

import datetime
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

