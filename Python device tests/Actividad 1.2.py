import time
from uiautomator import Device
import datatest

Number = datatest.getPhoneNumber()

datatest.GoHome()

#print(d.click(204,1743))
datatest.SafeClick(datatest.d(description="Teléfono"))

#Click Ajustes
datatest.SafeClick(datatest.d(text="Teclado"))

datatest.SafeLongClick(datatest.d(description="Botón Eliminar último dígito"))

datatest.ClickPhone(Number)

#Click Perfil Fuera de Linea
#SafeClick(d(descriptionContains="Llamar"))
#time.sleep(1)

#Click Desactivado
#datatest.GoHome()