from tkinter import *
from tkinter import ttk

from GlobalConfigComponent import GlobalConfigComponent
from InjectionSettingsComponent import InjectionSettingsComponent
from CustomConfigComponent import CustomConfigComponent
from SystemSettingsComponent import SystemSettingsComponent
from SCurveComponent import SCurveComponent


class MasterView:

    def __init__(self, root):

        # main frame
        container = ttk. LabelFrame(
            root, text="Container", width=200, height=100)

        container.grid(column=0, row=0, sticky=(
            N, S, E, W), padx=5, pady=5)

        container.columnconfigure(0, weight=0)
        container.columnconfigure(1, weight=0)
        container.columnconfigure(2, weight=0)
        container.columnconfigure(3, weight=2)
        container.columnconfigure(4, weight=2)
        container.columnconfigure(5, weight=2)

        self.build_left_section(container)
        self.build_right_section(container)

    def build_right_section(self, container):
        rightFrame = ttk.LabelFrame(
            container, borderwidth=5, text="rightFrame", width=200, height=100)

        sCurveFrame = ttk.LabelFrame(
            rightFrame, borderwidth=5, text="S Curve", width=200, height=100)

        # positioning

        rightFrame.grid(column=3, row=0, columnspan=3,
                        rowspan=2, sticky=(N, S, E, W), padx=8)
        rightFrame.columnconfigure(0, weight=2)
        rightFrame.columnconfigure(1, weight=2)
        rightFrame.columnconfigure(2, weight=2)

        sCurveFrame.grid(column=0, row=0, columnspan=3,
                         rowspan=2, sticky=(N, S, E, W), padx=8)

    def build_left_section(self, container):

       # Left column elements
        leftFrame = ttk. LabelFrame(
            container, borderwidth=5, text="leftFrame", width=200, height=100)

        systemSettingsFrame = ttk.LabelFrame(
            leftFrame, borderwidth=5, text="System Settings", width=200, height=100)  # system settings

        SystemSettingsComponent(systemSettingsFrame)

        injectionSettingsFrame = ttk. LabelFrame(
            leftFrame, borderwidth=5, text="Injection Settings", width=200, height=100)  # injection settings

        InjectionSettingsComponent(injectionSettingsFrame)

        globalConfigFrame = ttk. LabelFrame(
            leftFrame, borderwidth=5, text="Global Matrix Config", width=200, height=100)  # global config

        GlobalConfigComponent(globalConfigFrame)

        customConfigFrame = ttk.LabelFrame(
            leftFrame, borderwidth=5, text="Custom Charge Scan Settings", width=200, height=100)  # custom

        CustomConfigComponent(customConfigFrame)

        #####################
        # Positioning

        leftFrame.grid(column=0, row=0, columnspan=3,
                       rowspan=2, sticky=(N, S, E, W), padx=8)
        systemSettingsFrame.grid(
            column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)
        injectionSettingsFrame.grid(
            column=0, row=2, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)
        globalConfigFrame.grid(
            column=0, row=4, columnspan=3, rowspan=2, sticky=(N, S, E, W),  pady=5)

        customConfigFrame.grid(column=0, row=6, columnspan=3,
                               rowspan=2, sticky=(N, S, E, W),  pady=5)
