import machine
import time
import umqtt

soil_sensor = machine.ADC(4)
relay = machine.Pin(16, machine.Pin.OUT)

client = umqtt.MQTTClient('client_id', 'mqtt.example.com')
client.connect()

client.subscribe(b'smart_irrigation/devices/control')

while True:
    soil_moisture = soil_sensor.read()

    if soil_moisture < 1000:
        relay.value(1)
    else:
        relay.value(0)

    client.check_msg()
    time.sleep(1)
