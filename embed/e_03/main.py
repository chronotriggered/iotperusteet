import machine
import utime

led = machine.Pin(0, machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.5)