#llamo modulos
from machine import Pin
from utime import sleep

#creamos objetos

led_rojo = Pin(4, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_verde = Pin(15, Pin.OUT)

#creamos el ciclo

while True: 
  led_rojo.value(1)
  sleep(3)
  print("rojo")
  led_amarillo.value(1)
  sleep(2)
  led_rojo.value(0)
  led_amarillo.value(0)
  print("amarillo")
  led_verde.value(1)
  sleep(5)
  print("verde")
  led_verde.value(0)
 