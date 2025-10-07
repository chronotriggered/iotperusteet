import network
import time
import urequests
from machine import Pin
import dht

ssid = "Wokwi-GUEST"
password = ""

THINGSPEAK_URL = "http://api.thingspeak.com/update"
THINGSPEAK_API_KEY = "B5Z7032Q1KD9MNK6"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)
print("Connecting to WiFi...")
print("Connected to WiFi")
print("IP Address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(15))


def send_to_thingspeak(temperature, humidity):
    try:
        response = urequests.post(
            THINGSPEAK_URL,
            data="api_key={}&field1={}&field2={}".format(
                THINGSPEAK_API_KEY, temperature, humidity),
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.close()
    except Exception as e:
        print("Failed to send data to ThingSpeak:", e)


while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")
        send_to_thingspeak(temperature, humidity)
    except Exception as e:
        print("Error:", e)

    time.sleep(20)
