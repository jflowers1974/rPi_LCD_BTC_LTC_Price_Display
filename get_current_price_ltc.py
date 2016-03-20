#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

from variables import ltcUrlInfo

ltc_api = urllib2.urlopen(ltcUrlInfo)
response = ltc_api.read()
response_dictionary_ltc = json.loads(response)

# Want to format the amount that a Litecoin is in USD
# Need to round to two decimals too
#
ltcAmt = 1/float(response_dictionary_ltc['data'][0]['rates']['LTC'])
price_litecoin = "{:.2f}".format(ltcAmt)
#print price_litecoin
