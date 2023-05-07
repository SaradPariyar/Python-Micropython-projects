from machine import Timer, Pin, ADC
from piotimer import Piotimer
from led import Led
from fifo import Fifo
LED1 = 20
LED2 = 21
LED3 = 22

pin = Led(LED1)
adc = ADC(26)
samples = Fifo(250)

def toggle_pin(tid):
     pin.value(not pin.value())
     
def read_adc(tid):
     global m
     x = adc.read_u16()
     samples.put(x)
     

tmr = Piotimer(period = 10, callback = read_adc)

n = 0
m = 0
while n < 1000:
    if not samples.empty():
        x = samples.get()
        m = samples.average()
        print(x)
        if x > m:
            pin.on()
        else:
            pin.off()
        n = n +1
        
tmr.deinit()

