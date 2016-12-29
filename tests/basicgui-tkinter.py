from Tkinter import *
import tkFileDialog
import tkMessageBox
import ttk


class RoadscanGui:

    def __init__(self, master):
        master.title("Roadscan")
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', foreground='red', background='black')
        self.style.configure('TEntry', foreground='marineblue', background='cornsilk', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        # CREATE FRAME WITH MEASUREMENT CONTROLS#
        self.frame_control = ttk.Frame(master, relief=GROOVE)
        self.frame_control.pack()


        # WIDGETS DEFINITION
        self.gpslbl = ttk.Label(self.frame_control, text="GPS Port", font="Arial 11")
        self.gpsport = ttk.Entry(self.frame_control, width=10)

        self.fsh6lbl = ttk.Label(self.frame_control, text="FSH6 Port", font="Arial 11")
        self.fsh6port = ttk.Entry(self.frame_control, width=10)

        self.cfg = ttk.Button(self.frame_control, text="Select configuration", command=self.config_file)

        self.audioon = BooleanVar()
        self.audio = ttk.Checkbutton(self.frame_control, text="Audio", variable=self.audioon, onvalue=True)

        self.detect = ttk.Button(self.frame_control, text="Detect GPS and FSH6", style="TButton")


        # PUT WIDGETS IN THE FRAME
        self.gpslbl.grid(column=0, row=0)
        self.fsh6lbl.grid(column=1, row=0)

        self.gpsport.grid(column=0, row=1)
        self.fsh6port.grid(column=1, row=1)

        self.cfg.grid(column=0, row=2)
        self.audio.grid(column=1, row=2)

        self.detect.grid(column=0, row=3)


        #######################################
        # CREATE FRAME WITH MEASUREMENT STATUS#
        self.frame_status = ttk.Frame(master)
        self.frame_status.pack()

        self.latlnglbl = ttk.Label(self.frame_status, text="GPS position:", font="Arial 11")
        self.latlng = ttk.Entry(self.frame_status, state="readonly")
        self.magnlbl = ttk.Label(self.frame_status, text="Magnitude:", font="Arial 11")
        self.magn = ttk.Entry(self.frame_status, state="readonly")
        self.start = ttk.Button(self.frame_status, text="Start")
        self.progbar = ttk.Progressbar(self.frame_status, orient=HORIZONTAL, mode="indeterminate")

        self.latlnglbl.grid(row=0, column=0, padx=0, sticky=E)
        self.latlng.grid(row=0, column=1, sticky=W)
        self.magnlbl.grid(row=1, column=0)
        self.magn.grid(row=1, column=1)
        self.start.grid(row=2, column=1, sticky=W+E)
        self.progbar.grid(row=3, column=0, columnspan=2, sticky=W+E)

        # WORK IN PROGRESS ...


    def config_file(self):
        fname = tkFileDialog.askopenfilename(filetypes=(("Configuration file", "*.ini"), ("Text files", "*.txt")))
        if fname:
            try:
                print("""here it comes: self.settings["config"].set(fname)""")
            except:  # <- naked except is a bad idea
                tkMessageBox.showerror("Open Configuration File", "Failed to read file\n'%s'" % fname)
            return

    def detect_ports(self):
        """
        Find USB ports Where are GPS and FSH Connected
        :return:
        """
        return

    def start_measurement(self):
        return

    def stop_measurement(self):
        return

def main():
    root = Tk()
    roadscan = RoadscanGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()


