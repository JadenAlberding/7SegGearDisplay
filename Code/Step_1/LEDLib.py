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

def rev():
    led_top.on()
    led_right_top.on()
    led_right_bottom.on()
    led_left_top.on()
    led_left_bottom.on()
    led_middle.on()
    led_bottom.off()
