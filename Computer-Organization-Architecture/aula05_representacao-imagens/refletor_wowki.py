from machine import Pin, SPI
import time

spi = SPI(
    1,
    baudrate=1000000,
    polarity=0,
    phase=0,
    sck=Pin(10),
    mosi=Pin(11)
)

cs = Pin(9, Pin.OUT)
cs.value(1)

def enviar(registro, valor):

    cs.value(0)

    spi.write(bytes([registro, valor]))

    cs.value(1)

enviar(0x0C, 0x01)

enviar(0x09, 0x00)

enviar(0x0B, 0x07)

enviar(0x0A, 0x08)


imagem = [
    0x18,
    0x3C,
    0x66,
    0x66,
    0x7E,
    0x66,
    0x66,
    0x00
]

for linha in range(8):

    enviar(linha + 1, imagem[linha])

while True:

    time.sleep(1)


