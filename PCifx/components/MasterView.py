from tkinter import *
from tkinter import ttk

from GlobalConfigComponent import GlobalConfigComponent
from InjectionSettingsComponent import InjectionSettingsComponent
from CustomConfigComponent import CustomConfigComponent
from SystemSettingsComponent import SystemSettingsComponent


class MasterView:

    def __init__(self, root):

       # main frame
        container = ttk. LabelFrame(
            root, text="Container",  padding=(3, 3, 12, 12))

       # Left column elements

        leftFrame = ttk. LabelFrame(
            container, borderwidth=5, text="leftFrame", width=200, height=100)

        injectionSettingsFrame = ttk. LabelFrame(
            leftFrame, borderwidth=5, text="Injection Settings", width=200, height=100)
        InjectionSettingsComponent(injectionSettingsFrame)

        globalConfigFrame = ttk. LabelFrame(
            leftFrame, borderwidth=5, text="Global Matrix Config", width=200, height=100)
        GlobalConfigComponent(globalConfigFrame)

        buttonFullScan = ttk.Button(leftFrame, text="Full Matrix Charge Scan")

        # Right column elements
        rightFrame = ttk. LabelFrame(
            container, borderwidth=5, text="rightFrame", width=200, height=100)

        systemSettingsFrame = ttk.LabelFrame(
            rightFrame, borderwidth=5, text="System Settings", width=200, height=100)

        SystemSettingsComponent(systemSettingsFrame)

        customConfigFrame = ttk.LabelFrame(
            rightFrame, borderwidth=5, text="Custom Charge Scan Settings", width=200, height=100)

        CustomConfigComponent(customConfigFrame)

        buttonCustomScan = ttk.Button(rightFrame, text="Custom Charge Scan")

       # Positioning
        container.grid(column=0, row=0, sticky=(N, S, E, W))

        # left
        leftFrame.grid(column=0, row=0, columnspan=3,
                       rowspan=2, sticky=(N, S, E, W), padx=8)
        injectionSettingsFrame.grid(
            column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)
        globalConfigFrame.grid(
            column=0, row=2, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)

        buttonFullScan.grid(column=1, row=4)

        # right

        rightFrame.grid(column=3, row=0, columnspan=3,
                        rowspan=2, sticky=(N, S, E, W))
        systemSettingsFrame.grid(
            column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)
        customConfigFrame.grid(column=0, row=2, columnspan=3,
                               rowspan=2, sticky=(N, S, E, W),  pady=5)
        buttonCustomScan.grid(column=1, row=4)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(2, weight=1)
        container.columnconfigure(3, weight=1)
        container.columnconfigure(4, weight=1)
        container.columnconfigure(5, weight=1)
        container.rowconfigure(1, weight=1)

        leftFrame.columnconfigure(0, weight=1)
        leftFrame.columnconfigure(1, weight=1)
        leftFrame.columnconfigure(2, weight=1)

        leftFrame.rowconfigure(1, weight=2)
        leftFrame.rowconfigure(2, weight=2)
        leftFrame.rowconfigure(3, weight=1)

        rightFrame.columnconfigure(0, weight=1)
        rightFrame.columnconfigure(1, weight=1)
        rightFrame.columnconfigure(2, weight=1)

        rightFrame.rowconfigure(1, weight=2)
        rightFrame.rowconfigure(2, weight=2)
