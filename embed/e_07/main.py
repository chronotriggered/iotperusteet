import machine
import utime

inputPin = 22

motion_detector = machine.Pin(inputPin, machine.Pin.IN)

new_state = 0

while True:
    current_state = motion_detector.value()
    if current_state != new_state:
        if current_state:
            print("Motion detected!")
        else:
            print("Nothing detected!")
        new_state = current_state
    utime.sleep(0.2)