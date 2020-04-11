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

Number = input("Introduzca numero a marcar --> ")

GoHome()

#print(d.click(204,1743))
SafeClick(d(description="Teléfono"))
time.sleep(1)

#Click Ajustes
SafeClick(d(text="Teclado"))
time.sleep(1)

d.long_click(755,1542)
time.sleep(1)

for i in Number:
    SafeClick(d(description=i))

#Click Perfil Fuera de Linea
SafeClick(d(descriptionContains="Llamar"))
#time.sleep(1)

#Click Desactivado
GoHome()    