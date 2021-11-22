# Setting up (installing modules and importing saved data).
# Importing modules. I haven't actually added any comments into any of my Python projects before now, so I guess this is a first lol.
import os
import time
import glob, os
import webbrowser
import random
with open('C:\ECCS\Directory.txt') as f:
    lines = f.read()
# Folder Path
path = (lines)
path = lines.rstrip('\n')
ECCSDatafile = ("ECCSData")
# Changing the directory
os.chdir(path)
# Importing name
namepath = ("Name.txt")
fullnamepath = (os.path.join(path, ECCSDatafile, namepath))
fileObject = open(fullnamepath, "r")
Name = fileObject.read()
# Importing DOB
DOBpath = ("DOB.txt")
fullDOBpath = (os.path.join(path, ECCSDatafile, DOBpath))
fileObject = open(fullDOBpath, "r")
DOB = fileObject.read()
# Importing favourite colour
FavColourpath = ("FavColour.txt")
fullFavColourpath = (os.path.join(path, ECCSDatafile, FavColourpath))
fileObject = open(fullFavColourpath, "r")
FavColour = fileObject.read()
# ECCS system ready
# Copyright information, etc.
print ("Samuel Matthews, 2021")
time.sleep (1)
print ("Enhanced ChatBot Communication System, Version 1.3")
time.sleep (1)
# Greeting of user
print ("Welcome back, " + Name + "!")
time.sleep (1)
print ("Just so you know, the ECCS is just a proof of concept at the moment. So, it's actual functionality is pretty limited.")
time.sleep (1)
# Commands (in loop)
print ("For a list of commands, type 'Help'.")
count = 0
while (count < 3):
        cmd = input ("Enter command here: ")
        if cmd == ("Help"):
                print ("1. Tell me my DOB")
                print ("Tells you what your date of birth is, even though you should probably already know it anyway.")
                time.sleep (1)
                print ("2. Tell me my fav. colour")
                print ("Tells you what your favourite colour is, even though you should probably already know that too.")
                time.sleep (1)
                print ("3. Tell me my name")
                print ("It tells you your name. Which you should definitely already know. Not just because it's your name, but because I literally said it only 5 seconds ago.")
                time.sleep (1)
                print ("5. Help")
                print ("It shows you every available command, including itself. You're using it right now.")
                time.sleep (1)
                print ("6. Quit")
                print ("It closes ChatBot. Pretty self explanatory, don't you think?")
                time.sleep (1)
                print ("7. Karlson")
                print ("What do you think it does?")
                time.sleep (1)
                print ("8. Thicc Karlson")
                print("RIP RAM")
                time.sleep (1)
                print ("9. Tell me a joke")
                print("It tells you a joke. Duh")
                time.sleep(1)
                print ("ECCS is case-sensitive, so commands must be typed in precisely as they are described in this menu.")
        if cmd == ("Tell me my DOB"):
                print ("Your date of birth is " + DOB + ". Shouldn't you know that though?")
        if cmd == ("Tell me my name"):
                print ("Your name is " + Name + ". You should definitely know that.")
        if cmd == ("Tell me my fav. colour"):
                print ("Your favourite colour is" + FavColour + ".")
        if cmd == ("Karlson"):
                print ("FYI, you're going to need to be online for this.")
                time.sleep (3)
                webbrowser.open("https://www.youtube.com/watch?v=GwomfPkMZO8")
        if cmd == ("Thicc Karlson"):
                print ("FYI, you're going to need to be online for this. Also, your PC is gonna hate you for this.")
                while True:
                   webbrowser.open("https://www.youtube.com/watch?v=GwomfPkMZO8")
                   time.sleep(1)
        if cmd == ("Tell me a joke"):
            jokerandom = random.randrange(0, 5)
            if jokerandom == (0):
                print ("Your life.")
            if jokerandom == (1):
                print ("Why did the chicken cross the road?")
                time.sleep(1)
                print ("To get away from you.")
            if jokerandom == (2):
                print ("I was going to make a joke about salt.")
                time.sleep(2)
                print ("But then I figured, Na, you wouldn't get it")
            if jokerandom == (3):
                while True:
                    webbrowser.open_new_tab("http://corndog.io/")
            if jokerandom == (4):
                while True:
                    webbrowser.open_new_tab("http://corndog.io/")
            if jokerandom == (5):
                while True:
                    webbrowser.open_new_tab("http://corndog.io/")
        if cmd == ("Quit"):
                quit()

