import matplotlib.pyplot as plt
from scipy.special import erf
from numpy.lib.scimath import sqrt
from scipy.optimize import curve_fit

import os

import numpy as np
import datetime


from services.CommunicationService import CommunicationService


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AnalysisService(metaclass=Singleton):
    def __init__(self):
        self.communicationService = CommunicationService()

        self.x_erf = [[300, 400, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1300, 1400, 1500, 1600],
                      [400, 500, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1300, 1400, 1500, 1600]]
        self.y_erf = [
            [0, 0, 0, 0, 9.38e-3, 3.82e-2, 4.67e-2, 2.12e-1, 3.59e-1, 4.76e-1,
             6.29e-1, 7.35e-1, 8.46e-1, 9.55e-1, 9.86e-1, 1, 1, 1, 1],
            [0, 0, 0, 0, 9.38e-3, 3.82e-2, 4.67e-2, 2.12e-1, 3.59e-1, 4.76e-1,
             6.29e-1, 7.35e-1, 8.46e-1, 9.55e-1, 9.86e-1, 1, 1, 1, 1]
        ]
        print("CIAO")

    def myERF(self, x, mu, sigma):
        return 0.5*(1 + erf((x-mu)/(sigma*sqrt(2))))

    def getERFplot(self, index):
        plt.close()  # clears previous plot

        guess = [800, 100]
        parameters, covariance = curve_fit(
            self.myERF, self.x_erf[index], self.y_erf[index], p0=guess)

        fit_A = parameters[0]
        fit_B = parameters[1]
        print("Mean: ", fit_A)
        print("\nDispersion:", fit_B)
        print("\nCovariance matrix:\n", covariance)
        print("\nstd: ", np.sqrt(np.diag(covariance)))

        fig, ax = plt.subplots(1, 1, figsize=(8, 2.5))
        fit_x = np.arange(
            np.min(self.x_erf[index]), np.max(self.x_erf[index]), 10)
        fit_y = self.myERF(fit_x, fit_A, fit_B)
        plt.plot(self.x_erf[index], self.y_erf[index],
                 'o', label='data', color='blue')
        plt.plot(fit_x, fit_y, '-.', label='fit', color='red')
        ax.annotate("Threshold="+str(round(fit_A, 2))+" e-\nDispersion="+str(round(fit_B, 2))+" e-",  # text
                    (1005, 0.25),  # point
                    textcoords="offset points",  # positioning
                    xytext=(0, 0),  # txt distance from the point
                    ha='left')  # horizontal alignment

        plt.xlabel('Input charge (electrons)')
        plt.ylabel('Probability')

        plt.grid()
        plt.legend()

        plt.subplots_adjust(top=0.925,     # Further fix clipping of text in the figure
                            bottom=0.2,
                            left=0.1,
                            right=0.90,
                            hspace=0.3,
                            wspace=0.2)
        """
        ct = datetime.datetime.now()

        my_file = 'scurve-'+str(index)+'.png'

        fig.savefig(os.path.join(
            self.communicationService.directory+''+str(ct)+'/', my_file))
       """
        return fig
