import pyautogui as auto

import time

loc = 100, 870
loc2= 500, 250
loc3= 500, 650
loc4= 300, 550
loc5= 700, 400
loc6= 900, 360

auto.moveTo(loc[0], loc[1], 1)yt
auto.click()
time.sleep(5)
auto.moveTo(loc2[0], loc2[1], 1)
auto.click()
time.sleep(3)
auto.moveTo(loc3[0], loc3[1], 1)
auto.click()
time.sleep(3)
auto.moveTo(loc4[0], loc4[1], 1)
auto.click(clicks=2)
time.sleep(3)
auto.moveTo(loc5[0], loc5[1], 1)
auto.click()
time.sleep(3)
auto.moveTo(loc6[0], loc6[1], 1)
auto.click()
auto.typewrite("Guleed's Supermarket")
time.sleep(2)