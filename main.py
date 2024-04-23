import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# Setup pins
microphone = AnalogIn(board.IO1)

led_pins = [
    board.IO21,
    board.IO26,
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

while True:
    volume = microphone.value

    max_volume = 55000 
    min_volume = 20000 #set the minimum threshold to account for background noise

    num_leds = len(leds)
    volume_range = max_volume - min_volume

    segment_size = volume_range // num_leds 
    adjusted_volume = max(0, volume - min_volume)  # Adjust volume based on minimum threshold
    
    active_leds = min(adjusted_volume // segment_size, num_leds - 1)

    for i in range(num_leds):     # Turn on LEDs
        leds[i].value = i <= active_leds

    sleep(0.1)  

    #In the video submission, I moved the VU meter around because it seems to pick up sound from the side and the bottom 
    #a bit better than the top of the microphone