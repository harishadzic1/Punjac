from guizero import App, PushButton, Text, Picture, Box, Window
from tkinter import *
import time
from PIL import Image
import RPi.GPIO as GPIO

########################################################################################################
#					VARIJABLE
########################################################################################################


SDI   = 11 			#pin number 11 on board
RCLK  = 12			#pin number 12 on board
SRCLK = 13			#pin number 13 on board

chargerBits = 0		
time4Closing = 0	#timer for return to home page

punjac1zauzet = False
punjac2zauzet = False
punjac3zauzet = False
punjac4zauzet = False
punjac5zauzet = False
punjac6zauzet = False

button1Text = "1"
button2Text = "2"
button3Text = "3"
button4Text = "4"
button5Text = "5"
button6Text = "6"

punjac1Vrijeme = 0
punjac2Vrijeme = 0
punjac3Vrijeme = 0
punjac4Vrijeme = 0
punjac5Vrijeme = 0
punjac6Vrijeme = 0

########################################################################################################
#					SETUP PINOVA
########################################################################################################


def setup():
	GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

########################################################################################################
#					UPISIVANJE PODATAKA U SHIFT REGISTAR
########################################################################################################

def hc595_in(dat):
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)

########################################################################################################
#					LATCH SHIFT REGISTRA
########################################################################################################

def hc595_out():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

########################################################################################################
#					PRIKAZ I MIJENJANJE REKLAMA
########################################################################################################

def print1():
	global reklamniText
	global counter
	global interval
	if interval > 0:
		interval-=1
	elif interval == 0:
		interval = 5
		if counter == 3:
			counter = 1
		elif counter < 3:
			counter+=1
	reklamniText="REKLAMA " + str(counter) + "\n\n\n\nPRITISNI EKRAN DA AKTIVIRAS\ntrajanje: " + str(interval) + " sekundi" 
#	activationButton.image = "/home/pi/go/src/baza_testna/bg.png"
	activationButton.text = reklamniText
	checkTimes()

########################################################################################################
#					OTVARANJE EKRANA ZA BIRANJE VRATA NAKON KLIKA
########################################################################################################

def setupScreen():
	time.sleep(0.25)
	global messageText
	global time4Closing
	time4Closing = int(time.time()) + 30
	messageText = "ODABERITE VRATA" 
	windowText.text = messageText
	windowText.height=5
	windowText.width=30
	button1.visible = True
	button2.visible = True
	button3.visible = True
	button4.visible = True
	button5.visible = True
	button6.visible = True
	cijena.visible = True
	window.show()
	window.set_full_screen()

########################################################################################################
#					AKTIVIRANJE PUNJACA 1
########################################################################################################
	
def punjac1():
	global punjac1zauzet
	global messageText
	global punjac1Vrijeme
	global button1Text
	global chargerBits
	if punjac1zauzet == False:
		messageText="Punjac 1 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac1Vrijeme = time.time() + 1 * 60
		hours = time.localtime(punjac1Vrijeme).tm_hour
		minutes = time.localtime(punjac1Vrijeme).tm_min
		seconds = time.localtime(punjac1Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button1Text = "1\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button1Text = "1\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button1Text = "1\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button1Text = "1\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button1.text = button1Text
		punjac1zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b00000010
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 1 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	
   
########################################################################################################
#					AKTIVIRANJE PUNJACA 2
########################################################################################################

def punjac2():
	global punjac2zauzet
	global messageText
	global punjac2Vrijeme
	global button2Text
	global chargerBits
	if punjac2zauzet == False:
		messageText="Punjac 2 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac2Vrijeme = time.time() + 1 * 60
		minutes = time.localtime(punjac2Vrijeme).tm_min
		hours = time.localtime(punjac2Vrijeme).tm_hour
		seconds = time.localtime(punjac2Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button2Text = "2\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button2Text = "2\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button2Text = "2\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button2Text = "2\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button2.text = button2Text
		punjac2zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b00000100
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 2 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	
        
########################################################################################################
#					AKTIVIRANJE PUNJACA 3
########################################################################################################

def punjac3():
	global punjac3zauzet
	global messageText
	global punjac3Vrijeme
	global button3Text
	global chargerBits
	if punjac3zauzet == False:
		messageText="Punjac 3 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac3Vrijeme = time.time() + 1 * 60
		minutes = time.localtime(punjac3Vrijeme).tm_min
		hours = time.localtime(punjac3Vrijeme).tm_hour		
		seconds = time.localtime(punjac3Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button3Text = "3\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button3Text = "3\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button3Text = "3\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button3Text = "3\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button3.text = button3Text
		punjac3zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b00001000
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 3 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	

########################################################################################################
#					AKTIVIRANJE PUNJACA 4
########################################################################################################
    
def punjac4():
	global punjac4zauzet
	global messageText
	global punjac4Vrijeme
	global button4Text
	global chargerBits
	if punjac4zauzet == False:
		messageText="Punjac 4 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac4Vrijeme = time.time() + 1 * 60
		minutes = time.localtime(punjac4Vrijeme).tm_min
		hours = time.localtime(punjac4Vrijeme).tm_hour
		seconds = time.localtime(punjac4Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button4Text = "4\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button4Text = "4\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button4Text = "4\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button4Text = "4\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button4.text = button4Text 
		punjac4zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b00010000
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 4 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	
    
########################################################################################################
#					AKTIVIRANJE PUNJACA 5
########################################################################################################
    
def punjac5():
	global punjac5zauzet
	global messageText
	global punjac5Vrijeme
	global button5Text
	global chargerBits
	if punjac5zauzet == False:
		messageText="Punjac 5 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac5Vrijeme = time.time() + 1 * 60
		minutes = time.localtime(punjac5Vrijeme).tm_min
		hours = time.localtime(punjac5Vrijeme).tm_hour
		seconds = time.localtime(punjac5Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button5Text = "5\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button5Text = "5\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button5Text = "5\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button5Text = "5\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button5.text = button5Text
		punjac5zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b00100000
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 5 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	

########################################################################################################
#					AKTIVIRANJE PUNJACA 6
########################################################################################################
    
def punjac6():
	global punjac6zauzet
	global messageText
	global punjac6Vrijeme
	global button6Text
	global chargerBits
	if punjac6zauzet == False:
		messageText="Punjac 6 odabran uspjesno \n \n Uzivajte u boravku!"
		punjac6Vrijeme = time.time() + 1 * 60
		minutes = time.localtime(punjac6Vrijeme).tm_min
		hours = time.localtime(punjac6Vrijeme).tm_hour
		seconds = time.localtime(punjac6Vrijeme).tm_sec
		if hours < 10 and seconds < 10:
			button6Text = "6\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours < 10 and seconds >= 10:
			button6Text = "6\nZauzet do 0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		elif hours >= 10 and seconds < 10:
			button6Text = "6\nZauzet do " + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
		elif hours >= 10 and seconds >= 10:
			button6Text = "6\nZauzet do " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
		button6.text = button6Text
		punjac6zauzet = True
		button1.visible = False
		button2.visible = False
		button3.visible = False
		button4.visible = False
		button5.visible = False
		button6.visible = False
		cijena.visible = False
		chargerBits = chargerBits + 0b01000000
		hc595_in(chargerBits)
		hc595_out()
	else:
		messageText="Punjac 6 zauzet, odaberite neki drugi!"
	windowText.text = messageText
	windowText.height=32
	windowText.width=75
	window.update()
	time.sleep(3)
	window.hide() 	

########################################################################################################
#					GASENJE PUNJACA NAKON ISTEKA VREMENA I POVRATAK NA POCETNI EKRAN NAKON 30S
########################################################################################################

def checkTimes():
	global punjac1Vrijeme
	global punjac2Vrijeme
	global punjac3Vrijeme
	global punjac4Vrijeme
	global punjac5Vrijeme
	global punjac6Vrijeme
	global button1
	global button2
	global button3
	global button4
	global button5
	global button6
	global punjac1zauzet
	global punjac2zauzet
	global punjac3zauzet
	global punjac4zauzet
	global punjac5zauzet
	global punjac6zauzet
	global chargerBits
	global time4Closing
	if int(time.time()) >= time4Closing:
		window.hide()
	if time.time() > punjac1Vrijeme and punjac1Vrijeme != 0:
		punjac1Vrijeme = 0
		button1.text = "1"
		punjac1zauzet = False
		chargerBits = chargerBits & ~0b00000010
	if time.time() > punjac2Vrijeme and punjac2Vrijeme != 0:
		punjac2Vrijeme = 0
		button2.text = "2"
		punjac2zauzet = False
		chargerBits = chargerBits & ~0b00000100

	if time.time() > punjac3Vrijeme and punjac3Vrijeme != 0:
		punjac3Vrijeme = 0
		button3.text = "3"
		punjac3zauzet = False
		chargerBits = chargerBits & ~0b00001000

	if time.time() > punjac4Vrijeme and punjac4Vrijeme != 0:
		punjac4Vrijeme = 0
		button4.text = "4"
		punjac4zauzet = False
		chargerBits = chargerBits & ~0b00010000

	if time.time() > punjac5Vrijeme and punjac5Vrijeme != 0:
		punjac5Vrijeme = 0
		button5.text = "5"
		punjac5zauzet = False
		chargerBits = chargerBits & ~0b00100000

	if time.time() > punjac6Vrijeme and punjac6Vrijeme != 0:
		punjac6Vrijeme = 0
		button6.text = "6"
		punjac6zauzet = False
		chargerBits = chargerBits & ~0b01000000

	hc595_in(chargerBits)
	hc595_out()

########################################################################################################
#					MAIN
########################################################################################################

setup() 
hc595_in(0)
hc595_out()
app = App(title="Main Screen")
box = Box(app, layout="grid", align="bottom")
window = Window(app, layout = "auto", bg = "white", title="Autentifikacija")
windowBox = Box(window, layout="grid")
windowText = PushButton(windowBox, width = 30, height = 5, text="ODABERITE VRATA", grid=[0,0,2,2])
windowText.text_size = 20

cijena = PushButton(windowBox, width = 30, height = 5, text="Cijena:\n1 KM / 30 min", grid=[0,5,2,2])
cijena.text_size = 20
window.hide()

messageText=""
reklamniText = "REKLAMA 1\n\n\n\nPRITISNI EKRAN DA AKTIVIRAS\ntrajanje: 5 sekundi" #umjesto ovog texta ce ici slika reklame
counter = 1 	#redni broj reklame
interval = 5 	#trajanje reklame

button1 = PushButton(windowBox, text = button1Text, width = 20, height = 5, grid=[0,2])
button2 = PushButton(windowBox, text = button2Text, width = 20, height = 5, grid=[1,2])
button3 = PushButton(windowBox, text = button3Text, width = 20, height = 5, grid=[0,3])
button4 = PushButton(windowBox, text = button4Text, width = 20, height = 5, grid=[1,3])
button5 = PushButton(windowBox, text = button5Text, width = 20, height = 5, grid=[0,4])
button6 = PushButton(windowBox, text = button6Text, width = 20, height = 5, grid=[1,4])

button1.text_size = 20
button2.text_size = 20
button3.text_size = 20
button4.text_size = 20
button5.text_size = 20
button6.text_size = 20

button1.when_clicked = punjac1
button2.when_clicked = punjac2
button3.when_clicked = punjac3
button4.when_clicked = punjac4
button5.when_clicked = punjac5
button6.when_clicked = punjac6

activationButton = PushButton(box, text=reklamniText, width=50, height=20, grid=[0,0,3,1])
activationButton.bg="white"
activationButton.text_size = 30
activationButton.repeat(1000, print1) # update reklame 
activationButton.when_clicked = setupScreen

app.set_full_screen()
app.display()
