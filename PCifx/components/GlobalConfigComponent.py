from tkinter import *
from tkinter import ttk


class GlobalConfigComponent:
    def __init__(self, root):
        self.checkCD25Val = IntVar(value=0)
        self.checkCD50Val = IntVar(value=0)
        self.checkLkgVal = IntVar(value=0)

        self.create_widgets(root)
        self.position_widgets(root)

    def create_widgets(self, root):
        self.checkCD25 = ttk.Checkbutton(
            root, text="25 fF Detector Capacitance", variable=self.checkCD25Val, onvalue=1, offvalue=0)
        self.checkCD50 = ttk.Checkbutton(
            root, text="50 fF Detector Capacitance", variable=self.checkCD50Val, onvalue=1, offvalue=0)
        self.checkLkg = ttk.Checkbutton(
            root, text="Leakage Current", variable=self.checkLkgVal, onvalue=1, offvalue=0)

        self.buttonFullScan = ttk.Button(
            root, text="Full Matrix Charge Scan")  # button

    def position_widgets(self, root):
        self.checkCD25.grid(column=0, row=0, sticky=(N, S, W), padx=5)
        self.checkCD50.grid(column=0, row=1, sticky=(N, S, W), padx=5)
        self.checkLkg.grid(column=0, row=2, sticky=(N, S, W), padx=5)
        self.buttonFullScan.grid(column=1, row=1, sticky=(E), padx=5)

