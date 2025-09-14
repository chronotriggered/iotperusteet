import utime
import machine

punainen_valo = False
last_press_time = 0

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
buzzer = machine.Pin(12, machine.Pin.OUT)

def interrupt_handler(pin):
    global punainen_valo, last_press_time
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_press_time) > 300:
        punainen_valo = True
        last_press_time = now

button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button.irq(trigger=machine.Pin.IRQ_RISING, handler=interrupt_handler)

def stop_traffic():
    led_red.value(1)
    for i in range(10):
        buzzer.value(1)
        utime.sleep(0.2)
        buzzer.value(0)
        utime.sleep(0.2)
    led_red.value(0)

while True:
    if punainen_valo:
        stop_traffic()
        punainen_valo = False

    led_red.value(1)
    for _ in range(20):
        utime.sleep(0.1)
        if punainen_valo:
            break
    led_red.value(0)

    led_yellow.value(1)
    for _ in range(20):
        utime.sleep(0.1)
        if punainen_valo:
            break
    led_yellow.value(0)

    led_green.value(1)
    for _ in range(50):
        utime.sleep(0.1)
        if punainen_valo:
            break
    led_green.value(0)

    led_yellow.value(1)
    for _ in range(20):
        utime.sleep(0.1)
        if punainen_valo:
            break
    led_yellow.value(0)
