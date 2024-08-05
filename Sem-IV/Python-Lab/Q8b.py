print("Enter 5-6 lines of text ")
lines = [input(f"Lines {i+1}") for i in range(5)]

filename = "file1.txt"

with open(filename, "w") as file :
    for line in lines:
        file.write(line + "\n")

uppercase = 0
lowercase = 0
digit = 0

with open(filename,"r") as file:
    for line in lines:
        for char in line:
            if char.isupper():
                uppercase += 1
            if char.islower():
                lowercase += 1
            if char.isdigit():
                digit += 1

print("Upper case letters ",uppercase)
print("lower case letters ",lowercase)
print("Digits ",digit)

with open(filename,"r") as file:
    print(file.read())