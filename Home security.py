from machine import Pin, UART
import time
import urequests
import twilio

# Initialize PIR motion sensor and camera module
pir_sensor = Pin(16, Pin.IN)
camera = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))

while True:
    if pir_sensor.value() == 1:
        camera.write(b'photo\n')
        time.sleep(2)
        photo_data = camera.read()

        response = urequests.post('http://example.com/upload_photo', data=photo_data) # Sending image to the web server

        # Send SMS alert using Twilio
        twilio.send_sms('*********', 'Intruder detected!')
        time.sleep(60)
