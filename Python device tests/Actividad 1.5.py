import time
import datatest

Num1 = datatest.getNumber()

Operation = 0

while(Operation not in ["1","2","3","4"]):
    print()
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    Operation = input("Ingrese opcion:  ")
    if(Operation not in ["1","2","3","4"]):
        print("Operacion no valida")
    
Num2 = datatest.getNumber()

datatest.GoHome()

datatest.d.swipe(540,1500,540,500,25)

datatest.SafeClick(datatest.d(text=datatest.buttons[0]))

datatest.SafeClick(datatest.d(text=datatest.buttons[1]))
    
datatest.ClickNumber(Num1)
    
datatest.SafeClick(datatest.d(text=["+","−","×","÷"][int(Operation)-1]))

datatest.ClickNumber(Num2)

datatest.SafeClick(datatest.d(text="="))