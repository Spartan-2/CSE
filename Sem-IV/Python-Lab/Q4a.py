# Write a python program to initialize a dictionary of usernames and passwords associated with it.  
# passwd={‘rahul’: ‘genius’, ‘kumar’: ‘smart’, ‘ankita’: ‘intelligent’} 
# Define the following functions: 
# a) To print all the items in the dictionary. 
# b) To print all the keys in the dictionary. 
# c) To print all the values in the dictionary. 
# d) To get the passwords of users. For example, passwd[‘rahul’]= genius 
# e) Change the password of a particular user. For example, passwd[‘ankita’]=‘brilliant’

dict1 = {'Rahul' : 'genius',
        'kumar': 'smart',
        'ankita':'intelligent'}

print(dict1.items())
print(dict1.keys())
print(dict1.values())
n = input("Enter whose password you want to see ")
print(f"Password of {n} is {dict1[n]}")

x = input("Enter the user whose password you have to change ")
y = input("Enter the new password")

dict1[x] = y
print("Password changed successfully")