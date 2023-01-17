
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


class SCurveComponent:

    def __init__(self, root):

        fig = plt.figure(figsize=(8, 2.5))
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.subplots_adjust(top=0.925,     # Further fix clipping of text in the figure
                            bottom=0.2,
                            left=0.1,
                            right=0.90,
                            hspace=0.3,
                            wspace=0.2)

        # Create a canvas widget to display the plot
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0, row=1, sticky=(N, S, E, W))

        # injections
        pixelCurveVal = StringVar(value=1)
        pixelCurveSpinbox = ttk.Spinbox(
            root, from_=1, to=1000, textvariable=pixelCurveVal, wrap=True)
        pixelCurveLabel = Label(root, text="Selected pixel curve")

        pixelCurveSpinbox.grid(column=0, row=0, padx=5, pady=5,  sticky=(E))
        pixelCurveLabel.grid(column=0, row=0,  padx=(
            5, 150), pady=2.5, sticky=(E))
