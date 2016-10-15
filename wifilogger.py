# -*- coding: utf-8 -*-

__author__="skrilic"
__date__ ="$04.07.2010. 20:12:25$"

import sys
from pythonwifi.iwlibs import Wireless
from pythonwifi.iwlibs import getNICnames

channels = {
'2412000000':'1',
'2417000000':'2',
'2422000000':'3',
'2427000000':'4',
'2432000000':'5',
'2437000000':'6',
'2442000000':'7',
'2447000000':'8',
'2452000000':'9',
'2457000000':'10',
'2462000000':'11',
'2467000000':'12',
'2472000000':'13',
'2484000000':'14'
}

def findif():
    """
    Function finds network interfaces on a PC
    """
    ifnames=getNICnames()
    if len(ifnames) > 0:
        ifid = ifnames[0]
        print ifid
    else:
        ifid = 'none'
    return ifid

def scanwifi(ifid):
    wifi = Wireless(ifid)
    wifilist = wifi.scan()
    for ap in wifilist.aplist:
        #print "bssid:%s; essid:%s; chann.:%s, signlev.:%s dBm; mode:%s" % \
        #   (ap.bssid, ap.essid, channels['%s' % ap.frequency.getFrequency()], \
        #    ap.quality.signallevel-255, ap.mode)
        # Zyxel Zyair G-220 EE Linux driver, probably gives signal level
        # above receiver sensibility and it is -85dBm ...
        print "bssid:%s; essid:%s; chann.:%s, signlev.:%s dBm; mode:%s" % \
           (ap.bssid, ap.essid, channels['%s' % ap.frequency.getFrequency()], \
            ap.quality.signallevel-85, ap.mode)

if __name__ == "__main__":
    wiif = sys.argv[1]
    scanwifi(wiif)
    #print "Hello World"
