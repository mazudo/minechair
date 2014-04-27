#!/usr/bin/python

import time
import RPi.GPIO as GPIO

class LedLib:

    # LED active states
    LED_ENABLE = 0 # Cathode set to low.  Current will flow.
    LED_DISABLE = 1 # Cathode set to high.  Current won't flow.
    RGB_ENABLE = 1
    RGB_DISABLE = 0

    # LED GPIO ports
    LED1 = 12
    LED2 = 16
    LED3 = 18
    LED4 = 22
    LED5 = 7
    LED = [LED1,LED2,LED3,LED4,LED5]
    # RGB GPIO ports
    RGB_RED = 11
    RGB_GREEN = 13
    RGB_BLUE = 15
    RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]
    # Colors
    BLUE = 1  #001
    GREEN = 2 #010
    CYAN = 3  #011
    RED = 4   #100
    MAGENTA = 5 #101
    YELLOW = 6  #110
    WHITE = 7   #111
    COLOR = [BLUE,GREEN,CYAN,RED,MAGENTA,YELLOW,WHITE]

    # Setup the LED GPIO
    def led_setup(self):
        # setup the wiring
        GPIO.setmode(GPIO.BOARD)
        # setup ports
        for led_val in LedLib.LED:
            GPIO.setup(led_val, GPIO.OUT)
        for rgb_val in LedLib.RGB:
            GPIO.setup(rgb_val, GPIO.OUT)

    # Activate LED
    def led_activate(self,led,color):
        # turn on RGB port
        if (color & LedLib.BLUE):
            GPIO.output(LedLib.RGB_BLUE,LedLib.RGB_ENABLE)
        if (color & LedLib.GREEN):
            GPIO.output(LedLib.RGB_GREEN,LedLib.RGB_ENABLE)
        if (color & LedLib.RED):
            GPIO.output(LedLib.RGB_RED,LedLib.RGB_ENABLE)
        # turn on cathode port
        GPIO.output(led,LedLib.LED_ENABLE)

    # activate all leds
    def led_activate_all(self,color):
        for led_val in LedLib.LED:
            self.led_activate(led_val,color)

    def led_activate_rainbow(self):
        '''
        for i in range(0,200):
            led_activate(LED1,BLUE)
            time.sleep(0.005)
            led_deactivate(LED1,BLUE)
            led_activate(LED2,GREEN)
            time.sleep(0.005)
            led_deactivate(LED2,GREEN)
            led_activate(LED3,RED)
            time.sleep(0.005)
            led_deactivate(LED3,RED)
            led_activate(LED4,YELLOW)
            time.sleep(0.005)
            led_deactivate(LED4,YELLOW)
            led_activate(LED5,WHITE)
            time.sleep(0.005)
            led_deactivate(LED5,WHITE)
        '''

    def led_deactivate(self,led,color):
        # turn off rgb port
        if (color & LedLib.BLUE):
            GPIO.output(LedLib.RGB_BLUE,LedLib.RGB_DISABLE)
        if (color & LedLib.GREEN):
            GPIO.output(LedLib.RGB_GREEN,LedLib.RGB_DISABLE)
        if (color & LedLib.RED):
            GPIO.output(LedLib.RGB_RED,LedLib.RGB_DISABLE)
        # turn off cathode port
        GPIO.output(led,LedLib.LED_DISABLE)

    # deactivate all leds
    def led_deactivate_all(self,color):
        for led_val in LedLib.LED:
            self.led_deactivate(led_val,color)


    def led_clear(self):
        for led_val in LedLib.LED:
            GPIO.output(led_val, LedLib.LED_DISABLE)
        for rgb_val in LedLib.RGB:
            GPIO.output(rgb_val, LedLib.RGB_DISABLE)

    def cleanup(self):
        GPIO.cleanup()


# main test function
def main():
    print "hello led library!"
    LEDLib = LedLib()
    LEDLib.led_setup()
    LEDLib.led_clear()

    for color_val in LEDLib.COLOR:
        LEDLib.led_activate_all(color_val)
        time.sleep(1)
        LEDLib.led_deactivate_all(color_val)

    LEDLib.led_clear()
#    LEDLib.led_activate_rainbow()
#    LEDLib.led_clear()
    GPIO.cleanup()

# call main function
# main()

