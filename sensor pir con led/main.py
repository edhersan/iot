from machine import Pin
import utime

sen1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(12,Pin.OUT)

while True:
    estado = sen1.value()
    print(estado)
    utime.sleep_ms(500)

    if estado == 1:
     print("otra cosa")
     led1.on()
     utime.sleep_ms(50)
     led1.off()
     utime.sleep_ms(50)
    
        