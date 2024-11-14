from gpiozero import LED
from time import sleep
red = LED(2) # 2 is the GPIO pin

while TRUE:
  red.on()
  sleep(1)
  red.off()
  sleep(1)
