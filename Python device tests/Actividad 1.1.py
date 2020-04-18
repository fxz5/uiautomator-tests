import os
import datatest
Number = datatest.getPhoneNumber()
os.system("adb shell am start -a android.intent.action.CALL -d tel:" + str(Number))