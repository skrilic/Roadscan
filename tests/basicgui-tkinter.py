from Tkinter import *
import tkFileDialog
import tkMessageBox
import ttk


class MainControls(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Controls")
        # CONTAINERS
        # content = ttk.Frame(root)
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.grid(sticky=W+E+N+S)

        # WIDGETS DEFINITION
        self.gpslbl = ttk.Label(self, text="GPS Port")
        self.gpsport = ttk.Entry(self, width=10)

        self.fsh6lbl = ttk.Label(self, text="FSH6 Port")
        self.fsh6port = ttk.Entry(self, width=10)

        self.cfg = ttk.Button(self, text="Select configuration", command=self.config_file)

        self.audioon = BooleanVar()
        self.audio = ttk.Checkbutton(self, text="Audio ON", variable=self.audioon, onvalue=True)

        self.detect = ttk.Button(self, text="Detect GPS and FSH6")
        self.start = ttk.Button(self, text="Start")

        self.progbar = ttk.Progressbar(self, orient=HORIZONTAL, mode="indeterminate")

        # PUT WIDGETS IN THE FRAME

        self.gpslbl.grid(column=0, row=0)
        self.fsh6lbl.grid(column=1, row=0)

        self.gpsport.grid(column=0, row=1)
        self.fsh6port.grid(column=1, row=1)

        self.cfg.grid(column=0, row=2)
        self.audio.grid(column=1, row=2)

        self.detect.grid(column=0, row=3)
        self.start.grid(column=1, row=3)

        self.progbar.grid(column=0, row=4, columnspan=2, sticky=W+E)

    def config_file(self):
        fname = tkFileDialog.askopenfilename(filetypes=(("Configuration file", "*.ini"), ("Text files", "*.txt")))
        if fname:
            try:
                print("""here it comes: self.settings["config"].set(fname)""")
            except:  # <- naked except is a bad idea
                tkMessageBox.showerror("Open Configuration File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
    MainControls().mainloop()

