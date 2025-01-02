import random
import time
from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import Color

LED_COUNT      = 400      # Количество светодиодов в ленте
LED_PIN        = 18      # GPIO пин, к которому вы подсоединяете светодиодную ленту
LED_FREQ_HZ    = 800000  # Частота несущего сигнала (обычно 800 кГц)
LED_DMA        = 10      # DMA-канал для генерации сигнала (обычно 10)
# LED_BRIGHTNESS = 255     # Яркость: 0 - наименьшая, 255 - наибольшая
LED_INVERT     = False   # True для инвертирования сигнала (для подключения через NPN транзистор)
LED_CHANNEL    = 0       # '1' для GPIO 13, 19, 41, 45 или 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

def snakeWithFade(strip, color, wait_ms=50, tail_length=10, br=255):
    for i in range(LED_COUNT+tail_length):
        strip.setBrightness(br)
        strip.setPixelColor(i, color)
        for j in range(i - tail_length, 0, -1):
            strip.setPixelColor(j, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms * 0.001)

def fullColor(strip, color, wait_ms=50, br=255):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)

    strip.setBrightness(br)
    strip.show()


def oddPixels(strip, color_odd, color_non_odd, wait_ms=50, br=255):
    for i in range(LED_COUNT):
        if i%2 == 0:
            strip.setPixelColor(i, color_odd)
        else:
            strip.setPixelColor(i, color_non_odd)
    strip.setBrightness(br)
    strip.show()
    time.sleep(wait_ms * 0.001)

def rand_number() -> int:
    random_number = random.randint(1, 256)
    print(random_number)
    return random_number


if __name__ == "__main__":
    try:
        data = int(input("Select module: "))
        if data == 1:
            fullColor(strip, Color(255, 0, 0), wait_ms=10, br=255)
            time.sleep(2)
            strip.setBrightness(0)
            time.sleep(1)
            for index, dat in enumerate(strip.getPixels()):
                if dat > 0:
                    strip.setPixelColor(index, Color(0, 0, 0))
            strip.show()
            print('Snake with fading animation.')
            bri = 5
    
            while bri != 255:
                snakeWithFade(strip, Color(rand_number(), rand_number(), rand_number()), wait_ms=0.01, tail_length=100, br=bri)
                time.sleep(0.1)
                bri += 10 # Зеленая змейка с хвостом
                
                print(f"BRI now: {bri}")
                if bri == 255:
                    print("all good")
                    break
        
        elif data == 2:
            print('Full color with changing brightness. Access: GOOD')
            fullColor(strip, Color(255, 0, 0), wait_ms=10, br=255)
            time.sleep(2)
            strip.setBrightness(0)
            time.sleep(1)
            for index, dat in enumerate(strip.getPixels()):
                if dat > 0:
                    strip.setPixelColor(index, Color(0, 0, 0))
            strip.show()
            while True:
                # fullColor(strip, Color(0, 0, 255), wait_ms=50, br=120)
                for bri in range(30, 120):
                    fullColor(strip, Color(0, 255, 0), wait_ms=10, br=bri)
                    time.sleep(0.1)
                for bri in range(120, 30, -1):
                    fullColor(strip, Color(0, 255, 0), wait_ms=10, br=bri)
                    time.sleep(0.1)
        elif data == 3:
            while True:
                time.sleep(0.7)
                clr = Color(rand_number(), rand_number(), rand_number())
                clr_two = Color(rand_number(), rand_number(), rand_number())
                print("---iteration down---")
                oddPixels(strip, clr, clr_two, wait_ms=10, br=255)

        else:
            print("Wrong number")
            while True:
                fullColor(strip, Color(0, 255, 0), wait_ms=10, br=255)
                time.sleep(5)
                raise KeyboardInterrupt
            
    except KeyboardInterrupt:
        strip.setBrightness(0)
        for index, dat in enumerate(strip.getPixels()):
            if dat > 0:
                strip.setPixelColor(index, Color(0, 0, 0))
                
        print(strip.getPixels())
        strip.show()
