from gpiozero import LED
from time import sleep
from sevSegLED import one,two,three,four,five,six,seven,eight,nine,zero,turnAllOFF

while True:
    for i in range(0,10,1):
        if i == 1:
            one()
        if i == 2:
            two()
        if i == 3:
            three()
        if i == 4:
            four()
        if i == 5:
            five()
        if i == 6:
            six()
        if i == 7:
            seven()
        if i == 8 :
            eight()
        if i == 9:
            nine()
        sleep(0.2)
