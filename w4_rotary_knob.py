from machine import Pin
from utime import time, sleep_ms

RotA = Pin(10, Pin.IN)
RotB = Pin(11, Pin.IN)
Rot_Push = Pin(12, Pin.IN, Pin.PULL_UP)

class rotary_encoder:
    def __init__(self):
        self.count = 0
        self.to = time()
    
    def handler(self, pin):
        if RotB.value() == 0:
            self.count += 1
        
        else:
          self.count -= 1
    def button_pressed(self, pin):
        t1 = time()
        if abs(t1 - self.to) > 1.0:
            print("knob pushed")
            self.to = t1
    
          
    def get_value(self):
        return self.count
rot = rotary_encoder()

      

RotA.irq(handler = rot.handler, trigger = Pin.IRQ_RISING)
Rot_Push.irq(handler = rot.button_pressed, trigger = Pin.IRQ_FALLING)

while True:
    v = rot.get_value()
    print(v)
    
    sleep_ms(100)