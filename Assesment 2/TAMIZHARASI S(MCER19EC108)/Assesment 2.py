import random
from time import sleep
while True:
    temp=int(random.randint(1,100))
    hum=int(random.randint(1,100))

    if(temp>50):
       
        print("|        ALARM : HIGH TEMPERATURE       |")
       

    elif(hum>50):
       
        print("|        ALARM : HIGH HUMIDITY          |")
       
    else:
       
        print("|        ALARM : ALL OK          |")
       


    sleep(2)
