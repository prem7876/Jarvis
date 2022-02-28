

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 145) 

engine.say("Hey Prem Its Been Long time  Im khushboo  i hope you Know me")
engine.runAndWait()