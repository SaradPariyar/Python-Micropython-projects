import machine
import time
import umqtt

# Initialize sensors and relay module
temp_sensor = machine.ADC(4)
humidity_sensor = machine.ADC(5)
light_sensor = machine.ADC(6)
relay = machine.Pin(16, machine.Pin.OUT)


client = umqtt.MQTTClient('client_id', 'mqtt.example.com')
client.connect()

client.subscribe(b'smart_home/devices/control')

while True:
    temp = temp_sensor.read() # sensor data reading
    humidity = humidity_sensor.read()
    light = light_sensor.read()

    if temp > 30:   # Updating device status based on sensor data
        relay.value(1)
    else:
        relay.value(0)

    client.check_msg()  # Waiting for the message from the MQTT broker
    time.sleep(1)
