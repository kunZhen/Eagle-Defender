from machine import Pin, ADC
import utime

# Defensor ------------------------------------
buttonWhiteDef = Pin(2, Pin.IN, Pin.PULL_DOWN)
buttonBlackDef = Pin(3, Pin.IN, Pin.PULL_DOWN)
buttonBlueDef = Pin(4, Pin.IN, Pin.PULL_DOWN)
buttonGreenDef = Pin(5, Pin.IN, Pin.PULL_DOWN)
buttonRedDef = Pin(6, Pin.IN, Pin.PULL_DOWN)

# - Boton de Rotacion - Defensor
button_routeLeft_Def = Pin(0, Pin.IN, Pin.PULL_DOWN)
button_routeRight_Def= Pin(1, Pin.IN, Pin.PULL_DOWN)

# Joystick - Defensor
xAxisDef = ADC(Pin(26))
yAxisDef = ADC(Pin(27))
buttonDef = Pin(22,Pin.IN, Pin.PULL_UP)

#Atacante ------------------------------------
buttonWhiteAtk = Pin(9, Pin.IN, Pin.PULL_DOWN)
buttonBlackAtk = Pin(10, Pin.IN, Pin.PULL_DOWN)
buttonBlueAtk = Pin(11, Pin.IN, Pin.PULL_DOWN)
buttonGreenAtk = Pin(12, Pin.IN, Pin.PULL_DOWN)
buttonRedAtk = Pin(13, Pin.IN, Pin.PULL_DOWN)

# - Boton de Rotacion - Atacante
button_routeLeft_Atk = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_routeRight_Atk = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Joystick - Atacante
xAxisAtk = ADC(Pin(28))
yAxisAtk = Pin(21,Pin.IN)
buttonAtk = Pin(20,Pin.IN, Pin.PULL_UP)


led = Pin("LED", Pin.OUT)

while True:

    # DEFENSOR ---------------------------------------------
    if buttonWhiteDef.value() == 1:
        print("Button White Defensor was pressed!")
        if led.value() == 1:
            led.off()
        else:  
            led.on()
        utime.sleep(0.2)
    
    if buttonBlackDef.value() == 1:
        print("Button Black Defensor was pressed!")
        utime.sleep(0.2)

    if buttonBlueDef.value() == 1:
        print("Button Blue Defensor was pressed!")
        utime.sleep(0.2)

    if buttonGreenDef.value() == 1:
        print("Button Green Defensor was pressed!")
        utime.sleep(0.2)

    if buttonRedDef.value() == 1:
        print("Button Red Defensor was pressed!")
        utime.sleep(0.2)

    if button_routeLeft_Def.value() == 1:
        print("Button Route Left Defensor was pressed!")
        utime.sleep(0.2)

    if button_routeRight_Def.value() == 1:
        print("Button Route Right Defensor was pressed!")
        utime.sleep(0.2)

    # JOYSTICK - Defensor ----------------------------------
    xValueDef = xAxisDef.read_u16()
    yValueDef = yAxisDef.read_u16()
    buttonValueDef = buttonDef.value()
    xStatusDef = "middle"
    yStatusDef = "middle"
    buttonStatusDef = "not pressed"

    if buttonValueDef == 0:
        buttonStatusDef = "pressed"
        print("X: " + str(xStatusDef) + ", Y: " + str(yStatusDef) + " -- button value: " + str(buttonValueDef) + " button status: " + buttonStatusDef)

    if xValueDef <= 600:
        xStatusDef = "left"
        print("X: " + str(xStatusDef) + ", Y: " + str(yStatusDef) + " -- button value: " + str(buttonValueDef) + " button status: " + buttonStatusDef)

    if xValueDef >= 60000:
        xStatusDef = "right"
        print("X: " + str(xStatusDef) + ", Y: " + str(yStatusDef) + " -- button value: " + str(buttonValueDef) + " button status: " + buttonStatusDef)


    if yValueDef <= 600:
        yStatusDef = "up"
        print("X: " + str(xStatusDef) + ", Y: " + str(yStatusDef) + " -- button value: " + str(buttonValueDef) + " button status: " + buttonStatusDef)


    if yValueDef >= 60000:
        yStatusDef = "down"
        print("X: " + str(xStatusDef) + ", Y: " + str(yStatusDef) + " -- button value: " + str(buttonValueDef) + " button status: " + buttonStatusDef)

    # ATACANTE ---------------------------------------------

    if buttonWhiteAtk.value() == 1:
        print("Button White Atacante was pressed!")
        utime.sleep(0.2)

    if buttonBlackAtk.value() == 1:
        print("Button Black Atacante was pressed!")
        utime.sleep(0.2)

    if buttonBlueAtk.value() == 1:
        print("Button Blue Atacante was pressed!")
        utime.sleep(0.2)

    if buttonGreenAtk.value() == 1:
        print("Button Green Atacante was pressed!")
        utime.sleep(0.2)

    if buttonRedAtk.value() == 1:
        print("Button Red Atacante was pressed!")
        utime.sleep(0.2)

    if button_routeLeft_Atk.value() == 1:
        print("Button Route Left Atacante was pressed!")
        utime.sleep(0.2)

    if button_routeRight_Atk.value() == 1:
        print("Button Route Right Atacante was pressed!")
        utime.sleep(0.2)

    # JOYSTICK - Atacante ----------------------------------
    xValueAtk = xAxisAtk.read_u16()
    yValueAtk = yAxisAtk.value()
    buttonValueAtk = buttonAtk.value()
    xStatusAtk = "middle"
    yStatusAtk = "middle"
    buttonStatusAtk = "not pressed"

    if yValueAtk == 1 and buttonValueAtk == 1:
        yStatusAtk = "middle"
        #print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        utime.sleep(0.2)

    if buttonValueAtk == 0:
        buttonStatusAtk = "pressed"
        yStatusAtk = "down"
        print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        utime.sleep(0.2)
        
    if xValueAtk <= 600:
        xStatusAtk = "left"
        print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        utime.sleep(0.2)
        
    if xValueAtk >= 60000:
        xStatusAtk = "right"
        print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        utime.sleep(0.2)

    if yValueAtk == 0:
        yStatusAtk = "up"
        print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        utime.sleep(0.2)

