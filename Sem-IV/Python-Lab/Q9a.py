# Develop a python program read a dataset and perform the following using Pandas 
# a. Visualize the dataset using plot(). 
# b. Draw the Scatter plot for the dataset on any column. 
# c. Display the scatter plot with different colours. 
# d. Draw the Histogram for the dataset on any column


import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("Iris.csv")

iris.plot()
plt.show()

iris.plot(kind = 'scatter',x = 'PetalLengthCm',y ='SepalLengthCm')
plt.show()

x = iris['PetalLengthCm']
y = iris['SepalLengthCm']
a = iris['SepalLengthCm']
b = iris['PetalLengthCm']

plt.scatter(x,y,c='green')
plt.scatter(a,b,c='red')
plt.show()

iris['PetalWidthCm'].plot(kind ='hist')
plt.show()