from tkinter import *
from tkinter import ttk


class InjectionSettingsComponent:

    def __init__(self, root):

        # Element declaration

        # injections
        injNumberVal = StringVar(value=1)
        injNumberSpinbox = ttk.Spinbox(
            root, from_=1, to=1000, textvariable=injNumberVal, wrap=True)
        injNumberLabel = Label(root, text="Number of injections")

        # Qmin
        minChargeVal = StringVar(value=1)
        minChargeSpinbox = ttk.Spinbox(
            root, from_=1, to=49000, textvariable=minChargeVal, wrap=True)
        minChargeLabel = Label(
            root, text="Qin min - Start value of the charge scan - in electrons")

        # Qmax
        maxChargeVal = StringVar(value=1)
        maxChargeSpinbox = ttk.Spinbox(
            root, from_=2, to=50000, textvariable=maxChargeVal, wrap=True)
        maxChargeLabel = Label(
            root, text="Qin max - End value of the charge scan - in electrons")

        # steps
        chargeStepVal = StringVar(value=1)
        chargeStepSpinbox = ttk.Spinbox(
            root, from_=1, to=1000, textvariable=chargeStepVal, wrap=True)
        chargeStepLabel = Label(root, text="Number of steps")

        # Positioning

        injNumberSpinbox.grid(column=0, row=0, padx=5, pady=5)
        injNumberLabel.grid(column=1, row=0,  padx=5, pady=2.5, sticky=(W))

        minChargeSpinbox.grid(column=0, row=1, padx=5, pady=5)
        minChargeLabel.grid(column=1, row=1,  padx=5, pady=5, sticky=(W))

        maxChargeSpinbox.grid(column=0, row=2, padx=5, pady=5)
        maxChargeLabel.grid(column=1, row=2,  padx=5, pady=5, sticky=(W))

        chargeStepSpinbox.grid(column=0, row=3, padx=5, pady=5)
        chargeStepLabel.grid(column=1, row=3,  padx=5, pady=2.5, sticky=(W))

 