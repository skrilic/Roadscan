# -*- coding: utf-8 -*-

__author__="slaven"
#__date__ ="$28.05.2010. 10:51:58$"

from PySide import QtCore, QtGui
import os, sys
import maplayerDesign
import time
import ConfigParser
from string import Template

tmplvar=""
tmplplacemark= "templates/kmlbody.xml"
config = ConfigParser.ConfigParser()
config.read("conf/kml.ini")
ptcsv = config.get("webroot","csv")
ptimg = config.get("webroot","image")


class KmlGeneratorWindow(QtGui.QWidget, maplayerDesign.Ui_FormKml):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.toolButton_input.clicked.connect(self.open_file)
        self.toolButton_output.clicked.connect(self.save_file)
        self.pushButton_OK.clicked.connect(self.generate_kml)
        self.pushButton_Cancel.clicked.connect(self.close_widget)


    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File', 'measlog.csv' ,"Log files (*.csv)")
        self.lineEdit_input.setText(name[0])
        # Reset ProgressBar
        if self.progressBar.value != 0:
            self.progressBar.setValue = 0

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', "KML file (*.kml)")
        self.lineEdit_output.setText(name[0])

    def generate_kml(self):
        if (self.lineEdit_input.text() == "" or self.lineEdit_output.text() == ""):
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("You must select input and the output file!")
            msg.exec_()
        else:
            kml_out = KmlGenerator(self.lineEdit_input.text(), self.lineEdit_output.text())
            if kml_out.kml_generator():
                msg = QtGui.QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Program finished.")


    def close_widget(self):
        choice = QtGui.QMessageBox.question(self, "Close the Widget",
                                            "Really want to exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


class KmlGenerator:
    def __init__(self, csv_file, kml_file):
        self.csv_file = csv_file
        self.kml_file = kml_file

    def file2string(self, filein):
        """
        Function gets name of input file with complete path and returns string populated with
        content of the file.
        """
        stringout = ""
        stringin = open(filein, "r")
        for line in stringin:
            stringout = stringout + line
        return stringout

    def kml_generator(self):
        tmpldir = "templates"

        name_in = self.csv_file
        name_out = self.kml_file

        # First remove remaining KML file ...
        if os.path.isfile(name_out) == True:
            os.remove(name_out)

        kmlfile = open(name_out, "a")
        logobject = open(name_in, "r")
        header = open("%s/kmlheader.xml" % tmpldir, "r")
        footer = open("%s/kmlfooter.xml" % tmpldir, "r")
        # Write header of KML file
        for line in header:
            kmlfile.write(line)
        # Now, it is time to add tessallation.
        #tsltbody=open("%s/kmltessellatebody.xml" % tmpldir,"r")
        tsltbody="%s/kmltessellatebody.xml" % tmpldir
        # Create coords_values
        cooval = ""
        for logrow in logobject:
          elm = logrow.split(',')
          # Skip line with table header (column name), comments and empty new lines
          if elm[0] != 'datetime' and elm[0].strip()[0] != '#' and elm[0].strip() != '':
              cooval = cooval + "%s,%s,%s\r\n" % (elm[2],elm[1],elm[3])
              #print(cooval)
        string_tsltbody = self.file2string(tsltbody)
        kmlfile.write(Template(string_tsltbody).substitute(style="redLineOrangePoly",coords_values=cooval)) # Style could be: yellowLineGreenPoly or redLineOrangePoly, for now.
        #
        #measlogfile must be opened again for Points definitions.
        logobject.close()
        #
        logobject = open(name_in,"r")
        i = 1
        for logrow in logobject:
            elm = logrow.split(',')
            latit = elm[1]
            long = elm[2]
            coordinates = "%s,%s" %(long,latit)
            if elm[0] != 'datetime':
                description = elm[0] #Date and Time
                csvfile = elm[4]
                pngfile = elm[5]
                placemark = Template(self.file2string(tmplplacemark)).substitute(pathtocsv=ptcsv, pathtoimage=ptimg, name=i, coords=coordinates, desc=description, csv=csvfile, spectrum=pngfile)
                kmlfile.write(placemark)
                i=i+1
        #At last, write footer of KML file and then, close it.
        for line in footer:
            kmlfile.write(line)
        kmlfile.close()
        logobject.close()
        return True


def main():
    app = QtGui.QApplication(sys.argv)
    form = KmlGeneratorWindow()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
