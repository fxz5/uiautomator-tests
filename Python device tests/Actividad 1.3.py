import time
import datatest

datatest.GoHome()

datatest.d.swipe(540,1500,540,500,25)

#Click Ajustes
datatest.SafeClick(datatest.d(text="Ajustes"))

#Click Conexiones
datatest.SafeClick(datatest.d(text="Conexiones"))
#time.sleep(1)

#Click Perfil Fuera de Linea
datatest.SafeClick(datatest.d(text="Perfil Fuera de línea"))
#time.sleep(1)

#Click para desactivar modo avion
datatest.SafeClick(datatest.d(text="Activado"))
datatest.GoHome()