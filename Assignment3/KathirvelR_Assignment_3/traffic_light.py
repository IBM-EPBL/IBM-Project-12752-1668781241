 #Raspberry Pi Program for Traffic Light.

from gpiozero import Buzzer from gpiozero import Button
from gpiozero import LED
from time import sleep
button = Button (21) buzzer = Buzzer (15)
redled = LED(25)
yellowled = LED(8) greenled = LED(7)
while True:
      if button.is_pressed:
         redled.on()
          buzzer.on()
          sleep(2)
          redled.off()
          buzzer.off()
          yellowled.on()
          sleep(2)
          yellowled.off()
          greenled.on()
          sleep(2)	
          greenled.off() 
          break
