# Write  a  python  program  to  create  a  tuple  and  perform  the  following operations    
# Adding an items 
# Displaying the length of the tuple 
# Checking for an item in the tuple 
# Accessing an items

tup = tuple()
n = int(input("Enter the size of tuple "))

for i in range(n):
    item = int(input(f"Enter element {i+1} :"))
    tup += (item,)

print(f"The length of the tuple is {len(tup)}")

key = int(input("enter the element to be checked "))

if key in tup:
    print(f"The key {key} is present tuple")
else :
    print("not present")

index = int(input("Enter the index which you have to access "))
if index >= len(tup):
    print("Index out of bounds ")
else:
    print(f"The element present at {index} is {tup[index]}")


