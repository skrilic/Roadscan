#! /usr/bin/python

__author__="skrilic"
__date__ ="$22.05.2010. 21:25:40$"

from datetime import *
import time
import serial
from optparse import OptionParser
#import biggles

import matplotlib.pyplot as plt
import numpy as np

import configparser
#from string import Template
import os

from devices.Gpsmgr import Gpsmgr as Gpsmgr
from devices.FSH6mgr import FSH6mgr as FSH6

homedir = os.getenv("HOME")


class ResFile:
    def open(self, dir, name, mode):
        self.file=open("%s/%s" % (dir,name),"%s" % mode)

    def append(self, string):
        self.file.write(string)

    def close(self):
        self.file.close()


class Getvar:
    def callexit(self, message_string):
        print(message_string)
        exit()

    def getvars(self):
        parser = OptionParser()
        parser.add_option("-p", "--fshport", type="string", dest="fshport",
                            help="On which PORT is FSH connected?", metavar="FSHPORT")

        parser.add_option("-g", "--gpsport", type="string", dest="gpsport",
                            help='On which PORT is GPS device connected? Type "off" for disabling GPS.', metavar="GPSPORT")

        parser.add_option("-d", "--directory", type="string", dest="dir",
                            help="create CSV files in the DIRECTORY", metavar="DIRECTORY")
      
        parser.add_option("-c", "--config", type="string", dest="config",
                          help="The name of the instrument configuration file to use", metavar="CONFIGURATION")

        parser.add_option("-t", "--time", type="string", dest="time",
                          help="How long does measurement take in seconds? (Default: 60 sec)", metavar="TIME")

        parser.add_option("-s", "--sleep", type="string", dest="sleep",
                          help="SECONDS betweens two consecutive measurements. (Default: 10 sec)", metavar="SECONDS")
        """
        parser.add_option("-q", "--sqlitedb", type="string", dest="sqldb",
                          help="The name of output SQLite database", metavar="SQLITEDB")
        """
        (options, args) = parser.parse_args()
        #
        if options.fshport:
            self.fshport = options.fshport
        else:
            self.callexit("The serial port is not defined!\r\
                    For usage, Please type: <program> --help")
        #
        if options.gpsport:
            self.gpsport = options.gpsport
        else:
            self.gpsport = 'usb:'
        #
        if options.dir:
            self.dirname = options.dir
        else:
            self.dirname = "default"
            print("Results are going to be stored at $HOME/gpspectrum/data directory")
            #self.callexit("There is not Input directory variable!\r\
            #        For usage, Please type: <program> --help")
        #
        if options.config:
            self.config = options.config
        else:
            self.config = 'bcfm'
        #
        if options.time:
            self.time = float(options.time)
        else:
            self.time = 60
        #
        if options.sleep:
            self.sleep = float(options.sleep)
        else:
            self.sleep = 10
        """
        if options.sqldb:
            sqlitedb = options.sqldb
        else:
            sqlitedb = 'none'
            print "No sqlitedb. Never mind for now, it is OK!"
            #callexit("There is not output SQLite database variable!\r\
            #        For usage, Please type: <program> --help")
        """
        # Remove previous output file if such exists...
        #if os.path.exists("%s" % ofile):
        #    os.remove("%s" % ofile)
        # Remove previous sqlite database if such exists ...
        #if os.path.exists("%s" % sqlitedb):
        #    os.remove("%s" % sqlitedb)
        #
        return { 'fshport':self.fshport, 'gpsport':self.gpsport,\
                 'dirname':self.dirname,\
                 'time': self.time, 'sleep':self.sleep,\
                 'config':self.config}

# def draw(datafile, graphfile, fstart, fstop, ymin, ymax, myposition, datetime):
#     """
#     Take data from CSV file column 0 and 1 and Draw the spectrum
#     :param datafile: This is bigless.tmp file
#     :param graphfile: Output spectrum Plot file
#     :param fstart: Start frequency
#     :param fstop: End/Stop frequency
#     :param ymin: Min magnitude value
#     :param ymax: Max magnitude value
#     :param myposition: GPS read out
#     :param datetime: Date time stamp for the spectrum at the GPS point
#     :return:
#     """
#     #
#     #Take data from CSV file column 0 and 1, Comments in the file started with #
#     x = biggles.read_column ( 0, datafile, float, "#" )
#     y = biggles.read_column ( 1, datafile, float, "#" )
#
#     g = biggles.FramedPlot()
#     g.xrange = fstart, fstop #ie. 863000000, 870000000 for RFID/SRD
#     g.yrange = (ymin - 5), (ymax + 5) #-100, -20
#     #pts = biggles.Points( x, y, type="filled circle", color = "red")
#     line = biggles.Curve(x, y, color = "blue")
#     #g.add( pts, line )
#     g.add( line )
#     g.xlabel = "Frequency [Hz]"
#     g.ylabel = "Magnitude [dBm]"
#     g.title = "Spectrum for the GPS: %s at Date and Time: %s" % (myposition, datetime)
#     g.frame.draw_grid = 1
#     #g.add( biggles.LineY(0, type='dot') )
#     #g.show()
#     #g.write_img( 1200, 400, "%s" % graphfile )
#     g.write_img( 900, 300, "%s" % graphfile )

def read_datafile(file_name):
    data = np.genfromtxt(file_name, delimiter=' ', skip_header=0, skip_footer=0, names=['x', 'y'])
    return data


def draw_pyplot(datafile, graphfile, myposition, datetime):
    data = read_datafile(datafile)
    plt.figure(1)
    plt.subplot(111)
    plt.title("Spectrum for the GPS: %s at Date and Time: %s" % (myposition, datetime))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dBm]")
    plt.grid(True)
    plt.plot(data['x'], data['y'], color='r', label='the data')
    #plt.show()
    plt.savefig(graphfile)


def latlong(port, type):
    if port == 'off':
        mylocation = "0.000000,0.000000"
    else:
        mygps = Gpsmgr()
        mygps.setport(port)
        mygps.setgpstype(type)
        try:
            mylocation=mygps.getpos()
        except:
            mylocation("0.000000,0.000000")
        #gpstime=mygps.getgpstime()
    return mylocation

def findpeaks(list):
    vmax0=float(list[0])
    vmin0=float(list[0])
    for v in list:
        if v != '':
            if float(v) > vmax0:
                vmax0 = float(v)
            if float(v) < vmin0:
                vmin0 = float(v)
    return {'ymax':vmax0, 'ymin':vmin0}

# TODO: Change DATE-TIME format to ISO GMT bigless
def dt():
    """
    Calling this function returns current Local Date and Time
    :return:
    """
    nowis=datetime.now()
    dtnow=nowis.strftime("%Y-%m-%d %H:%M:%S")
    return dtnow


def onestep(fshport,gpsport,csvdirname,imagedirname,allres,measlogfile,fshconfig,threshold):
    """
    Function creates log files for further analysis in a GPS position. For every GPS position
    this function is called to create log and picture specific for that point.
    """
    config = configparser.ConfigParser()
    config.read("conf/%s.ini" % (fshconfig))
    #
    fstart = float(config.get("frequency","start"))
    fstop = float(config.get("frequency","stop"))
    #
    varreset = config.get("repetition","reset")
    fsh6 = FSH6()
    fsh6.connect(fshport)
    fsh6.setmeas(fshconfig,varreset)
    # If Max-hold mode is required ...
    if config.get("trace","mode") == '2':
        cycle = float(config.get("repetition","cycle"))
        # In this mode preset results are in buffer, so first  clear it ... and do nothing with it.
        fsh6.getresults(newlinechar='\r')
        # Wait for new buffer ...
        time.sleep(cycle)
        results=fsh6.getresults(newlinechar='\r')
    # If Min-hold mode is required ...
    elif config.get("trace","mode") == '3':
        cycle = float(config.get("repetition","cycle"))
        # In this mode preset results are in buffer, so first  clear it ... and do nothing with it.
        fsh6.getresults()
        # Wait for new buffer ...
        time.sleep(cycle)
        results=fsh6.getresults(newlinechar='\r')
    else:
        results=fsh6.getresults(newlinechar='\r')
    fsh6.close()
    dattim = dt()
    
    #myposition = latlong('/dev/ttyUSB0','garmin')
    myposition = latlong(gpsport,'garmin')
    stepcount  = (len(results) - 1)
    filename_base = dattim.replace(':', '-').replace(' ','_')
    csvfile = "%s_%s.csv" % (myposition.replace(',','-').replace('.','_'),filename_base)
    pngfile = "%s.png" % filename_base
    #
    # First, make sure the file is created, or cleared if already exists...
    fileout = ResFile()
    fileout.open(csvdirname, csvfile, "w")
    fileout.close
    #
    # Open file with results for all GPS locations ...

    # And temporary file for Biggles graph ...
    bigglesin = ResFile()
    bigglesin.open(csvdirname,"biggles.tmp","w")
    bigglesin.close()
    # Then the file is ready for results gathering ...
    meas = ResFile()
    meas.open(csvdirname, csvfile, "a")
    bigglesin.open(csvdirname,"biggles.tmp","a")
    #
    #
    print("-------------------------")
    i = 1
    for rez in results:
        freq = fstart + (i-1)*(fstop - fstart)/stepcount
        #print "%i,%s,%s,%s,%s,%s" % (i,dattim,myposition,rez,csvfile,pngfile
        if rez != '' and rez != ' ':
            linefull = "%s,%s,%f,%f,%s,%s\r\n" % (dattim, myposition, float(freq), float(rez), csvfile, pngfile)
            line = "%i,%s,%s\r\n" % (i, freq, rez)
            bigglesline = "%s %s\r\n" % (freq, rez)
            #print line
            allres.append(linefull)
            meas.append(line)
            bigglesin.append(bigglesline)
        i = i+1
    meas.close()
    bigglesin.close()
    max_min=findpeaks(results)
    if (max_min['ymax'] - threshold) < 0:
        abovethreshold = 0
    else:
        abovethreshold = max_min['ymax'] - threshold
        measlogfile.append("%s,%s,%s,%s,%s\r\n" % (dattim, myposition, abovethreshold, csvfile, pngfile))

    time.sleep(1)
    # draw( "%s/biggles.tmp" % csvdirname, "%s/%s" % (imagedirname, pngfile),
    #       fstart, fstop, max_min['ymin'], max_min['ymax'],myposition, dattim )
    draw_pyplot("%s/biggles.tmp" % csvdirname, "%s/%s" % (imagedirname, pngfile), myposition, dattim)
    print("GPS position: %s" % myposition)
    print("Max. %s" % max_min['ymax'])
    print("Min. %s" % max_min['ymin'])
    print("-------------------------")


def meascontrol(dirmeas):
    variables = Getvar()
    vars = variables.getvars()
    if vars['dirname'] != 'default':
            dirname = vars['dirname']
    else:
            dirname = "%s/data" % dirmeas
    # Open up file with stored GPS points of measurement, date and time of measurements,
    # and names of files where measurements are stored
    datetimestring = dt().replace(':', '-').replace(' ','_')
    csvdirname = "%s/%s/csv" % (dirname,datetimestring)
    imagedirname = "%s/%s/image" % (dirname,datetimestring)
    os.makedirs(csvdirname)
    os.makedirs(imagedirname)
    #
    # Open up file for storing measured values for a GPS point ...
    measlogfile = ResFile()
    measlogfile.open(csvdirname, "measlog.csv", "a")
    # And write the table header ...
    measlogfile.append("datetime,latitude,longitude,abovethreshold,csvfile,pngfile\r\n")
    #
    # Open up file for storing all measured results from whole path (GPS locations)
    bigfile = ResFile()
    bigfile.open(csvdirname, "total.csv", "a")
    #First line is populated by names of columns
    bigfile.append("datetime,latitude,longitude,frequency,magnitude,csvfile,pngfile")
    #
    clearfsh = FSH6()
    clearfsh.connect(vars['fshport'])
    # Read output and do nothing...
    clearfsh.getresults(newlinechar='\r')
    clearfsh.close()
    #
    config = configparser.ConfigParser()
    print("Config file: ./conf/{}.ini".format(vars['config']))
    config.read("./conf/%s.ini" % (vars['config']))
    threshold = float(config.get("level","threshold"))
    #
    start = time.time()
    end = start
    while vars['time'] >= (end - start):
        onestep( vars['fshport'], vars['gpsport'], csvdirname, imagedirname, bigfile, measlogfile, vars['config'],threshold)
        time.sleep(vars['sleep'])
        end = time.time()
    bigfile.close()
    measlogfile.close()
    
    print("Measurement has completed ...")
    print("time:%s sec, step: %s sec, span: %s sec" % (vars['time'], vars['sleep'], (end - start)))


def dirhandling():
    if os.path.isdir("%s/gpspectrum/data" % homedir) != True:
        os.makedirs("%s/gpspectrum/data" % homedir)
    dirpath = "%s/gpspectrum" % homedir
    return dirpath

def main():
    #variables=Getvar()
    #vars=variables.getvars()
    #onestep( vars['fshport'], vars['gpsport'], vars['dirname'], vars['fstart'], vars['fstop'] )
    dirmeas = dirhandling()
    meascontrol(dirmeas)

if __name__ == "__main__":
    main()
