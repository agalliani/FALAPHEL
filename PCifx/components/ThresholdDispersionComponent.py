
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


class ThresholdDispersionComponent:

    def __init__(self, root):

        fig = plt.figure(figsize=(4, 2.5))
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.subplots_adjust(top=0.925,     # Further fix clipping of text in the figure
                            bottom=0.2,
                            left=0.2,
                            right=0.90,
                            hspace=0.2,
                            wspace=0.2)
        # Create a canvas widget to display the plot
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0, row=0, sticky=(N, S, E, W))

        fig2 = plt.figure(figsize=(4, 2.5))
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.subplots_adjust(top=0.925,     # Further fix clipping of text in the figure
                            bottom=0.2,
                            left=0.2,
                            right=0.90,
                            hspace=0.2,
                            wspace=0.2)
        # Create a canvas widget to display the plot
        canvas2 = FigureCanvasTkAgg(fig2, master=root)
        canvas2.get_tk_widget().grid(column=1, row=0, sticky=(N, S, E, W))
