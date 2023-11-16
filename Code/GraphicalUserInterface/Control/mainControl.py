## Este programa se encarga de enviar los datos de los botones y joysticks a la computadora
# Se debe ejecutar en Thonny IDE

import network
import utime
import socket
from machine import Pin, ADC

# Defensor ------------------------------------
buttonWhiteDef = Pin(2, Pin.IN, Pin.PULL_DOWN)
buttonBlackDef = Pin(3, Pin.IN, Pin.PULL_DOWN)
buttonBlueDef = Pin(4, Pin.IN, Pin.PULL_DOWN)
buttonGreenDef = Pin(5, Pin.IN, Pin.PULL_DOWN)
buttonRedDef = Pin(6, Pin.IN, Pin.PULL_DOWN)

# - Botón de Rotación - Defensor
button_routeLeft_Def = Pin(1, Pin.IN, Pin.PULL_DOWN)
button_routeRight_Def = Pin(0, Pin.IN, Pin.PULL_DOWN)

# Joystick - Defensor
xAxisDef = ADC(Pin(26))
yAxisDef = ADC(Pin(27))
buttonDef = Pin(22, Pin.IN, Pin.PULL_UP)

# Atacante ------------------------------------
buttonWhiteAtk = Pin(9, Pin.IN, Pin.PULL_DOWN)
buttonBlackAtk = Pin(10, Pin.IN, Pin.PULL_DOWN)
buttonBlueAtk = Pin(11, Pin.IN, Pin.PULL_DOWN)
buttonGreenAtk = Pin(12, Pin.IN, Pin.PULL_DOWN)
buttonRedAtk = Pin(13, Pin.IN, Pin.PULL_DOWN)

# - Botón de Rotación - Atacante
button_routeLeft_Atk = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_routeRight_Atk = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Joystick - Atacante
yAxisAtk = ADC(Pin(28))
xAxisAtk = Pin(21, Pin.IN)
buttonAtk = Pin(20, Pin.IN, Pin.PULL_UP)

led = Pin("LED", Pin.OUT)

# Configuración de la red Wi-Fi
ssid_wifi = 'Sansung A-32'  #'JM.Loría'
password_wifi = 'Mascotas#2020' #'bdfd0591'

wifi = network.WLAN(network.STA_IF)

# Conéctate a la red Wi-Fi
wifi.active(True)
wifi.connect(ssid_wifi, password_wifi)

# Espera a que se conecte
while not wifi.isconnected():
    print("Conectando a la red Wi-Fi...")
    utime.sleep(1)

print("Conexión Wi-Fi exitosa")
print(wifi.ifconfig())

# Dirección IP y puerto de la computadora
server_address = ('192.168.100.17', 12345)  # Cambia esto con la IP de tu computadora

# Configuración del socket para enviar datos a la computadora
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bucle principal
attackerCounter  = 0
defensorCounter = 0
while True:
    # DEFENSOR ---------------------------------------------
    defensor_buttons = [buttonWhiteDef, buttonBlackDef, buttonBlueDef, buttonGreenDef, buttonRedDef,
                        button_routeLeft_Def, button_routeRight_Def]
    attackerCounter  = 0;
    defensorCounter = 0;
    for button in defensor_buttons:
        if button.value() == 1:
            message = f"D{defensorCounter}"
            sock.sendto(message.encode(), server_address)
            print(f'Enviando mensaje: {message}')
            utime.sleep(0.1)
        defensorCounter+=1; 
    
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
        message = f"DL"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    if xValueDef >= 60000:
        xStatusDef = "right"
        message = f"DR"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    if yValueDef <= 600:
        yStatusDef = "up"
        message = f"DU"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    if yValueDef >= 60000:
        yStatusDef = "down"
        message = f"DD"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    # ATACANTE ---------------------------------------------
    atacante_buttons = [buttonWhiteAtk, buttonBlackAtk, buttonBlueAtk, buttonGreenAtk, buttonRedAtk,
                        button_routeLeft_Atk, button_routeRight_Atk]
    for button in atacante_buttons:
        if button.value() == 1:
            message = f"A{attackerCounter}"
            sock.sendto(message.encode(), server_address)
            print(f'Enviando mensaje: {message}')
            utime.sleep(0.1)
        attackerCounter+=1 

    # JOYSTICK - Atacante ----------------------------------
    yValueAtk = yAxisAtk.read_u16()
    xValueAtk = xAxisAtk.value()
    buttonValueAtk = buttonAtk.value()
    xStatusAtk = "middle"
    yStatusAtk = "middle"
    buttonStatusAtk = "not pressed"

    if xValueAtk == 1 and buttonValueAtk == 1:
        xStatusAtk = "middle"
        #print("X: " + str(xStatusAtk) + ", Y: " + str(yStatusAtk) + " -- button value: " + str(buttonValueAtk) + " button status: " + buttonStatusAtk)
        #utime.sleep(0.1)

    if buttonValueAtk == 0:
        buttonStatusAtk = "pressed"
        xStatusAtk = "right"
        message = f"AR"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)
        
    if yValueAtk <= 600:
        yStatusAtk = "up"
        message = f"AU"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)
        
    if yValueAtk >= 60000:
        yStatusAtk = "down"
        message = f"AD"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    if xValueAtk == 0:
        xStatusAtk = "left"
        message = f"AL"
        sock.sendto(message.encode(), server_address)
        print(message)
        utime.sleep(0.1)

    # Pequeño retardo para evitar rebotes
    utime.sleep_ms(100)

