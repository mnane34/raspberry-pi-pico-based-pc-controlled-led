# PC Controlled Led


# Module Definition
from machine import Pin,UART
import utime


# Pin Definition
redLedPin = 19
yellowLedPin = 18
greenLedPin = 17
blueLedPin = 16


# Veriables Definition
logicHigh = 1
logicLow = 0
data = 0


# Configration Definition
redLed = Pin(redLedPin,mode=Pin.OUT,value=logicHigh) 
yellowLed = Pin(yellowLedPin,mode=Pin.OUT,value=logicHigh)
greenLed = Pin(greenLedPin,mode=Pin.OUT,value=logicHigh)
blueLed = Pin(blueLedPin,mode=Pin.OUT,value=logicHigh)

redLed.value(logicLow)
yellowLed.value(logicLow)
greenLed.value(logicLow)
blueLed.value(logicLow)

uartZero = UART(0,9600)


#İnfinity Loop Definition
while True:
        if(uartZero.any()>0):        
            data = int(uartZero.read(1))
            print(data)

        if data == 1:
            redLed.value(logicHigh)
        elif data == 2:
            redLed.value(logicLow)
        elif data == 3:
            yellowLed.value(logicHigh)
        elif data == 4:
            yellowLed.value(logicLow)
        elif data == 5:
            greenLed.value(logicHigh)
        elif data == 6:
            greenLed.value(logicLow)
        elif data == 7:
            blueLed.value(logicHigh)
        elif data == 8:
            blueLed.value(logicLow)
        else:
            redLed.value(logicLow)
            yellowLed.value(logicLow)
            greenLed.value(logicLow)
            blueLed.value(logicLow)
            
            