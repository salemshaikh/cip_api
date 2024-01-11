"""
Module for standard visualisation
"""
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Line Chart

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Line Chart
class line_chart:
    """
    Object for creating line charts using various plotting libraries.
    """
    
    def plotly_line(self, data, x, y):
        """
        Plot a line chart using Plotly.
        
        Parameters:
        data: DataFrame.
        x: Name of the column to be used as x-axis.
        y: Name of the column to be used as y-axis.
        """
        fig = px.line(data, x=x, y=y)
        fig.show()
    
    def matplotlib_line(self, data, x, y):
        """
        Plot a line chart using Matplotlib.
        
        Parameters:
        data: DataFrame.
        x: Name of the column to be used as x-axis.
        y: Name of the column to be used as y-axis.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(data[x], data[y], marker='o')
        plt.title(f'Line Chart of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid(True)
        plt.show()

    def seaborn_line(self, data, x, y):
        """
        Plot a line chart using Seaborn.
        
        Parameters:
        data: DataFrame.
        x: Name of the column to be used as x-axis.
        y: Name of the column to be used as y-axis.
        """
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=data, x=x, y=y)
        plt.title(f'Line Chart of {y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid(True)
        plt.show()
