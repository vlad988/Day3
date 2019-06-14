import datetime
rf = open("text.txt")
wf = open("text2.txt","w")
for string in rf:
    new_string = string.replace("\n","")
    wf.write(new_string)
    wf.write('. ')
rf.close()
wf.close()
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")

