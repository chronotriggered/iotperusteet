import machine

led = machine.Pin(18, machine.Pin.OUT)
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

led.value(0)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)