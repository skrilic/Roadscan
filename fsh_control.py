#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__="skrilic"
__date__ ="$22.05.2010. 21:25:40$"

import ConfigParser
import serial
import os

fsh=serial.Serial()
confdir = "%s/conf" % os.getcwd()

def connect(fshport):
    ##---DEFINING SERIAL PORT ---
    fsh.port=fshport
    fsh.baudrate=19200
    fsh.bytesize=8
    fsh.parity='N'
    fsh.stopbits=1
    fsh.timeout=1
    fsh.xonxoff=0
    fsh.rtscts=0
    ##---------------------------
    fsh.open()

def close():
    fsh.write('CMD\r')
    fsh.write('LOCAL\r')
    fsh.close()

# FSH6 Types of commands and handling different responses
def getcmd(cmd):
    fsh.write('GET\r')
    #response
    fsh.write('%s' % cmd)
    #response
    return

def setcmd(cmd):
    fsh.write('SET\r')
    #response
    fsh.write('%s' % cmd)
    #response
    return

def cmd(cmd):
    fsh.write('CMD\r')
    #response
    fsh.write('%s\r' % cmd)
    #response
    return

def setmeas(fshconfig, reset ):
    """Gpsmgr
    Set instrument for specfic data.
    """
    config = ConfigParser.ConfigParser()
    #config.read("%s/gpspectrum/conf/%s.ini" % (homedir,fshconfig))
    config.read("%s/%s.ini" % (confdir,fshconfig))
    fstart = float(config.get("frequency","start"))
    fstop = float(config.get("frequency","stop"))

    freqcentral = (fstop+fstart)/2
    freqspan = (fstop-fstart)
    ##---------------------------
    cmd('REMOTE')
    #setcmd('MEAS,1') # Analyzer mode
    if reset == '1':
        cmd('PRESET\r')
        time.sleep(1)
    setcmd('FREQ,%s\r' % freqcentral)
    setcmd('SPAN,%s\r' % freqspan)
    setcmd('SWPTIME, %s\r' % (config.get("sweep","time")))
    setcmd('SWPCONT,%s\r' % (config.get("sweep","continous")))
    #cmd('INIT\r') #Initialize sweep
    #cmd('WAIT\r') #Wait for end of sweep
    setcmd('UNIT,%s\r' % (config.get("unit","unit")))
    setcmd('TRACEMODE,%s\r' % (config.get("trace","mode")))
    if config.get("trace","mode") == 1:
        setcmd('TRACEAVG,%s\r' % (config.get("trace","average")))
    setcmd('TRACEDET,%s\r' % (config.get("trace","detector")))
    #
    setcmd('RBW,%s\r' % (config.get("bandwidth","resolution")))
    setcmd('VBW,%s\r' % (config.get("bandwidth","video")))
    getcmd('TRACE\r')

def getresults(newlinechar):
    spectrum = fsh.readline()
    newlist = []
    for a in spectrum.split(','):
        b = a.split(newlinechar)
        if b != '' and b != ' ':
            newlist.append(b[len(b)-1])
    return newlist

"""
class FSH6mgr:
    def connect(self, fshport):
        self.fsh=serial.Serial()
        ##---DEFINING SERIAL PORT ---
        self.fsh.port=fshport
        self.fsh.baudrate=19200
        self.fsh.bytesize=8
        self.fsh.parity='N'
        self.fsh.stopbits=1
        self.fsh.timeout=1
        self.fsh.xonxoff=0
        self.fsh.rtscts=0
        ##---------------------------
        self.fsh.open()

    def close(self):
        self.fsh.write('CMD\r')
        self.fsh.write('LOCAL\r')
        self.fsh.close()

    # FSH6 Types of commands and handling different responses
    def getcmd(self,cmd):
        self.fsh.write('GET\r')
        #response
        self.fsh.write('%s' % cmd)
        #response
        return

    def setcmd(self,cmd):
        self.fsh.write('SET\r')
        #response
        self.fsh.write('%s' % cmd)
        #response
        return

    def cmd(self,cmd):
        self.fsh.write('CMD\r')
        #response
        self.fsh.write('%s\r' % cmd)
        #response
        return

    def setmeas( self, fshconfig, reset ):
        #Gpsmgr
        #Set instrument for specfic data.
        
        config = ConfigParser.ConfigParser()
        #config.read("%s/gpspectrum/conf/%s.ini" % (homedir,fshconfig))
        config.read("%s/%s.ini" % (confdir,fshconfig))
        fstart = float(config.get("frequency","start"))
        fstop = float(config.get("frequency","stop"))

        freqcentral = (fstop+fstart)/2
        freqspan = (fstop-fstart)
        ##---------------------------
        self.cmd('REMOTE')
        #self.setcmd('MEAS,1') # Analyzer mode
        if reset == '1':
            self.cmd('PRESET\r')
            time.sleep(1)
        self.setcmd('FREQ,%s\r' % freqcentral)
        self.setcmd('SPAN,%s\r' % freqspan)
        self.setcmd('SWPTIME, %s\r' % (config.get("sweep","time")))
        self.setcmd('SWPCONT,%s\r' % (config.get("sweep","continous")))
        #self.cmd('INIT\r') #Initialize sweep
        #self.cmd('WAIT\r') #Wait for end of sweep
        self.setcmd('UNIT,%s\r' % (config.get("unit","unit")))
        self.setcmd('TRACEMODE,%s\r' % (config.get("trace","mode")))
        if config.get("trace","mode") == 1:
            self.setcmd('TRACEAVG,%s\r' % (config.get("trace","average")))
        self.setcmd('TRACEDET,%s\r' % (config.get("trace","detector")))
        #
        self.setcmd('RBW,%s\r' % (config.get("bandwidth","resolution")))
        self.setcmd('VBW,%s\r' % (config.get("bandwidth","video")))
        self.getcmd('TRACE\r')

    def getresults(self, newlinechar):
        spectrum = self.fsh.readline()
        newlist = []
        for a in spectrum.split(','):
            b = a.split(newlinechar)
            if b != '' and b != ' ':
                newlist.append(b[len(b)-1])
        return newlist
"""
