
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

from services.AnalysisService import AnalysisService


class SCurveComponent:

    def __init__(self, root):

        self.analysisService = AnalysisService()

        self.switchPlot(root, 0)

        # injections
        self.pixelCurveVal = IntVar(value=1)
        self.pixelCurveSpinbox = ttk.Spinbox(
            root,
            from_=0,
            to=len(self.analysisService.x_erf)-1,
            textvariable=self.pixelCurveVal,
            command=lambda: self.switchPlot(root, self.pixelCurveVal.get()),
            wrap=True)

        self.pixelCurveLabel = Label(root, text="Selected pixel curve")

        self.pixelCurveSpinbox.grid(
            column=0, row=0, padx=5, pady=5,  sticky=(E))
        self.pixelCurveLabel.grid(column=0, row=0,  padx=(
            5, 150), pady=2.5, sticky=(E))

    def switchPlot(self, root, index):
        self.fig = self.analysisService.getERFplot(index)

        # Create a canvas widget to display the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(column=0, row=1, sticky=(N, S, E, W))
