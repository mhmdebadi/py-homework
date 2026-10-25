import os
import numpy as np
from  scipy.stats import norm,kurtosis,bernoulli,binom,skew,expon,laplace,mode
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 2, 4]
z = ['A', 'B' , 'C', 'D', 'F']
a = [
    [10, 12, 14, 16, 18],
    [24, 26, 34, 45, 11],
    [41, 24, 39, 50, 44]
]

""" Plot_line / 1

def plot_line(x, y):

    plt.plot(x, y, color='red',linestyle='--')
    plt.title('Line Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


plot_line(x, y)

"""

""" SketcherPlotter / 2

class SketcherPlotter:
    #

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, color='blue', size=30):
        plt.figure(figsize=(8, 5))
        plt.scatter(self.x, self.y, color=color, s=size)
        plt.grid(True)
        plt.show()

    def add_labels(self, x_label, y_label, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)


plotter = SketcherPlotter(x, y)
plotter.plot(color='red', size=30)
plotter.add_labels('X', 'Y', 'Scatter Plot')

"""

""" Bar_plot / 3

class BaseChart:
    # z = categories , y = values

    def show(self):
        plt.show()

class BarChart(BaseChart):

    def __init__(self, z, y):
        self.z = z
        self.y = y

    def plot(self):
        plt.bar(self.z, self.y)
        plt.title('Bar Chart')
        plt.xlabel('z')
        plt.ylabel('y')
        self.show()



chart = BarChart(z, y)
chart.plot()

"""

""" Plot_histogram / 4

def plot_histogram(x, bins=10, color='green'):
    # x = data
    
    mean = np.mean(x)
    std = np.std(x)

    plt.hist(x, bins=bins, color=color)
    plt.axvline(mean, color='red', linestyle='--')
    plt.title(f'Div = {std}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

plot_histogram(x)

"""

""" Box_plot / 5

def plot_boxplot(a, labels=['G_A', 'G_B', 'G_C']):
    #a = array

    plt.figure(figsize=(8, 5))

    bp = plt.boxplot(
        a,
        tick_labels=labels, 
        patch_artist=True, 
        flierprops=dict(marker='o')
    )

    colors = ['red', 'green', 'blue']

    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set_facecolor(colors[i])

    plt.title('Box Plot G')
    plt.grid(True)
    plt.show()


plot_boxplot(a, labels=['G_A', 'G_B,', 'G_C'])

"""

