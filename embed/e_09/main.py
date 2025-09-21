import time
import dht
import machine
import network
import urequests

ssid = 'Wokwi-GUEST'
password = ''

api_key = 'B5Z7032Q1KD9MNK6'
base_url = 'https://api.thingspeak.com/update'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(machine.Pin(22))


def send_to_tspeak(temp, hum):
    if temp is None:
        print("No temperature data to send.")
        return
    try:
        response = urequests.post(
            base_url,
            data='api_key={}&field1={}&field2={}'.format(api_key, temp, hum),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)


while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")
        send_to_tspeak(temperature, humidity)
    except Exception as e:
        print("Error reading sensor or sending data:", e)

    time.sleep(15)
