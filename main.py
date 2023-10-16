import machine, ssd1306, os, utime, framebuf
import utils

# Conexión con OLED
i2c = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Conexion con el sensor de temperatura
sensor_temp = machine.ADC(4)
def get_temp():
    reading = sensor_temp.read_u16() * 3.3 / 65535
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature, float(temperature * 9/5 + 32)
i=0
while True:
    i=i+1
    # Obtener temperatura
    temp, temp_f = get_temp()
    # temp, temp_f = [i, i * 9/5 + 32 ] # <------ TEST
    # Display de la imagen
    oled.fill(0)
    utils.show_img(oled, utils.int32_to_bytes(utils.cold if temp < 15 else utils.hot if temp > 27 else utils.ok))
    oled.text("%.2f" % temp, 80, 17)
    oled.text("%.2f" % temp_f, 80, 42)
    oled.show()
    # Esperar un segundo
    utime.sleep_ms(100)
