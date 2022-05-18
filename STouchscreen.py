
import tkinter as tk
import tkinter.font as font
from tkinter import StringVar, ttk
from tkinter.constants import NORMAL
import pytz

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

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = ()

		global wifiSSID
		wifiSSID = tk.StringVar()
		global wifiPassword
	        wifiPassword = tk.StringVar()

		for index, F in enumerate([Home, Data, Info, Settings]) #fill in whatever pages needed
			print("Framing ", F, " with index ", index)

			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew"

		self.show_frame(Home)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class Home(tk.Frame):
	def delete_all(self):
		for obj in self.winfo_children():
			obj.destroy()

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		buttonFont = font.Font(self, family='Georgia', size='12', weight='bold')
		fieldFOnt = font.Font(self, family='Aerial', size='12')
		textFont = font.Font(self, family='Times', size='10', weight='normal', slant='roman', underline=0, overstrike=0)

		buttonHome = tk.Button(self, text="Home", font=buttonFont, command = lambda : controller.show_frame(Home))
		buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)

		buttonData = ttk.Button(self, text="Data", command = lambda : controller.show_frame(Data))
		buttonData.grid(row = 1, column = 0, padx = 10, pady = 10)

		buttonInfo = ttk.Button(self, text="Info", command = lambda : controller.show_frame(Info)
		buttonInfo.grid(row = 2, column = 0, padx = 10, pady = 10)

		buttonSettings = ttk.Button(self, text="Settings", command = lambda : controller.show_frame(Settings))
		buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)

		buttonQuit = ttk.Button(self, text="Quit", command=self.destroy)
		buttonQuit.grid(row = 3, column = 5, padx = 10, pady = 10)

class Data(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		buttonFont = font.Font(self, family='Georgia', weight='bold')
		fieldFont = font.Font(self,family='Aerial', size='12')
		textFont = font.Font(self, family='Times',size='10',weight='normal',slant='roman',underline=0,overstrike=0)
		mainButtonWidth = 8

		buttonHome = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(Home), width = mainButtonWidth)
	        buttonHome.grid(row = 0, column = 0, padx = 10, pady = 10)

       	 	buttonData = tk.Button(self, text ="Data", font=buttonFont, command = lambda : controller.show_frame(Data), width = mainButtonWidth)
        	buttonData.grid(row = 1, column = 0, padx = 10, pady = 10)

        	buttonInfo = ttk.Button(self, text ="Info", command = lambda : controller.show_frame(Info), width = mainButtonWidth)
        	buttonInfo.grid(row = 2, column = 0, padx = 10, pady = 10)

        	buttonSettings = ttk.Button(self, text ="Settings", command = lambda : >
        	buttonSettings.grid(row = 3, column = 0, padx = 10, pady = 10)

#fill in temp, humidity, and pms data, with the option to refresh

#class Info

#class Settings
app = tkinterApp()
while True:
	app.update_idletasks()
	app.update()
	time.sleep(0.1)

app.mainloop()
