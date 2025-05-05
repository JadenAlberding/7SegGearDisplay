from gpiozero import LED
from time import sleep

led_top = LED(14)
led_right_top = LED(15)
led_right_bottom = LED(20)
led_middle = LED(21)
led_bottom = LED(26)
led_left_bottom = LED(6)
led_left_top = LED(17)

def turnAllOFF():
    led_top.off()
    led_right_top.off()
    led_right_bottom.off()
    led_middle.off()
    led_bottom.off()
    led_left_bottom.off()
    led_left_top.off()

    return

def zero():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.off()
    led_left_top.on()
    led_left_bottom.on()

    return

def one():
    led_top.off()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.off()
    led_middle.off()
    led_left_top.off()
    led_left_bottom.off()

    return

def two():
    led_top.on()
    led_right_top.on()
    led_right_bottom.off()
    led_bottom.on()
    led_middle.on()
    led_left_top.off()
    led_left_bottom.on()

    return

def three():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.on()
    led_left_top.off()
    led_left_bottom.off()

    return

def four():
    led_top.off()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.off()
    led_middle.on()
    led_left_top.on()
    led_left_bottom.off()

    return

def five():
    led_top.on()
    led_right_top.off()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.on()
    led_left_top.on()
    led_left_bottom.off()

    return

def six():
    led_top.on()
    led_right_top.off()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.on()
    led_left_top.on()
    led_left_bottom.on()

    return

def seven():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.off()
    led_middle.off()
    led_left_top.off()
    led_left_bottom.off()

    return

def eight():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.on()
    led_left_top.on()
    led_left_bottom.on()

    return

def nine():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_bottom.on()
    led_middle.on()
    led_left_top.on()
    led_left_bottom.off()

    return




while True:
    try:
        number = int(input("Gear: "))
        if number == 0:
            zero()
            print("0")
        elif number == 1:
            one()
            print("1")
        elif number == 2:
            two()
            print("2")
        elif number == 3:
            three()
            print("3")
        elif number == 4:
            four()
            print("4")
        elif number == 5:
            five()
            print("5")
        elif number == 6:
            six()
            print("6")
        elif number == 7:
            print("Not A Gear")
            seven()
        elif number == 8:
            print("Not A GEAR")
            eight()
        elif number == 9:
            print("!NOT A GEAR!")
            nine()
        elif number == 10:
            turnAllOFF()
        else:
            raise ValueError

    except ValueError:
        print("Not a Gear")
        break
