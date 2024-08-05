# Write  a  python  program  to  utilize  NumPy  and  perform  the  following operations. 
# Read and display a 2D Array. 
# Display the array elements in the reverse order. 
# Display all the elements of principal diagonal elements. 
# Sort the 2D array in ascending and descending order

import numpy as np


row = int(input("Enter the number of rows "))
col = int(input("Enter the number of columns "))

print("Enter the array elements ")

list = [int(input()) for _ in range(row*col)]
arr = np.array(list).reshape(row,col)

print("The reshaped array/ matrix ")
print(arr)

print("Array in reverse order ")
print(arr[::-1,::-1])

print("Principal diagonal element ",np.diagonal(arr))

arr_asec = np.sort(arr,axis = None).reshape(arr.shape)
print("Ascending order ",arr_asec)

arr_desc = np.sort(arr,axis=None)[::-1].reshape(arr.shape)
print("Descending order ",arr_desc)
