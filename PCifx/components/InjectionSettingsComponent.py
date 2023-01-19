from tkinter import *
from tkinter import ttk

from services.CommunicationService import CommunicationService


# It's a GUI component that allows the user to set the number of injections, the minimum charge, the
# maximum charge, and the number of steps.
class InjectionSettingsComponent:
    def setAll(self, event):
        self.communicationService.setNumInjection(self.injNumberSpinbox.get())
        self.communicationService.setQmin(self.minChargeSpinbox.get())
        self.communicationService.setQmax(self.maxChargeSpinbox.get())
        self.communicationService.setNumSteps(self.chargeStepSpinbox.get())
        self.communicationService.printInjSet() # to remove

    def __init__(self, root):
        self.communicationService = CommunicationService()

        # Element declaration

        # injections
        injNumberVal = StringVar(value=1)
        self.injNumberSpinbox = ttk.Spinbox(
            root,
            from_=1,
            to=1000,
            textvariable=injNumberVal,
            wrap=True,
            command=lambda: self.communicationService.setNumInjection(injNumberVal.get()))
        injNumberLabel = Label(root, text="Number of injections")
        self.injNumberSpinbox.bind(
            "<Return>", self.setAll)

        # Qmin
        minChargeVal = StringVar(value=1)
        self.minChargeSpinbox = ttk.Spinbox(
            root,
            from_=1,
            to=49000,
            textvariable=minChargeVal,
            wrap=True,
            command=lambda: self.communicationService.setQmin(minChargeVal.get()))
        self.minChargeSpinbox.bind(
            "<Return>", self.setAll)

        minChargeLabel = Label(
            root, text="Qin min - Start value of the charge scan - in electrons")

        # Qmax
        maxChargeVal = StringVar(value=2)
        self.maxChargeSpinbox = ttk.Spinbox(
            root,
            from_=2,
            to=50000,
            textvariable=maxChargeVal,
            wrap=True,
            command=lambda: self.communicationService.setQmax(maxChargeVal.get()))

        self.maxChargeSpinbox.bind(
            "<Return>", self.setAll)
        maxChargeLabel = Label(
            root, text="Qin max - End value of the charge scan - in electrons")

        # steps
        chargeStepVal = StringVar(value=1)
        self.chargeStepSpinbox = ttk.Spinbox(
            root,
            from_=1,
            to=1000,
            textvariable=chargeStepVal,
            wrap=True,
            command=lambda: self.communicationService.setNumSteps(chargeStepVal.get()))
        self.chargeStepSpinbox.bind(
            "<Return>", self.setAll)
        chargeStepLabel = Label(root, text="Number of steps")

        # Positioning

        self.injNumberSpinbox.grid(column=0, row=0, padx=5, pady=5)
        injNumberLabel.grid(column=1, row=0,  padx=5,
                            pady=2.5, sticky=(W))

        self.minChargeSpinbox.grid(column=0, row=1, padx=5, pady=5)
        minChargeLabel.grid(column=1, row=1,  padx=5,
                            pady=5, sticky=(W))

        self.maxChargeSpinbox.grid(column=0, row=2, padx=5, pady=5)
        maxChargeLabel.grid(column=1, row=2,  padx=5,
                            pady=5, sticky=(W))

        self.chargeStepSpinbox.grid(column=0, row=3, padx=5, pady=5)
        chargeStepLabel.grid(column=1, row=3,  padx=5,
                             pady=2.5, sticky=(W))
