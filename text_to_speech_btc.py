#!/usr/bin/python
# -*- coding: utf-8

import subprocess
import time
import textwrap

from better_spoken_time import now
from better_spoken_time import period
from get_current_price_btc import price_bitcoin
from variables import name

# reads out good morning + my name
gmt = 'Good' + period + name + ','

# reads date and time (sorry for the no apostrophe in it's)
day = ' it is ' + now

btc = ' .. The value of 1 bitcoin in dollars is: ' + str(price_bitcoin) + '..'

wad = (gmt + day + btc)
print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)
