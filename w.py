from ssd1306 import SSD1306_I2C
import ssd1306
from machine import Pin, PWM, I2C, ADC
from fifo import Fifo
from piotimer import Piotimer as Timer
# from machine import Timer
from led import Led
from utime import sleep_ms

#hardware setup
adc = ADC(26)
fifo = Fifo(100)
fs = 25
i2c = I2C(1, scl = Pin(15), sda = Pin(14))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def read(tim):
    x = adc.read_u16()
    fifo.put(x)

timer = Timer(freq = fs, callback = read)

count = 0
L = 250
x = fifo.get()
while True:
    if not fifo.empty():
        count += 1
        fifo.put(x)
    
        
    m = 0
    for x in fifo.data:
        m += x
        mn = m/fifo.size
    print(mn)
        
timer.deinit()

