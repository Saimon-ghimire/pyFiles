import pyautogui, time, subprocess


my_dict = {
      # put a key as per your wish for its corresponding PMI and password.
      # you will have to choose and input the key to join the class.
      'your key here':('PMI','Password'),
      'your key here':('PMI','Password'),
      'your key here':('PMI','Password')
}

key=input("Name: ") #input the key from the dictionary above
pin=my_dict[key][0]
passs=my_dict[key][1]
    


pyautogui.hotkey('win','d') #clears the screen
subprocess.call(["Zoom app location here"]) #opens the app
time.sleep(5)
pyautogui.click(750,420,duration=0.2) #the join button
pyautogui.typewrite(pin) #write PMI
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(passs) #write Password
pyautogui.press('enter') #and go

