
from machine import Pin  # Importa la clase Pin del módulo machine para controlar los pines del ESP32
import utime  # Importa el módulo utime para manejar las funciones de tiempo

# Configura el pin 15 como entrada con una resistencia de pull-down
sen1 = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Bucle infinito para leer el estado del pin continuamente
while True:
    # Lee el estado del pin 15
    estado = sen1.value()
    # Imprime el estado del pin (0 o 1)
    print(estado)
    # Pausa la ejecución durante 500 milisegundos
    utime.sleep_ms(500)

    # Si el estado del pin es 0, imprime "algo"
    if estado == 0:
        print("algo")
    else:
        # Si el estado del pin es 1, imprime "otra cosa"
        print("otra cosa")
