# Develop a python program read a dataset and perform the following using Pandas 
# a. Display first 5 rows of the dataset. 
# b. Display last 5 rows of the dataset. 
# c. Display the information about the dataset. 
# d. Display the overview of the values of each column.
# e. Visualize the dataset using plot ().


import pandas as pd

iris = pd.read_csv("Iris.csv")

iris.head(5)

iris.tail(5)

iris.describe()

iris.info()

import matplotlib.pyplot as plt

iris.plot()
plt.show()

