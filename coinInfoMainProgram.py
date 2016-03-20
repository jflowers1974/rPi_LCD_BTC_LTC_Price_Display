#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import textwrap
import sys
import time
import urllib2
import json


#Make certain that the permission permit writing to
#
sys.path.append("/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#
lcd = Adafruit_CharLCDPlate()

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.LEFT  , ''),
       (lcd.UP    , ''),
       (lcd.DOWN  , ''),
       (lcd.RIGHT , ''),
       (lcd.SELECT, ''))

HALT_ON_EXIT = True
prev = -1

sys.path.append('/home/pi/Jeffs_Ticker_Prices')

def shutdown():
	lcd.clear()
	if HALT_ON_EXIT:
		lcd.message('Wait 30 sec')
		subprocess.call("sync")
		subprocess.call(["shutdown", "-h", "now"])
	else:
		exit(0)

def displayBtcCurrency():
	lcd.clear()
	lcd.backlight(lcd.GREEN)
	subprocess.call('sudo python get_current_price_btc.py', shell = True)
	from get_current_price_btc import price_bitcoin
	lcd.message('Bitcoin is:\n$' + price_bitcoin + '/btc')
	time.sleep(5)

def displayLtcCurrency():
	lcd.clear()
	lcd.backlight(lcd.RED)
	subprocess.call('sudo python get_current_price_ltc.py', shell = True)
	from get_current_price_ltc import price_litecoin
	lcd.message('Litecoin is:\n$' + price_litecoin + '/ltc')
	time.sleep(5)

def cleanScreen():
	lcd.clear()
	lcd.backlight(lcd.YELLOW)
	lcd.message('Welcome: ltc/btc \n           <- ->')

cleanScreen()

while True:
	for b in btn:
		if lcd.buttonPressed(b[0]):
			if b is not prev:
		        	if lcd.buttonPressed(lcd.SELECT):
		        		lcd.message('Shutdown Init')
		        		tt = time.time()
		        		while lcd.buttonPressed(lcd.SELECT):
		        			if (time.time() - tt) >= 3:
		        				shutdown()
		        	elif lcd.buttonPressed(lcd.UP):
		        		displayBtcCurrency()
		        		subprocess.call('sudo python text_to_speech_btc.py',shell = True)
					cleanScreen()
		        	elif lcd.buttonPressed(lcd.RIGHT):
		        		displayBtcCurrency()
					cleanScreen()
		        	elif lcd.buttonPressed(lcd.DOWN):
		                	displayLtcCurrency()
		                	subprocess.call('sudo python text_to_speech_ltc.py',shell = True)
					cleanScreen()
		        	elif lcd.buttonPressed(lcd.LEFT):
		                	displayLtcCurrency()
					cleanScreen()
		        	prev = b
		        	lastTime = time.time()
		        break
