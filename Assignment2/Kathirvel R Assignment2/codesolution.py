import datetime
import time
import random
import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BCM)      
GPIO.setwarning(false)     
BUZZER = 23                
buzzerstate = False 

dt = datetime.datetime.now()
GPIO.setup(BUZZER,GPIO.OUT)


while True:
	temp = random.randint(0, 100)
    	humidity = random.randint(0, 100)
    	buzzstate = not buzzstate                
    	GPIO.output(BUZZER,buzzstate)
    	if(temp>=55):
		print("temperature have crossed the threshold level on",dt.strftime("%d-%m-%y"),"at",dt.strftime("%H:%M"))
    	elif(humidity>=78):
        	print("humidity have crossed the threshold level on",dt.strftime("%d-%m-%y"),"at",dt.strftime("%H:%M"))
        time.sleep(20)
	
   
