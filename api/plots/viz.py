"""
Module for standard visualisation
"""
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#  Create base class with validation.
class BaseChart:
    def __init__(self, data, x, y=None):
        self.data = data
        self.x = x
        self.y = y
 
    def validate_data(self):
        if type(self.data) != pd.DataFrame:
            raise TypeError('Expected A Data Frame')


# Line Chart
 

class LineChart(BaseChart):

    def plotly_line(self):

        self.validate_data()

        fig = px.line(self.data, x=self.x, y=self.y)

        fig.show()

    def matplotlib_line(self):

        self.validate_data()

        plt.figure(figsize=(10, 5))

        plt.plot(self.data[self.x], self.data[self.y], marker='o')

        plt.title(f'Line Chart of {self.y} vs {self.x}')

        plt.xlabel(self.x)

        plt.ylabel(self.y)

        plt.grid(True)

        plt.show()
 
    def seaborn_line(self):

        self.validate_data()

        plt.figure(figsize=(10, 5))

        sns.lineplot(data=self.data, x=self.x, y=self.y)

        plt.title(f'Line Chart of {self.y} vs {self.x}')

        plt.xlabel(self.x)

        plt.ylabel(self.y)

        plt.grid(True)

        plt.show()


# Bar Chart
class bar_chart:
    """
    Object for creating bar charts using various plotting libraries.
    """
    
    def plotly_bar(self, data, x, y):
        fig = px.bar(data, x=x, y=y)
        fig.show()
    
    def matplotlib_bar(self, data, x, y):
        plt.figure(figsize=(10, 5))
        plt.bar(data[x], data[y])
        plt.title(f'Bar Chart of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def seaborn_bar(self, data, x, y):
        plt.figure(figsize=(10, 5))
        sns.barplot(data=data, x=x, y=y)
        plt.title(f'Bar Chart of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

# Scatter Plot
class scatter_plot:
    """
    Object for creating scatter plots using various plotting libraries.
    """
    
    def plotly_scatter(self, data, x, y):
        fig = px.scatter(data, x=x, y=y)
        fig.show()
    
    def matplotlib_scatter(self, data, x, y):
        plt.figure(figsize=(10, 5))
        plt.scatter(data[x], data[y])
        plt.title(f'Scatter Plot of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def seaborn_scatter(self, data, x, y):
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=data, x=x, y=y)
        plt.title(f'Scatter Plot of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

# Histogram
class histogram:
    """
    Object for creating histograms using various plotting libraries.
    """
    
    def plotly_histogram(self, data, x):
        fig = px.histogram(data, x=x)
        fig.show()
    
    def matplotlib_histogram(self, data, x):
        plt.figure(figsize=(10, 5))
        plt.hist(data[x], bins=10)
        plt.title(f'Histogram of {x}')
        plt.xlabel(x)
        plt.show()

    def seaborn_histogram(self, data, x):
        plt.figure(figsize=(10, 5))
        sns.histplot(data=data, x=x, bins=10)
        plt.title(f'Histogram of {x}')
        plt.xlabel(x)
        plt.show()


# Box Plot
class box_plot:
    """
    Object for creating box plots using various plotting libraries.
    """

    def plotly_box(self, data, x=None, y=None):
        """
        Plot a box plot using Plotly.

        Parameters:
        data: DataFrame.
        x: Name of the column to be used as categories (optional).
        y: Name of the column for the distribution.
        """
        fig = px.box(data, x=x, y=y)
        fig.show()

    def matplotlib_box(self, data, y, vert=True):
        """
        Plot a box plot using Matplotlib.

        Parameters:
        data: DataFrame.
        y: Name of the column for the distribution.
        vert: Whether to plot the boxes vertically or horizontally.
        """
        plt.figure(figsize=(10, 5))
        plt.boxplot(data[y], vert=vert)
        plt.title(f'Box Plot of {y}')
        if vert:
            plt.ylabel(y)
        else:
            plt.xlabel(y)
        plt.show()

    def seaborn_box(self, data, x=None, y=None):
        """
        Plot a box plot using Seaborn.

        Parameters:
        data: DataFrame.
        x: Name of the column to be used as categories (optional).
        y: Name of the column for the distribution.
        """
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=data, x=x, y=y)
        plt.title(f'Box Plot of {y}')
        plt.xlabel(x if x else '')
        plt.ylabel(y if y else '')
        plt.show()
