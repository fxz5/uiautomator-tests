from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz

def GoHome():
    while(d.press.home()):
        time.sleep(1)
    time.sleep(1)

def SafeClick(button):
    if(button.count != 0):
        button.click()
        time.sleep(1)

d = Device()

GoHome()

print(d.swipe(540,1500,540,500,25))
time.sleep(1)

#Click Ajustes
SafeClick(d(text="Ajustes"))
time.sleep(1)

#Click Conexiones
SafeClick(d(text="Conexiones"))
#time.sleep(1)

#Click Perfil Fuera de Linea
SafeClick(d(text="Perfil Fuera de línea"))
#time.sleep(1)

#Click Desactivado
SafeClick(d(text="Desactivado"))
GoHome()