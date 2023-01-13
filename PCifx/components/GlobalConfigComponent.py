from tkinter import *
from tkinter import ttk


class GlobalConfigComponent:

    def __init__(self, root):

        # Element declaration

        checkCD25Val = IntVar(value=0)
        checkCD50Val = IntVar(value=0)
        checkLkgVal = IntVar(value=0)

        checkCD25 = ttk.Checkbutton(
            root, text="25 fF Detector Capacitance", variable=checkCD25Val, onvalue=1, offvalue=0)
        checkCD50 = ttk.Checkbutton(
            root, text="50 fF Detector Capacitance", variable=checkCD50Val, onvalue=1, offvalue=0)
        checkLkg = ttk.Checkbutton(
            root, text="Leakage Current", variable=checkLkgVal, onvalue=1, offvalue=0)

        checkCD25.state(['!alternate'])
        checkCD50.state(['!alternate'])
        checkLkg.state(['!alternate'])

        # Positioning

        checkCD25.grid(column=1, row=0, sticky=(N, S, W))
        checkCD50.grid(column=1, row=1, sticky=(N, S, W))
        checkLkg.grid(column=1, row=2, sticky=(N, S, W))

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
