#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

from variables import btcUrlInfo

btc_api = urllib2.urlopen(btcUrlInfo)
response = btc_api.read()
response_dictionary = json.loads(response)

price_bitcoin = response_dictionary['amount']
print price_bitcoin
