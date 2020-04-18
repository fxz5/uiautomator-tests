import time
from uiautomator import Device

buttons = []
buttons.append("Calculadora")
buttons.append("C")

d = Device()

def GoHome():
    while(d.press.home()):
        time.sleep(1)
    time.sleep(1)

def SafeClick(button):
    if(button.count != 0):
        button.click()
    time.sleep(1)

def SafeLongClick(button):
    if(button.count != 0):
        button.long_click()
    time.sleep(1)

def ClickNumber(Num):
    if(Num[0] == "-"):
        SafeClick(d(text="( )"))
        SafeClick(d(text="−"))
        
        for i in Num[1:]:
            if(i == "."):
                SafeClick(d(text=i))
            else:
                SafeClick(d(description=i))
        
        SafeClick(d(text="( )"))        
    else:
        for i in Num:
            if(i == "."):
                SafeClick(d(text=i))
            else:
                SafeClick(d(description=i))
                
def ClickPhone(Phone):
    Phone = Phone.replace("+","0")
    for i in Phone:
        if(i == "*"):
            SafeClick(d(description = "Asterisco"))
        elif(i == "#"):
            SafeClick(d(description = "Numeral"))
        else:
            SafeClick(d(description=i))


def getNumber():
    n = input("Ingrese un numero:  ")
    
    while(not isfloat(n)):
        n = input("Ese numero no es valido\nIngrese un numero:  ")
    return n

def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def isfloat(value):
    a = value.split(".")
    if(len(a) > 2):
        return False
    for i in a:
        if not isint(i):
            return False
    return True

def getPhoneNumber():
    p = input("Ingrese numero a marcar:  ")
    
    while(not ValidPhoneNumber(p)):
        p = input("Ese numero telefonico no es valido\nIngrese numero a marcar:  ")
    return p

def ValidPhoneNumber(Phone):
    chars = ["1","2","3","4","5","6","7","8","9","0","+","#","*"]
    for i in Phone:
        if i not in chars:
            return False
    if(Phone == ""):
        return False
    return True