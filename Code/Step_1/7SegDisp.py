import lgpio
import LEDLib as sev

HALL_1_PIN = 23
HALL_2_PIN = 24
HALL_3_PIN = 25
HALL_4_PIN = 22
HALL_5_PIN = 12
HALL_6_PIN = 27
HALL_R_PIN = 0
h = lgpio.gpiochip_open(0)



try:
    while True:
        value_hall1 = lgpio.gpio_read(h,HALL_1_PIN)
        value_hall2 = lgpio.gpio_read(h,HALL_2_PIN)
        value_hall3 = lgpio.gpio_read(h,HALL_3_PIN)
        value_hall4 = lgpio.gpio_read(h,HALL_4_PIN)
        value_hall5 = lgpio.gpio_read(h,HALL_5_PIN)
        value_hall6 = lgpio.gpio_read(h,HALL_6_PIN)
        if value_hall1 == 0:
            sev.one()
        elif value_hall2 == 0:
            sev.two()
        elif value_hall3 == 0:
            sev.three()
        elif value_hall4 == 0:
            sev.four()
        elif value_hall5 == 0:
            sev.five()
        elif value_hall6 == 0:
            sev.rev()
        else:
            sev.zero()
except KeyboardInterrupt:
    print()
finally:
    lgpio.gpiochip_close(h)
