from gpiozero import LED

led = LED(24)
while True:
    led.on()


