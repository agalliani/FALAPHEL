from tkinter import *
from tkinter import ttk

from services.CommunicationService import CommunicationService


class GlobalConfigComponent:
    def __init__(self, root):
        self.communicationService = CommunicationService()

        self.checkCD25Val = IntVar(value=0)
        self.checkCD50Val = IntVar(value=0)
        self.checkLkgVal = IntVar(value=0)

        self.create_widgets(root)
        self.position_widgets(root)

    def create_widgets(self, root):
        self.checkCD25 = ttk.Checkbutton(
            root,
            text="25 fF Detector Capacitance",
            variable=self.checkCD25Val,
            command=lambda: self.communicationService.setCD25(
                self.checkCD25Val.get()),
            onvalue=1,
            offvalue=0)

        self.checkCD50 = ttk.Checkbutton(
            root,
            text="50 fF Detector Capacitance",
            variable=self.checkCD50Val,
            command=lambda: self.communicationService.setCD50(
                self.checkCD50Val.get()),
            onvalue=1,
            offvalue=0)

        self.checkLkg = ttk.Checkbutton(
            root,
            text="Leakage Current",
            variable=self.checkLkgVal,
            command=lambda: self.communicationService.setLeakage(
                self.checkLkgVal.get()),
            onvalue=1,
            offvalue=0)

        self.buttonFullScan = ttk.Button(
            root,
            text="Full Matrix Charge Scan",
            command=lambda: self.communicationService.printGlobalMatrixConfig())  # button

    def position_widgets(self, root):
        self.checkCD25.grid(column=0, row=0, sticky=(N, S, W), padx=5)
        self.checkCD50.grid(column=0, row=1, sticky=(N, S, W), padx=5)
        self.checkLkg.grid(column=0, row=2, sticky=(N, S, W), padx=5)
        self.buttonFullScan.grid(column=1, row=1, sticky=(E), padx=5)
