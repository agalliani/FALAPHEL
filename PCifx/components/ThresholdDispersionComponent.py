
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import numpy as np



class ThresholdDispersionComponent:

    def __init__(self, root):
        fig = plt.figure(figsize=(4, 2.5))

        # generate some random data
        data = np.random.normal(loc=0, scale=1, size=1000)

        # plot the histogram
        plt.hist(data, bins=50, density=True, color='blue', alpha=0.5)

        #  compute the mean and standard deviation of the data
        mean = np.mean(data)
        std = np.std(data)

        #  create a x-axis for the plot
        x = np.linspace(min(data), max(data), 100)

        # plot the Gaussian distribution
        plt.plot(x, (1 / (std * np.sqrt(2 * np.pi))) *
                 np.exp(- (x - mean) ** 2 / (2 * std ** 2)),
                 color='red', lw=2)

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
         # generate some random data
        data = np.random.normal(loc=0, scale=1, size=1000)

        # plot the histogram
        plt.hist(data, bins=50, density=True, color='green', alpha=0.5)

        #  compute the mean and standard deviation of the data
        mean = np.mean(data)
        std = np.std(data)

        #  create a x-axis for the plot
        x = np.linspace(min(data), max(data), 100)

        # plot the Gaussian distribution
        plt.plot(x, (1 / (std * np.sqrt(2 * np.pi))) *
                 np.exp(- (x - mean) ** 2 / (2 * std ** 2)),
                 color='blue', lw=2)
        
        
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
