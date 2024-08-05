# Develop a python program to read 20 random numbers. Display all the odd numbers from this list which are of length 2 and 4

print("Enter 20 random numbers ")
nums = [int(input()) for _ in range(20)]
odd_nums = [num for num in nums if num%2 == 1 ]
len2and4 = [num for num in odd_nums if len(str(num)) in [2,4]]
print(len(len2and4))
print(len2and4)