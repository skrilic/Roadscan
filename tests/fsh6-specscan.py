from FSH6 import FSH6
import ConfigParser as configparser
from optparse import OptionParser
import time


# Read command line options
class Getvar:
    def callexit(self, message_string):
        print(message_string)
        exit()

    def getvars(self):
        parser = OptionParser()
        parser.add_option("-p", "--fshport", type="string", dest="fshport",
                          help="On which PORT is FSH connected?", metavar="FSHPORT")

        # parser.add_option("-g", "--gpsport", type="string", dest="gpsport",
        #                   help='On which PORT is GPS device connected? Type "off" for disabling GPS.',
        #                   metavar="GPSPORT")

        parser.add_option("-d", "--directory", type="string", dest="dir",
                          help="Measurement CSV and Plots files go in the DIRECTORY", metavar="DIRECTORY")

        parser.add_option("-c", "--config", type="string", dest="config",
                          help="Full path to the name of instrument configuration file to use", metavar="CONFIGURATION")

        parser.add_option("-t", "--time", type="string", dest="time",
                          help="How long should measurement last? (Default: 60 sec)", metavar="TIME")

        parser.add_option("-s", "--sleep", type="string", dest="sleep",
                          help="SECONDS betweens two consecutive measurements. (Default: 10 sec)", metavar="SECONDS")

        # parser.add_option("-q", "--sqlitedb", type="string", dest="sqldb",
        #                   help="The name of output SQLite database", metavar="SQLITEDB")

        (options, args) = parser.parse_args()
        #
        if options.fshport:
            self.fshport = options.fshport
        else:
            self.callexit("The serial port is not defined!\r\
                    For usage, Please type: <program> --help")
        #
        # if options.gpsport:
        #     self.gpsport = options.gpsport
        # else:
        #     self.gpsport = 'usb:'
        #
        if options.dir:
            self.dirname = options.dir
        else:
            self.dirname = "default"
            # print("Results are going to be stored at $HOME/gpspectrum/data directory")
            self.callexit("The data otput directory variable missing!\r\
                   For usage, Please type: <program> --help")
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
        #
        # if options.sqldb:
        #     sqlitedb = options.sqldb
        # else:
        #     sqlitedb = 'none'
        #     print "No sqlitedb. Never mind for now, it is OK!"
        #     #callexit("There is not output SQLite database variable!\r\
        #     #        For usage, Please type: <program> --help")
        #
        # Remove previous output file if such exists...
        # if os.path.exists("%s" % ofile):
        #    os.remove("%s" % ofile)
        # Remove previous sqlite database if such exists ...
        # if os.path.exists("%s" % sqlitedb):
        #    os.remove("%s" % sqlitedb)
        #
        return {'fshport': self.fshport, 'gpsport': self.gpsport, \
                'dirname': self.dirname, \
                'time': self.time, 'sleep': self.sleep, \
                'config': self.config}


# Connect FSH6
def connect(fsh6port):
    """
    Open up port and connect to the instrument
    :param fsh6port: Port where the instrument is connected
    :return: Return Instrument object
    """
    fsh6 = FSH6(fsh6port)
    return fsh6


# Initialize measurement
def init_measurement(port, measurement_config_file, reset):
    """
    Set instrument for specfic data.
    """
    fsh6 = connect(port)
    config = configparser.ConfigParser()
    print("Config file is {}.ini".format(measurement_config_file))
    config.read("{}.ini".format(measurement_config_file))

    measurement_config = {
        'fstart': float(config.get("frequency", "start")),
        'fstop': float(config.get("frequency", "stop")),
        'sweep_time': config.get("sweep", "time"),
        'sweep_continous': config.get("sweep", "continous"),
        'measurement_unit': config.get("unit", "unit"),
        'trace_mode': config.get("trace", "mode"),
        'trace_type': config.get("trace", "average"),
        'trace_detector': config.get("trace", "detector"),
        'rbw': config.get("bandwidth", "resolution"),
        'vbw': config.get("bandwidth", "video")
    }
    fsh6.setmeas(measurement_config, reset)
    return fsh6


# Perform measurement
def measurement(fsh6):
    results = fsh6.getresults(newlinechar='\r')
    return results


def main():
    vars = Getvar().getvars()

    print("Config file: {}.ini".format(vars['config']))
    port = vars['fshport']
    measurement_config_file = "{}.ini".format(vars['config'])
    #
    fsh6 = init_measurement(port, measurement_config_file, 1)
    counter = 0
    start = time.time()
    end = start
    while vars['time'] >= (end - start):
        results = measurement(fsh6)
        print(results)
        # Draw spectrum
        time.sleep(vars['sleep'])
        end = time.time()
        counter += 1

    print("Measurement has completed ...")
    print("time:%s sec, step: %s sec, span: %s sec" % (vars['time'], vars['sleep'], (end - start)))


