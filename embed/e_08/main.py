import time
import dht
import machine

sensor = dht.DHT22(machine.Pin(22))

while True:
    time.sleep(2)
    sensor.measure()
    h = sensor.humidity()
    t = sensor.temperature()
    print("Temperature:", t, "Humidity:", h)