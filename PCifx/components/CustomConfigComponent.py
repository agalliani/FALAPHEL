from tkinter import *
from tkinter import ttk


class CustomConfigComponent:

    def __init__(self, root):
       # Elements declaration

        # Start pixel selection
        startPixelSelectionVal = StringVar(value="0")
        startPixelSelectionSpinbox = ttk.Spinbox(
            root, from_=0, to=29, textvariable=startPixelSelectionVal, wrap=True)
        startPixelSelectionLabel = Label(root, text="Start pixel range")

        # End pixel selection TODO: if single pixel scan enabled, then this deactivated
        endPixelSelectionVal = StringVar(value="0")
        endPixelSelectionSpinbox = ttk.Spinbox(
            root, from_=1, to=30, textvariable=endPixelSelectionVal, wrap=True)
        endPixelSelectionLabel = Label(root, text="End pixel range")

        # Boolean single pixel scan
        isSinglePixelVal = BooleanVar(value=False)
        isSinglePixelCheck = ttk.Checkbutton(
            root, text="Single pixel scan", onvalue=True, offvalue=False)
        isSinglePixelCheck.state(['!alternate'])

       # Positioning

        startPixelSelectionSpinbox.grid(column=0, row=0, padx=5, pady=5)
        startPixelSelectionLabel.grid(column=1, row=0, padx=5, pady=5)

        endPixelSelectionSpinbox.grid(column=0, row=1, padx=5, pady=5)
        endPixelSelectionLabel.grid(column=1, row=1, padx=5, pady=5)

        isSinglePixelCheck.grid(column=0, row=2, padx=5, pady=5)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
