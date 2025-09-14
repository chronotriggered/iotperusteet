import machine
import utime
import urandom

start = 0

led = machine.Pin(0, machine.Pin.OUT)
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

def btnHandler(pin):
    btn.irq(handler=None)
    reaction = (utime.ticks_diff(utime.ticks_ms(), start) / 1000)
    print("Your reaction time was " + str(reaction) + " seconds")


led.value(1)
utime.sleep(urandom.uniform(3, 10))

led.value(0)
start = utime.ticks_ms()

btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=btnHandler)