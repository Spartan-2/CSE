# Write a python function binarySearch() to read a sorted array and search for the key element. Display the appropriate messages

def binarySearch(arr,low,high,key):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binarySearch(arr,mid+1,high,key)
        if arr[mid] < key:
            return binarySearch(arr,low,mid -1,key)
    else :
        return -1

n = int(input("Enter the size of array "))

lst = [int(input()) for _ in range(n)]
key = int(input("Enter the key "))
ans = binarySearch(lst,0,len(lst)-1,key)
if ans != -1:
    print(f"The key {key} is present at {ans}")
else:
    print("Key is not present")