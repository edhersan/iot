#llamo modulos
from machine import Pin
from utime import sleep

#creamos objeto

led_rojo = Pin(5, Pin.OUT)

#creamos el ciclo

while True: 
  led_rojo.value(1)
  sleep(2)
  print("Off")
  led_rojo.value(0)
  sleep(2)
  print("On")
  