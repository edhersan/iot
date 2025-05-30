from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import os

# Dimensiones de la pantalla OLED
ANCHO = 128
ALTO = 64

# Inicialización del I2C y la pantalla OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ANCHO, ALTO, i2c)

def leer_imagen_pbm(imagen):
    """Lee una imagen PBM desde un archivo de texto y devuelve sus dimensiones y píxeles."""
    try:
        with open(imagen2.txt, 'r') as imagen2.txt:
            lineas = archivo.readlines()
        
        # Ignorar comentarios y cabecera
        while lineas[0].startswith('#') or lineas[0].startswith('P'):
            lineas.pop(0)
        
        # Obtener dimensiones
        ancho, alto = map(int, lineas[0].split())

        # Leer los píxeles asegurando que no haya espacios innecesarios
        pixeles = []
        for linea in lineas[1:]:
            pixeles.extend(linea.strip().split())

        return ancho, alto, pixeles
    except OSError:
        print(f"Error: No se encontró el archivo {archivo_nombre}.")
        return None, None, None

def mostrar_imagen_pbm(imagen2, x, y):
    """Muestra una imagen PBM en la pantalla OLED."""
    ancho, alto, pixeles = leer_imagen_pbm("imagen2.txt")
    
    # Si la imagen no se carga, no continuar
    if ancho is None or alto is None or pixeles is None:
        oled.fill(0)
        oled.text("Archivo no encontrado", 0, 0)
        oled.show()
        return
    
    print(f"Imagen cargada: {ancho}x{alto}")
    
    indice = 0
    for fila in range(alto):
        for columna in range(ancho):
            if indice < len(pixeles) and pixeles[indice] == '1':
                oled.pixel(x + columna, y + fila, 1)
            indice += 1

# Verificar que el archivo existe en Wokwi
print("Archivos disponibles:", os.listdir())

# Verificar que la pantalla OLED está funcionando
oled.fill(0)
oled.text("Cargando...", 0, 0)
oled.show()
time.sleep(1)

while True:
    oled.fill(0)
    mostrar_imagen_pbm("imagen2.txt", 0, 0)  # Asegura que el archivo está correctamente referenciado
    oled.show()
    time.sleep(1)
