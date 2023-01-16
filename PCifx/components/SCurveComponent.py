
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


class SCurveComponent:

    def __init__(self, root):

        fig = plt.figure()
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        # Create a canvas widget to display the plot
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=3,
                                    rowspan=2, sticky=(N, S, E, W))
