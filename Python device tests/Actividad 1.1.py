import os
Number = input("Introduzca numero a marcar --> ")
os.system("adb shell am start -a android.intent.action.CALL -d tel:" + str(Number))