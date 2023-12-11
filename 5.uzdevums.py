import datetime
laiks=datetime.datetime.now()
stunda=datetime.datetime.hour

if 12<= stunda :
    sveicienu="Labdien!"
elif time()<= 12:
    sveicienu="Labrīt!"
else:
    sveicienu="Labvakar!"
print(sveicienu)

