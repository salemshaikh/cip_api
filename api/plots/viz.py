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