# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:03 2020

@author: Ema
"""


from pyautogui import *
import pyautogui
import time
import keyboard
###might use it later so that it clicks slightly off everytime
#import random 



#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590
########
#%%Fail-Safes
##After each pyautogui instruction waits for 0.25 seconds
pyautogui.PAUSE = 0.3
##If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True
#%%Set-up
##Get screen res
pantalla=pyautogui.size()
##Move to center of the screen instantly
pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
#number of visual inspections done on screen
contador=0
#number of coven bought
cont_coven=0
#number of mystic bought
cont_mystic=0
#number of refresh done
cont_refresh=0

#%%
while keyboard.is_pressed('q') == False:
    time.sleep(0.2)
#Search for the refresh button
    RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
#The confidence is added due to little variations in the background
#Search for the price and quantity image of covenant summon
    Coven_pos=pyautogui.locateOnScreen('new_coven.PNG',confidence=0.98)
#Search for the price and quantity image of mystic summon
    Mystic_pos=pyautogui.locateOnScreen('mystic1.PNG',confidence=0.90)
#Checks for covenant
    if (Coven_pos) != None:
        print("Buy Covenant Summons.")
        contador=0
        Coven_point=pyautogui.center(Coven_pos)
        #print("La pos en x seria...",Coven_point[0],"\nLa pos en y seria...", Coven_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        pyautogui.click(x=Coven_point[0], y=Coven_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        cont_coven+=1
        
    else:
        time.sleep(0.05)
        #print("No Covenant summons to buy.")
        

#checks for mystic
    if (Mystic_pos) != None:
        print("Buy Mystic Summons.")
        contador=0
        Mystic_point=pyautogui.center(Mystic_pos)
        #print("x=",Mystic_point[0],"y=",Mystic_point[1])
        #print("La pos en x seria...",Mystic_point[0],"\nLa pos en y seria...", Mystic_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        pyautogui.click(x=Mystic_pos[0]+800, y=Mystic_pos[1]+100, clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        cont_mystic+=1
        
    else:
        #print("No Mystic summons to buy.")
        pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
        #Drag upward 300 pixels in 0.2 seconds
        pyautogui.dragTo(pantalla[0]/2, pantalla[1]/2-300, duration=0.2)
        time.sleep(0.1)
        contador = contador + 1
        
#Double check in case of lag don't enable unless you're lagging
    # if contador==2 :
    #     pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
    #     #Drag upward 300 pixels in 0.2 seconds
    #     pyautogui.dragTo(pantalla[0]/2, pantalla[1]/2-300, duration=0.2)
    #     time.sleep(0.5)
#Finally refreshes
    if contador>=2 :
        time.sleep(0.5)
        RB_point=pyautogui.center(RB_pos)
        pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm to appear
        Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG')
        Confirm_point=pyautogui.center(Confirm_pos)
        pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
        contador=0
        time.sleep(0.5)
        cont_refresh+=1
        print("Covenant Summons bought=",cont_coven)
        print("Mystic Summons bought=",cont_mystic)
        print("Refresh Done=",cont_refresh)
#%%Outside of the while loop
print("You exited successfuly")