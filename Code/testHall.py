import lgpio

GPIO_PIN = 21
h = lgpio.gpiochip_open(0)

lgpio.gpio_claim_input(h, GPIO_PIN)

try:
    while True:
        value = lgpio.gpio_read(h,GPIO_PIN)
        if value == 0:
            print("Mag")
        else:
            print("no mag")
except KeyboardInterrupt:
    print("done")
finally:
    lgpio.gpiochip_close(h)
