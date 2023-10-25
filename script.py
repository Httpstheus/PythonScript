
import pyautogui

import time

from datetime import datetime, timedelta


print(pyautogui.position()) 

pyautogui.moveTo(1915,1063)
pyautogui.click()

time.sleep(10)
# # Locale with coordenate the App 'Mundial.ink' 


pyautogui.moveTo(1836,25)
pyautogui.doubleClick()
time.sleep(15)

# Alter for login and password 

pyautogui.hotkey('tab')

time.sleep(3)

#  user login
pyautogui.write('')

time.sleep(3)

pyautogui.hotkey('tab')

time.sleep(2)

# password 
pyautogui.write('')

time.sleep(2)

pyautogui.hotkey('enter')

time.sleep(10)

pyautogui.hotkey('enter')

# Search and Click on '' 

time.sleep(4)

pyautogui.moveTo(500,39)

pyautogui.click()

time.sleep(2)

# here click on '' 

pyautogui.moveTo(516,95)

pyautogui.click()

time.sleep(3)
 

print(pyautogui.position())

pyautogui.moveTo(372,111)

pyautogui.click()

pyautogui.write('101')

pyautogui.moveTo(263,152)

time.sleep(3)

pyautogui.doubleClick()

# Obtem a data de ontem no formato "dd.mm.yyyy"
data_ontem = (datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y')  

print(pyautogui.position())

pyautogui.moveTo(322,116)

time.sleep(1)

pyautogui.click()

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')

pyautogui.write('01102023')

time.sleep(2)

pyautogui.moveTo(322,137)
time.sleep(2)

pyautogui.click()

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left') 

pyautogui.write(data_ontem)

print(pyautogui.position())

pyautogui.moveTo(293,178)
pyautogui.click()

time.sleep(3)

print(pyautogui.position())

pyautogui.moveTo(45,984)

time.sleep(2)
pyautogui.click() 

time.sleep(4)

print(pyautogui.position())

pyautogui.moveTo(30,140)

time.sleep(4)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(64,973)

time.sleep(4)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(838,779)

time.sleep(2)

pyautogui.click()

time.sleep(45)

print(pyautogui.position())

pyautogui.moveTo(709,445)

time.sleep(2)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(863,639)

time.sleep(2)

pyautogui.doubleClick()

print(pyautogui.position())
 
pyautogui.moveTo(1026,456) 

time.sleep(2)

pyautogui.doubleClick()

print(pyautogui.position())

pyautogui.moveTo(999,509) 

time.sleep(2)

pyautogui.doubleClick()

print(pyautogui.position())

pyautogui.moveTo(1026,456)

time.sleep(2)

pyautogui.doubleClick()

time.sleep(10)    

pyautogui.hotkey('esc')

time.sleep(10)  

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(1)
pyautogui.click()

time.sleep(3)

print(pyautogui.position())

pyautogui.moveTo(113,87)

time.sleep(3)
pyautogui.click()

pyautogui.moveTo(372,111)

pyautogui.doubleClick()

time.sleep(2)

pyautogui.write('615')

print(pyautogui.position())

pyautogui.moveTo(51,975)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(317,115)

time.sleep(3)

pyautogui.click()

time.sleep(1)

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')

pyautogui.write('01102023')

# time.sleep(2)

print(pyautogui.position())

pyautogui.moveTo(317,156)
time.sleep(2)

pyautogui.click()

time.sleep(2)

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left') 

pyautogui.write(data_ontem)

print(pyautogui.position())

pyautogui.moveTo(641,207)
time.sleep(2)

pyautogui.click()
time.sleep(2)

pyautogui.moveTo(351,238)
time.sleep(2)

pyautogui.click()

print(pyautogui.position())
pyautogui.moveTo(67,979)
time.sleep(2)

pyautogui.click()
time.sleep(2)

print(pyautogui.position())
pyautogui.moveTo(37,139)
time.sleep(2)

pyautogui.click()
time.sleep(2)

print(pyautogui.position())
pyautogui.moveTo(61,972)
time.sleep(2)

pyautogui.click()
time.sleep(2)

print(pyautogui.position())
pyautogui.moveTo(828,784)
time.sleep(2)

pyautogui.click()
time.sleep(45)

print(pyautogui.position())
pyautogui.moveTo(709,450)
time.sleep(2)

pyautogui.click()
time.sleep(3)

print(pyautogui.position())
pyautogui.moveTo(878,630)
time.sleep(2)

pyautogui.doubleClick()
time.sleep(2)

print(pyautogui.position())
pyautogui.moveTo(924,456)
time.sleep(2)

pyautogui.doubleClick()
time.sleep(3)

print(pyautogui.position())
pyautogui.moveTo(995,474)
time.sleep(2)

pyautogui.doubleClick()
time.sleep(3)

print(pyautogui.position())
pyautogui.moveTo(924,456)
time.sleep(2)

pyautogui.doubleClick()
time.sleep(3)

pyautogui.hotkey('esc')

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(1)
pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(113,87)

time.sleep(1)
pyautogui.click()

pyautogui.moveTo(372,111)

pyautogui.doubleClick()

time.sleep(2)

pyautogui.write('618')

print(pyautogui.position())

pyautogui.moveTo(51,975)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(298,113)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(325,140)

time.sleep(3)

pyautogui.click()

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')

pyautogui.write('01102023')

# time.sleep(2)

print(pyautogui.position())

pyautogui.moveTo(326,160)
time.sleep(2)

pyautogui.click()

time.sleep(2)

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left') 

pyautogui.write(data_ontem)

print(pyautogui.position())

pyautogui.moveTo(51,977)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(35,138)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(57,972)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(840,784) 

time.sleep(3)

pyautogui.click()

time.sleep(40)

print(pyautogui.position())
pyautogui.moveTo(709,450)
time.sleep(2)

pyautogui.click()
time.sleep(3)

print(pyautogui.position())
pyautogui.moveTo(878,630)
time.sleep(2)

pyautogui.doubleClick()
time.sleep(2)

print(pyautogui.position())
pyautogui.moveTo(924,456)
time.sleep(2)

pyautogui.doubleClick()


print(pyautogui.position())
pyautogui.moveTo(892,552)
time.sleep(2)

pyautogui.doubleClick()

print(pyautogui.position())
pyautogui.moveTo(924,456)
time.sleep(2)

pyautogui.doubleClick()

time.sleep(3)

pyautogui.hotkey('esc')

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(3)
pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(113,87)

time.sleep(1)
pyautogui.click()

pyautogui.moveTo(372,111)

pyautogui.doubleClick()

time.sleep(2)

pyautogui.write('693')

print(pyautogui.position())

pyautogui.moveTo(51,975)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(321,114)

time.sleep(3)

pyautogui.click()

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')

pyautogui.write('01102023')

time.sleep(2)

print(pyautogui.position())

pyautogui.moveTo(324,139)
time.sleep(2)

pyautogui.click()

time.sleep(2)

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left') 

pyautogui.write(data_ontem)

print(pyautogui.position())

pyautogui.moveTo(51,977)

time.sleep(3)

pyautogui.click()

print(pyautogui.position()) 

pyautogui.moveTo(33,140)

time.sleep(10)

pyautogui.click()

print(pyautogui.position()) 

pyautogui.moveTo(70,980) 

time.sleep(3)

pyautogui.click()

print(pyautogui.position())  

pyautogui.moveTo(835,801) 

time.sleep(3)

pyautogui.click()

time.sleep(80)

print(pyautogui.position())  

pyautogui.moveTo(736,426) 

time.sleep(3)

pyautogui.click()

time.sleep(2)

pyautogui.moveTo(842,640)

time.sleep(2)

pyautogui.doubleClick()


pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()

pyautogui.moveTo(945,572)

time.sleep(2)

pyautogui.doubleClick()

pyautogui.moveTo(913,455)

time.sleep(2)

pyautogui.doubleClick()


time.sleep(3)

pyautogui.hotkey('esc')

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(2)
pyautogui.click()


pyautogui.moveTo(113,87)

time.sleep(1)
pyautogui.click()

pyautogui.moveTo(372,111)

pyautogui.doubleClick()

time.sleep(2)

pyautogui.write('702')

print(pyautogui.position())

pyautogui.moveTo(51,975)

time.sleep(3)

pyautogui.click()

print(pyautogui.position()) 

pyautogui.moveTo(333,112)

time.sleep(3)

pyautogui.click()

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')

pyautogui.write('01102023')

time.sleep(2)

print(pyautogui.position())

pyautogui.moveTo(329,137)
time.sleep(2)

pyautogui.click()

time.sleep(2)

pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left')
pyautogui.hotkey('ctrl','shift','left') 

pyautogui.write(data_ontem)

print(pyautogui.position())

pyautogui.moveTo(51,977)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(33,133)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(40,985)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(842,794)

time.sleep(3)

pyautogui.click()

time.sleep(120)

print(pyautogui.position())  

pyautogui.moveTo(736,426) 

time.sleep(3)

pyautogui.click()

time.sleep(2)

pyautogui.moveTo(842,640)

time.sleep(2)

pyautogui.doubleClick()


pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()

pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()

pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()


time.sleep(3)

pyautogui.hotkey('esc')

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(2)
pyautogui.click()


pyautogui.moveTo(113,87)

time.sleep(1)
pyautogui.click()

pyautogui.moveTo(372,111)

pyautogui.doubleClick()

time.sleep(2)

pyautogui.write('59')

print(pyautogui.position())

pyautogui.moveTo(51,975)

time.sleep(3)

pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(303,116)

time.sleep(3)

pyautogui.click()


print(pyautogui.position())

pyautogui.moveTo(313,172)

time.sleep(3)

pyautogui.click()

pyautogui.moveTo(313,137)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(293,157)

time.sleep(3)

pyautogui.click()

pyautogui.moveTo(272,159)

time.sleep(3)

pyautogui.click()

pyautogui.moveTo(272,176)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(36,979)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(35,137)

time.sleep(10)

pyautogui.click() 

print(pyautogui.position())

pyautogui.moveTo(47,977)

time.sleep(3)

pyautogui.click()


pyautogui.moveTo(805,792)

time.sleep(3)

pyautogui.click()

time.sleep(40)


print(pyautogui.position())  

pyautogui.moveTo(736,426) 

time.sleep(3)

pyautogui.click()

time.sleep(2)

pyautogui.moveTo(842,640)

time.sleep(2)

pyautogui.doubleClick()


pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()

print(pyautogui.position())  

pyautogui.moveTo(937,529)

time.sleep(2)

pyautogui.doubleClick()

pyautogui.moveTo(921,458)

time.sleep(2)

pyautogui.doubleClick()

time.sleep(3)

pyautogui.hotkey('esc')

print(pyautogui.position())

pyautogui.moveTo(1325,781)

time.sleep(2)
pyautogui.click()

print(pyautogui.position())

pyautogui.moveTo(1856,61)

time.sleep(2)
pyautogui.click()
