from machine import Timer, Pin, ADC
from piotimer import Piotimer
from led import Led
LED1 = 20
LED2 = 21
LED3 = 22

pin = Led(LED1)
adc = ADC(26)

def toggle_pin(tid):
     pin.value(not pin.value())
     
def read_adc(tid):
     v = adc.read_u16()
     print(v)
     
     
tmr = Piotimer(period = 500, callback = toggle_pin)
tmr2 = Piotimer(period = 100, callback = read_adc)


