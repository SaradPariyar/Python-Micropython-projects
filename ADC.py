from machine import ADC
from utime import sleep_ms


adc = ADC(26)

while True:
    v = adc.read_u16()
    if (v > 15000) & (v < 45000):
        print(v*1000)      
    sleep_ms(100)