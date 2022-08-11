#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

#ADD:
# 1. Keyboard: https://codingshiksha.com/python/python-3-tkinter-script-to-display-virtual-on-screen-keyboard-on-canvas-window-to-take-input-gui-desktop-app-full-project-for-beginners/
# 2. Add sensitivity settings
# 3. Take user-values for sensitivities
# 4. Add MES info
# 5. Add real-time data from sensor devices to "Info" frame.
# 6. Make full screen (eliminate 'destroy' button)
# 7. Add "Connecting...." and "Connected!" messages in WIFI class after get() credentials
# 8. Allow user to input time-zone. Update in Pi system.


#from _typeshed import Self
import tkinter as tk
import tkinter.font as font
from tkinter import StringVar, ttk
from tkinter.constants import NORMAL
import pytz #timezone calcuations and formatting

import os
import time
from datetime import datetime
TIMEZONE = pytz.timezone('US/Eastern')
rawTime = datetime.now(TIMEZONE)
timeNow = rawTime.strftime("%H:%M:%s %p")

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

LARGEFONT =("Georgia", 20)

#s = ttk.Style(tk.Tk())
#s.configure('buttonStyle', font=('Georgia', 20, 'bold'))
#s.configure('fieldStyle', font=('Aerial',12,NORMAL))
#s.configure('textStyle', font = ('Times', 18, 'italic'))

class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        # initializing frames to an empty array
        self.frames = {} 

        global wifiSSID 
        wifiSSID = tk.StringVar()
        global wifiPassword 
        wifiPassword = tk.StringVar()

        # iterating through a tuple consisting
        # of the different page layouts
        for index, F in enumerate([Home, Info, Wifi, Settings, QuickSet, SetSensitivities]):
            print ("Framing ", F, " with index ", index)
            frame = F(container, self)

            # initializing frame of that object from
            # Home, Info, Wifi, Settings, QuickSet respectively with for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")
        

        self.show_frame(Home)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(tk.Frame):

    def delete_all(self):
        for obj in self.winfo_children():
            obj.destroy()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', size='12', weight='bold')
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)


        #labelHome = tk.Label(self, text ="Home", font = LARGEFONT)
        #labelHome.grid(row = 0, column = 5, padx = 10, pady = 10)
  
        #buttonHome = ttk.Button(self, text ="Home", style=ttk.Style.configure( style='buttonStyle', forebround = 'blue', font=('Georgia', 20, 'bold')), command = lambda : controller.show_frame(Home))
        #Use a "tk" button with font option for screen selection
        buttonHome = tk.Button(self, text ="Home",font=buttonFont, command = lambda : controller.show_frame(Home))        
        buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        buttonInfo = ttk.Button(self, text ="Info", command = lambda : controller.show_frame(Info))
        buttonInfo.grid(row = 1, column = 0, padx = 10, pady = 10)
  
        buttonWifi = ttk.Button(self, text ="Wifi", command = lambda : controller.show_frame(Wifi))
        buttonWifi.grid(row = 2, column = 0, padx = 10, pady = 10)

        buttonSettings = ttk.Button(self, text ="Settings", command = lambda : controller.show_frame(Settings))
        buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)

        #ONLY destroys current frame.... Need to destroy ALL or quit program.
        #buttonQuit =ttk.Button(self, text="Quit", command=self.delete_all())        
        buttonQuit =ttk.Button(self, text="Quit", command=self.destroy)
        buttonQuit.grid(row = 3, column = 5, padx = 10, pady = 10)
    

class Info(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', weight='bold')
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)
        mainButtonWidth = 8
        #labelHome = ttk.Label(self, text ="Info", font = LARGEFONT)
        #labelHome.grid(row = 0, column = 5, padx = 10, pady = 10)
  
        buttonHome = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(Home), width = mainButtonWidth)
        buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        buttonInfo = tk.Button(self, text ="Info", font=buttonFont, command = lambda : controller.show_frame(Info), width = mainButtonWidth)
        buttonInfo.grid(row = 1, column = 0, padx = 10, pady = 10)
  
        buttonWifi = ttk.Button(self, text ="Wifi", command = lambda : controller.show_frame(Wifi), width = mainButtonWidth)
        buttonWifi.grid(row = 2, column = 0, padx = 10, pady = 10)

        buttonSettings = ttk.Button(self, text ="Settings", command = lambda : controller.show_frame(Settings), width = mainButtonWidth)
        buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)
        
        rawTime = datetime.now(TIMEZONE)
        timeNow = rawTime.strftime("%H:%M:%s %p")
        global timeLabel
        timeLabel = tk.Label(self, text = timeNow, font = textFont)
        timeLabel.grid(row=1,column=1)

        buttonRefresh = tk.Button(self, text = "Refresh", font=buttonFont, command = self.update_info)#controller.update())#lambda : self.update_info)
        buttonRefresh.grid(row = 5, column = 1)

    def update_info(self):
        rawTime = datetime.now(TIMEZONE)
        timeNow = rawTime.strftime("%H:%M:%s %p")
        dateNow = rawTime.strftime("%d %b %Y")
        dateFormatted = rawTime.strftime("%d-%m-%Y")
        timeLabel.config(text = timeNow)
        timeLabel.after(1000, self.update_info) #update clock every 1,000 ms
        return timeNow

#Info(tk.Frame) #try to run get_info function to constantly update values

# declaring string variable for storing name and password
#wifiSSID=tk.StringVar()
#wifiPassword=tk.StringVar() 
class Wifi(tk.Frame):
    #wifiSSID=tk.Frame.StringVar()
    #wifiPassword=tk.Frame.StringVar() 
    
    # defining a function that will get the name and password and print them on the screen
    def submit(self):
        wifiSSID.get()
        wifiPassword.get()
        print("The name is : " + str(wifiSSID.get()))
        print("The password is : " + str(wifiPassword.get()))
        labelCurrentWifiSSID.config(text="Current Value: "+str(wifiSSID.get()))
        wifiSSID.set("")
        wifiPassword.set("")
        print("The name is : " + str(wifiSSID.get()))
#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

    def __init__(self, parent, controller):

        #ssid = StringVar
        #password = StringVar
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', size='12', weight='bold')
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)

        #Wifi SSID entry label and button
        labelWifiSSID = tk.Label(self, text = 'WIFI Username', font=textFont)
        labelWifiSSID.grid(row = 1, column = 2)
        entryWifiSSID = tk.Entry(self,textvariable = wifiSSID, font=fieldFont)
        entryWifiSSID.grid(row = 1, column = 3)
        global labelCurrentWifiSSID
        labelCurrentWifiSSID = tk.Label(self, text = 'Current Value: '+ str(wifiSSID.get()), font=textFont)
        labelCurrentWifiSSID.grid(row=0,column=2)
        labelCurrentWifiSSID.config(text = 'Current Value: '+ wifiSSID.get())

        #Wifi password entry label and button
        labelWifiPassword = tk.Label(self, text = 'WIFI Password', font=textFont)
        labelWifiPassword.grid(row = 2, column = 2)
        entryWifiPassword = tk.Entry(self,textvariable = wifiPassword, font=fieldFont)
        entryWifiPassword.grid(row = 2, column = 3)
        #Wifi submit button
        submitButton=tk.Button(self,text = 'Submit', command = self.submit)
        #submitButton=tk.Button(self,text = 'Submit')

        submitButton.grid(row=3, column = 2)



        #labelHome = ttk.Label(self, text ="Wifi", font = LARGEFONT)
        #labelHome.grid(row = 0, column = 5, padx = 10, pady = 10)
  
        buttonHome = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(Home))
        buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        buttonInfo = ttk.Button(self, text ="Info", command = lambda : controller.show_frame(Info))
        buttonInfo.grid(row = 1, column = 0, padx = 10, pady = 10)
  
        buttonWifi = tk.Button(self, text ="Wifi", font=buttonFont, command = lambda : controller.show_frame(Wifi))
        buttonWifi.grid(row = 2, column = 0, padx = 10, pady = 10)

        buttonSettings = ttk.Button(self, text ="Settings", command = lambda : controller.show_frame(Settings))
        buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', size='12', weight='bold')
        settingsButtonFont = font.Font(self,family='Georgia', size='10', weight='bold') #Must decrease size of "Settings" for clicked-button sizes to match
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)


        #Settings Buttons. Columns 3+ (fourth+)
        buttonQuickSet = ttk.Button(self, text = "Quick Set", command=lambda: controller.show_frame(QuickSet))
        buttonQuickSet.grid(row = 0, column = 3)

        buttonSetSensitivities = ttk.Button(self, text = "Set Sensitivities", command=lambda: controller.show_frame(SetSensitivities))
        buttonSetSensitivities.grid(row = 1, column = 3)


        #labelHome = ttk.Label(self, text ="Settings", font = LARGEFONT)
        #labelHome.grid(row = 0, column = 5, padx = 10, pady = 10)
  
        buttonHome = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(Home))
        buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        buttonInfo = ttk.Button(self, text ="Info", command = lambda : controller.show_frame(Info))
        buttonInfo.grid(row = 1, column = 0, padx = 10, pady = 10)
  
        buttonWifi = ttk.Button(self, text ="Wifi", command = lambda : controller.show_frame(Wifi))
        buttonWifi.grid(row = 2, column = 0, padx = 10, pady = 10)

        buttonSettings = tk.Button(self, text ="Settings", font=settingsButtonFont, bg = 'blue', fg = 'yellow', command = lambda : controller.show_frame(Settings))
        buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)

#SETTINGS BUTTONS
class QuickSet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', size='12', weight='bold')
        settingsButtonFont = font.Font(self,family='Georgia', size='10', weight='bold') #Must decrease size of "Settings" for clicked-button sizes to match
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)

        buttonSettings = tk.Button(self, text ="Settings",font=settingsButtonFont, command = lambda : controller.show_frame(Settings))        
        buttonSettings.grid(row = 0, column = 0, padx = 10, pady = 10)

class SetSensitivities(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonFont = font.Font(self,family='Georgia', size='12', weight='bold')
        settingsButtonFont = font.Font(self,family='Georgia', size='10', weight='bold') #Must decrease size of "Settings" for clicked-button sizes to match
        fieldFont = font.Font(self,family='Aerial', size='12')
        textFont = font.Font(self,family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)

        buttonSettings = tk.Button(self, text ="Settings",font=settingsButtonFont, command = lambda : controller.show_frame(Settings))        
        buttonSettings.grid(row = 0, column = 0, padx = 10, pady = 10)



app = tkinterApp()
while True:
    app.update_idletasks()
    app.update()
    print("The current wifi ssid is ", wifiSSID.get())
    print("The current wifi password is ", wifiPassword.get())
    time.sleep(0.1)

app.mainloop()


    #print("At time ", datetime.datetime.utcnow(), " name var has value: ", name_var)

    #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
