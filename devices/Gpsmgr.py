import gpsbabel

__author__="slaven"


class Gpsmgr:
    """
    Handling gpsbabel command get_posn. This way it is possible to get latitude,
    longitude and gps time as well.
    """

    def setport(self,port):
        self.port = port

    def setgpstype(self, gpsType):
        self.gpsType = gpsType


    def getpos(self):
        gpsbbl=gpsbabel.GPSBabel()
        position=gpsbbl.getCurrentGpsLocation(self.port,self.gpsType)
        for element in position:
            elm=element.split(' ')
            if elm[0] == '<None':
                lat=elm[1].strip('"').strip('lat="')
                long=elm[2].strip('">').strip('lon="')
        return "%s,%s" % (lat,long) #by using gpsbabel

    def getgpstime(self):
        gpsbbl=gpsbabel.GPSBabel()
        position=gpsbbl.getCurrentGpsLocation(self.port,self.gpsType)
        for element in position:
            if element.find('<time>') != -1:
                datetime=element.strip('<time>').strip('</time>')
        return datetime #by using gpsbabel
