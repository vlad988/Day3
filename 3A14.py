import random
lines = open('password.txt').read().splitlines()
for i in range(len(lines)):
    if len(lines[i]) < 3:
        del lines[i]
lines = [i.title() for i in lines]
password = random.choice(lines) + random.choice(lines)
if len(password) < 8 or len(password) > 10:
    print("Your Password incorrect")
else:
    print("Your Password: ", password)

import datetime
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

