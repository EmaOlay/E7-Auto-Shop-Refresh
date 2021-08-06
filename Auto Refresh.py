# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:03 2020

@author: Usuario
"""


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590
#number of visual inspections done on screen
contador=0
#number of coven bought
cont_coven=0
#number of mystic bought
cont_mystic=0
#number of refresh done
cont_refresh=0


while keyboard.is_pressed('q') == False:
    
    RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
#The confidence is added due to little variations in the background
    Coven_pos=pyautogui.locateOnScreen('covenant.PNG',confidence=0.90)
    Mystic_pos=pyautogui.locateOnScreen('mystic.PNG',confidence=0.90)
#Checks for covenant
    if (Coven_pos) != None:
        Coven_pos=pyautogui.locateOnScreen('covenant.PNG',confidence=0.90)
        print("Buy Covenant Summons.")
        contador=0
        Coven_point=pyautogui.center(Coven_pos)
        
        #print("La pos en x seria...",Coven_point[0],"\nLa pos en y seria...", Coven_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Coven_point[0]+800, Coven_point[1]+50)
        click(Coven_point[0]+800, Coven_point[1]+50)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        cont_coven+=1
        print("Covenant Summons bought=",cont_coven)
    else:
        time.sleep(0.05)
        #print("No Covenant summons to buy.")
        #print(contador)
        

#checks for mystic
    if (Mystic_pos) != None:
        Mystic_pos=pyautogui.locateOnScreen('mystic.PNG',confidence=0.90)
        print("Buy Mystic Summons.")
        contador=0
        Mystic_point=pyautogui.center(Mystic_pos)
        #print("x=",Mystic_point[0],"y=",Mystic_point[1])
        #print("La pos en x seria...",Mystic_point[0],"\nLa pos en y seria...", Mystic_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Mystic_point[0]+800, Mystic_point[1]+0)
        click(Mystic_point[0]+800, Mystic_point[1]+0)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        cont_mystic+=1
        print("Covenant Summons bought=",cont_mystic)
    else:
        #print("No Mystic summons to buy.")
        click(x=1263,y=590)
        pyautogui.scroll(-5, x=1263, y=590)
        contador = contador + 1
        #print(contador)
        #time.sleep(0.5)
        
#Double check in case of lag
    if contador==2 :
        pyautogui.scroll(5, x=1263, y=590)
        time.sleep(0.5)
#Finally refreshes
    if contador>2 :
        time.sleep(0.5)
        RB_point=pyautogui.center(RB_pos)
        click(RB_point[0], RB_point[1])
        click(RB_point[0], RB_point[1])
        time.sleep(0.5)#wait for confirm to appear
        Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG')
        Confirm_point=pyautogui.center(Confirm_pos)
        click(Confirm_point[0], Confirm_point[1])
        click(Confirm_point[0], Confirm_point[1])
        contador=0
        time.sleep(0.5)
        cont_refresh+=1
        print("Refresh Done=",cont_refresh)
        