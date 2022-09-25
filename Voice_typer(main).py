from logging import exception
from multiprocessing import process
from multiprocessing.context import Process
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi#, loadUiType
import time
import multiprocessing
from ctypes import c_char_p
from PyQt5.uic.uiparser import WidgetStack
#import win32api
#import win32gui
import time
import pyperclip
import keyboard
from pyrebase.pyrebase import Database
import speech_recognition as sr
import pyautogui
import pyrebase
import subprocess
import os
#import struct
#import urllib2
import socket
#import AP
register_loaded = False
Logged_in = False

'''
directory = os.getcwd()
#print(directory)
version = struct.calcsize("P")*8

if version == 64:
    directory = directory + '\soundvolumeview-x64\SoundVolumeView.exe /Mute "Microphone"'
    print(directory)

if version == 32:
    directory = directory + '\soundvolumeview-x64\soundvolumeview\SoundVolumeView.exe /Mute "Microphone"'
'''
#User_interface = 0





def update_label():
    global status
    global Language_1
    global Language_2
    global User_interface
    global status_of_internet
    status2 = str(status)
    status2 = status2.replace("Value(<class 'ctypes.c_char_p'>,", "").replace("'","").replace(")","")
    User_interface.value = widget.currentIndex()
    '''
    time.sleep(1)
    print(str(widget.currentIndex()))
    time.sleep(1)
    try:
        print(widget.indexOf("Register"))
    except Exception as I:
        print(I)
    '''
    try:
        main.whatshesaid_2.setText("<font size=12 color='#4ac8eb'>"+ status2 +"</font>")
        Language_1.value = main.Language1.currentText()
        Language_2.value = main.Language2.currentText()
    except Exception:
        pass

    if status_of_internet.value == "connected":
        try:
            if User_interface.value == 0:
                main.internet.setHidden(True)
            if User_interface.value == 1:
                Login.internet.setHidden(True)
            if User_interface.value == 2:
                Register.internet.setHidden(True)
                pass
        except Exception:
            pass
    elif status_of_internet.value == "not":
        try:
            if User_interface.value == 0:
                main.internet.setVisible(True)
            if User_interface.value == 1:
                Login.internet.setVisible(True)
            if User_interface.value == 2:
                Register.internet.setVisible(True)
        except Exception:
            pass
    #print(str(widget.currentIndex()))None

def Update_the_app(status_of_internet,User_interface):
    time.sleep(8)
    if status_of_internet.value=="connected":
        file = open(r"C:\ProgramData\App_version.txt", 'r')
        current_version = file.read()
        file.close()
        print(current_version)
        database = Firebase.database()
        Server_Version = database.get()
        Server_version = str(Server_Version.val()).replace("OrderedDict", "").replace("(", "").replace(")" ,"").replace("[" ,"").replace("]" ,"").replace("'" ,"").replace("Beta" ,"").replace("," ,"").replace("Nope" ,"").replace(" " ,"").replace("Version","")
        print(Server_version)
        if current_version != Server_version:
            os.startfile('voice typer updaterr.bat')
            os.system("TASKKILL /F /IM Voice_typer(main).exe")


def Internet(status_of_internet,User_interface):
    #os.startfile('AP.exe')
    time.sleep(3)
    #User_interface = widget.currentIndex()
    while True:
        time.sleep(1)
        try:
            socket.create_connection(("1.1.1.1", 53))
            status_of_internet.value = "connected"
        except Exception:
            status_of_internet.value = "not"
        '''
        try:
            socket.create_connection(("1.1.1.1", 53))
            if User_interface.value == 0:
                main.internet.setHidden(True)
            if User_interface.value == 1:
                Login.internet.setHidden(True)
            if User_interface.value == 2:
                Register.internet.setHidden(True)
                pass
            

        except Exception:
            #User_interface = widget.currentIndex()
            try:
                if User_interface.value == 0:
                    main.internet.setVisible(True)
                if User_interface.value == 1:
                    print("duck")
                    Login.internet.setVisible(True)
                if User_interface.value == 2:
                    Register.internet.setVisible(True)

            except Exception:
                pass
        '''

def toreduce():
    if keyboard.is_pressed("ctrl + 1"):
        '''
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_UP = 26
        APPCOMMAND_MICROPHONE_VOLUME_DOWN = 25
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 24
        win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_MICROPHONE_VOLUME_MUTE * 0x10000)
        time.sleep(2)
        win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_MICROPHONE_VOLUME_UP * 0x10000)
        
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
        hwnd_active = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        '''
        subprocess.Popen('Muting.cmd')
        time.sleep(2)
        subprocess.Popen('Unmuting.cmd')
    else:
        pass
        #print('the code will be executed when it is muted')


def trying(status,Language_1,Language_2,User_interface):
    '''
    def typee():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-in')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng


    def typenh():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening"
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingh = r.recognize_google(audio, language='hi')
            print(f"user said: {typethingh}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingh


    def typep():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='pa')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng

    '''









    def typAfrikaansSouthAfrica():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='af-ZA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typAlbanianAlbania():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sq-AL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typAmharicEthiopia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='am-ET')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicAlgeria():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-DZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicBahrain():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-BH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicEgypt():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-EG')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicIraq():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-IQ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicIsrael():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-IL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicJordan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-JO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicKuwait():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-KW')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicLebanon():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-LB')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicMorocco():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-MA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicOman():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-OM')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicQatar():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-QA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicSaudiArabia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-SA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicStateofPalestine():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-PS')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicTunisia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-TN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicUnitedArabEmirates():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-AE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArabicYemen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ar-YE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typArmenianArmenia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='hy-AM')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typAzerbaijaniAzerbaijan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='az-AZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBasqueSpain():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='eu-ES')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBengaliBangladesh():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='bn-BD')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBengaliIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='bn-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBosnianBosniaandHerzegovina():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='bs-BA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBulgarianBulgaria():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='bg-BG')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typBurmeseMyanmar():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='my-MM')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typCatalanSpain():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ca-ES')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typChineseCantoneseTraditionalHongKong():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='yue-Hant-HK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng

    def typChineseMandarinSimplifiedChina():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='zh (cmn-Hans-CN)')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typChineseMandarinTraditionalTaiwan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='zh-TW (cmn-Hant-TW)')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng

    def typCroatianCroatia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='hr-HR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typCzechCzechRepublic():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='cs-CZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typDanishDenmark():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='da-DK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typDutchBelgium():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='nl-BE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typDutchNetherlands():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='nl-NL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishAustralia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-AU')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishCanada():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-CA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishGhana():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-GH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishHongKong():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-HK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishIreland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-IE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishKenya():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-KE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishNewZealand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-NZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishNigeria():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-NG')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishPakistan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-PK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishPhilippines():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-PH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishSingapore():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-SG')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishSouthAfrica():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-ZA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishTanzania():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-TZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishUnitedKingdom():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-GB')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEnglishUnitedStates():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='en-US')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typEstonianEstonia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='et-EE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFilipinoPhilippines():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fil-PH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFinnishFinland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fi-FI')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFrenchBelgium():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fr-BE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFrenchCanada():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fr-CA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFrenchFrance():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fr-FR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typFrenchSwitzerland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fr-CH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGalicianSpain():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='gl-ES')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGeorgianGeorgia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ka-GE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGermanAustria():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='de-AT')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGermanGermany():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='de-DE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGermanSwitzerland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='de-CH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGreekGreece():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='el-GR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typGujaratiIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='gu-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typHebrewIsrael():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='iw-IL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typHindiIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='hi-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typHungarianHungary():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='hu-HU')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typIcelandicIceland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='is-IS')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typIndonesianIndonesia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='id-ID')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typItalianItaly():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='it-IT')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typItalianSwitzerland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='it-CH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typJapaneseJapan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ja-JP')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typJavaneseIndonesia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='jv-ID')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typKannadaIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='kn-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typKazakhKazakhstan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='kk-KZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typKhmerCambodia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='km-KH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typKoreanSouthKorea():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ko-KR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typLaoLaos():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='lo-LA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typLatvianLatvia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='lv-LV')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typLithuanianLithuania():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='lt-LT')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typMacedonianNorthMacedonia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='mk-MK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typMalayMalaysia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ms-MY')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typMalayalamIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ml-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typMarathiIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='mr-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typMongolianMongolia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='mn-MN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typNepaliNepal():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ne-NP')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typNorwegianBokmlNorway():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='no-NO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typPersianIran():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='fa-IR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typPolishPoland():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='pl-PL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typPortugueseBrazil():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='pt-BR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typPortuguesePortugal():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='pt-PT')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typPunjabiGurmukhiIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='pa-Guru-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typRomanianRomania():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ro-RO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typRussianRussia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ru-RU')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSerbianSerbia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sr-RS')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSinhalaSriLanka():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='si-LK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSlovakSlovakia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sk-SK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSlovenianSlovenia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sl-SI')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishArgentina():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-AR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishBolivia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-BO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishChile():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-CL')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishColombia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-CO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishCostaRica():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-CR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishDominicanRepublic():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-DO')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishEcuador():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-EC')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishElSalvador():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-SV')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishGuatemala():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-GT')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishHonduras():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-HN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishMexico():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-MX')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishNicaragua():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-NI')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishPanama():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-PA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishParaguay():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-PY')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishPeru():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-PE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishPuertoRico():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-PR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishSpain():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-ES')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishUnitedStates():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-US')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishUruguay():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-UY')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSpanishVenezuela():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='es-VE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSundaneseIndonesia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='su-ID')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSwahiliKenya():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sw-KE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSwahiliTanzania():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sw-TZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typSwedishSweden():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='sv-SE')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTamilIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ta-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTamilMalaysia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ta-MY')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTamilSingapore():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ta-SG')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTamilSriLanka():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ta-LK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTeluguIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='te-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typThaiThailand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='th-TH')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typTurkishTurkey():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='tr-TR')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typUkrainianUkraine():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='uk-UA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typUrduIndia():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ur-IN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typUrduPakistan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='ur-PK')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typUzbekUzbekistan():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='uz-UZ')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typVietnameseVietnam():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='vi-VN')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng
    def typZuluSouthAfrica():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            status.value = "Listening..."
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            status.value = "Recognizing..."
            typethingeng = r.recognize_google(audio, language='zu-ZA')
            print(f"user said: {typethingeng}\n")
        except Exception as e:
            print(e)
            return "None"
        status.value = "PRESS HOTKEY"
        return typethingeng


    while True:
        #print(str(User_interface.value))
        while User_interface.value == 0:
            if keyboard.is_pressed("ctrl + shift"):
                Language13 = str(Language_1.value)
                Language13 = Language13.replace(" ","").replace("(","").replace(")","").replace(",","")
                Language13 = "typ"+Language13
                #gg = globals()[pagal]
                typethingh = locals()[Language13]()
                content = typethingh
                if content == "None":
                    status.value = "PRESS HOTKEY"
                else:
                    pyperclip.copy(content)
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'v')


            if keyboard.is_pressed("ctrl + alt"):

                Language23 = str(Language_2.value)
                Language23 = Language23.replace(" ","").replace("(","").replace(")","").replace(",","")
                Language23 = "typ"+Language23
                #gg = globals()[pagal]
                typethinghe = locals()[Language23]()
                content = typethinghe
                if content == "None":
                    status.value = "PRESS HOTKEY"
                else:
                    pyperclip.copy(content)
                    time.sleep(0.5)
                    pyautogui.hotkey('ctrl', 'v')
        '''

        if keyboard.is_pressed("ctrl + 1") and foronetime == 0:
            foronetime = 1
            time.sleep(1)
            typethinghe = typep()
            content = typethinghe
            pyperclip.copy(content)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
        

        '''




Register = None






firebaseConfig = {
    "apiKey": "AIzaSyCohmb-xbwVMH7LN3gL2BhSNM1Uy4ZojNA",
    "authDomain": "voice-typer-beta.firebaseapp.com",
    "projectId": "voice-typer-beta",
    "storageBucket": "voice-typer-beta.appspot.com",
    "messagingSenderId": "459931259449",
    "appId": "1:459931259449:web:0b263ed7254f748d1273e8",
    "measurementId": "G-46YPRNMMKZ",
    "databaseURL": "https://voice-typer-beta-default-rtdb.firebaseio.com"
}

Firebase = pyrebase.initialize_app(firebaseConfig)
auth = Firebase.auth()
storage = Firebase.storage()
database = Firebase.database()

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

#FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"voice typer ui.ui"))


class Main(QMainWindow): #,FROM_MAIN):
    global Logged_in
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        loadUi("voice typer ui.ui",self)
        #self.setupUi(self)
        widget.setFixedSize(1381,801)
        self.ts = time.strftime("%A, %d %B")
        self.whatshesaid.setText("<font size=12 color='#4ac8eb'>"+self.ts+"</font>")
        self.sign_out.clicked.connect(self.gotologin)
        #self.whatshesaid_2.setText("<font size=12 color='#4ac8eb'>"+ "listening" +"</font>")
        self.internet.setHidden(True)

    def gotologin(self):
        global Logged_in
        if Logged_in == False:
            Login = login()
            widget.addWidget(Login)

        my_shine = open(r"C:\ProgramData\Logged_in.txt", "w")
        my_shine.write("N")
        my_shine.close()
        widget.setCurrentIndex(widget.currentIndex() +1)






class login(QDialog):
    global register_loaded
    global Register
    def __init__(self):
        super(login,self).__init__()
        loadUi("Log_in.ui",self)
        widget.setFixedSize(897,617)
        self.Register_button.clicked.connect(self.switchtoregister)
        self.Login_button.clicked.connect(self.login_to_firebase)
        self.internet.setHidden(True)


    def switchtoregister(self):
        global register_loaded
        global Register
        if register_loaded == False:
            Register = register()
            widget.addWidget(Register)
        if register_loaded == True:
            pass
        #if widget.currentIndex == 
        widget.setCurrentIndex(widget.currentIndex() +1)
        #widget.removeWidget(self)
        #widget.setCurrentIndex(widget.currentIndex() +1)

    def login_to_firebase(self):
        global auth
        global Firebase
        email = self.Email_input.toPlainText()
        password = self.Password_input.toPlainText()
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            #main = Main()
            #widget.addWidget(main)
            my_file = open(r"C:\ProgramData\Logged_in.txt", "w")
            email_credentials = email
            my_file.write(email_credentials +"\n")
            my_file.write(password)
            my_file.close()
            widget.setCurrentIndex(widget.currentIndex() - 1)
            widget.setFixedSize(1381,801)
        except Exception as a:
            print(a)
            self.Hidden_label.setText("<font size=4 color='#ff0000'>"+"wrong or NOT registered email or WRONG password"+"</font>")






class register(QDialog):
    global register_loaded
    global auth
    global Firebase
    def __init__(self):
        super(register,self).__init__()
        loadUi("Register_user.ui",self)
        widget.setFixedSize(897,617)
        self.Login_Button.clicked.connect(self.gotologin)
        self.Register_button.clicked.connect(self.register_firebase)
        self.internet.setHidden(True)
    def gotologin(self):
        #Login = login()
        #widget.addWidget(Login)
        #if widget.currentIndex() == 4:
        #    widget.removeWidget(self)
        global register_loaded
        register_loaded = True
        widget.setCurrentIndex(widget.currentIndex() -1)

    def register_firebase(self):
        global auth
        global Firebase
        email = self.Email_user_input.toPlainText()
        password = self.Password_user_input.toPlainText()
        confirm_pass = self.Confirm_Passoword_user_input.toPlainText()
        if password == confirm_pass:
            try:
                user = auth.create_user_with_email_and_password(email,password)
                self.Hidden_thing.setText("<font size=5 color='#55ff00'>"+"you are registered, plaease login"+"</font>")
            except Exception as identifier:
                print(identifier)
                self.Hidden_thing.setText("<font size=5 color='#ff0000'>"+"wrong or registered email or weak password"+"</font>")
        else:
            self.Hidden_thing.setText("<font size=5 color='#ff0000'>"+"Passwords not matched"+"</font>")
            



if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    try:
        file1 = open(r"C:\ProgramData\Logged_in.txt","r")
    except Exception:
        file1 = open(r"C:\ProgramData\Logged_in.txt","w+")
    login_state = file1.read()
    '''
    if login_state == "Y":
        main = Main()
        main.show()
        manager = multiprocessing.Manager()
        status = manager.Value(c_char_p, "PRESS HOTKEY")
        Language_1 = manager.Value(c_char_p, "hindi")
        Language_2 = manager.Value(c_char_p, "ENGLISH")
        p1 = Process(target = trying, args=(status,Language_1,Language_2))
        p1.start()
        p2 = Process(target=toreduce)
        p2.start()
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(100)
        print ("yess")
        sys.exit(app.exec_())
    '''
    widget=QtWidgets.QStackedWidget()
    main = Main()
    widget.addWidget(main)
    #widget.setFixedSize(1381,801)
    widget.show()
    to_check = open(r"C:\ProgramData\Logged_in.txt")
    content = to_check.read()
    to_check.close()
    if content == "N":
        Login = login()
        widget.addWidget(Login)
        widget.setCurrentIndex(widget.currentIndex() +1)
    else:
        try:
            to_check3 = open(r"C:\ProgramData\Logged_in.txt")
            string_list = to_check3.readlines()
            to_check3.close()
            email_id = str(string_list[0])
            email_id = email_id.replace("\n","")
            print(email_id)
            #print(email_id)
            password_cre = str(string_list[1])
            logggggin = auth.sign_in_with_email_and_password(email_id,password_cre)
        except Exception as I:
            print(I)
            to_check2 = open(r"C:\ProgramData\Logged_in.txt", "w+")
            to_check2.write("N")
            to_check2.close()
            Login = login()
            widget.addWidget(Login)
            widget.setCurrentIndex(widget.currentIndex() +1)


    #main.show()
    manager = multiprocessing.Manager()
    status = manager.Value(c_char_p, "PRESS HOTKEY")
    status_of_internet = manager.Value(c_char_p, "PRESS HOTKEY")
    Language_1 = manager.Value(c_char_p, "hindi")
    Language_2 = manager.Value(c_char_p, "ENGLISH")
    User_interface = manager.Value(c_char_p, 0)
    p1 = Process(target = trying, args=(status,Language_1,Language_2,User_interface))
    p1.start()
    p2 = Process(target=Internet, args=(status_of_internet, User_interface))
    p2.start()
    p3 = Process(target=Update_the_app, args=(status_of_internet, User_interface))
    p3.start()
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.timeout.connect(toreduce)
    timer.start(100)
    #timer2 = QtCore.QTimer()
    #timer2.timeout.connect(Internet)
    #timer2.start(10000)
    print ("yess")
    sys.exit(app.exec_())




