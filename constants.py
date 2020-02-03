import adafruit_ads1x15.ads1115 as ADS
import board

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

PM_LED_PIN = board.D25
PM_ADC_CHANNEL = ADS.D7

DHT_PIN = board.D18