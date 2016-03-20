#!/usr/bin/python
# -*- coding: utf-8

import subprocess
import time
import textwrap

from better_spoken_time import now
from better_spoken_time import period
from get_current_price_ltc import price_litecoin
from variables import name

# reads out good morning + my name
gmt = 'Good' + period + name + ','

# reads date and time (sorry for the no apostrophe in it's)
day = ' it is ' + now

ltc = ' .. The value of 1 light coin in dollars is: ' + str(price_litecoin) + '..'

wad = (gmt + day + ltc)
print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)
