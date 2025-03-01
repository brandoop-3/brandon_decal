#hw5.py
#Brandon Pestoni

# HW1/HW2 Review: The Terminal + Command Line + Git

#1   'pwd'

#2   'ls'

#3    cd python_decal/brianna_repo/
#     git pull orgigin master

#4 mv homeowrk.py ~/python_decal/judy_decal/homework

#5 cat python_decal/judy_decal/homework/homework.py

#6 nano python_decal/judy_decal/homework/homework.py

#7 git add homework.py
#  git commit -m "adding homework"
#  git push origin master

#8 This error happens because the the remote repostiory has changes that my local repository doesn't have yet. So we have to use the git pull command.
#   git pull origin master
#   git add homework.py
#   git commit -m "adding homework"
#   git push origin master

#9 ~/Recents

###############################################################################################################################################

# 2 HW3 Review: Data Types + Functions +
# Conditionals + Loops

# 2.1 Data Types

# Write a function that takes any input and returns a string indicating its data
# type.

def checkDataType(whateverData):
    return type(whateverData) #uses built in command to return type of input 

print(checkDataType(3.14))
print(checkDataType(True))

# 2.2 Conditionals

def evenOrOdd(int):
    if int % 2 == 0: #definition of even number
        return ('Even')
    else:
        return ('Odd')
    
print(evenOrOdd(7))
print(evenOrOdd(10))

# 3 Loops

numbers = [1, 2, 3, 4, 5]

def sumWithLoop(numbers):
    sum = 0 #create sum counter
    for i in numbers:
        sum += i #adds each element to total sum
    return sum

print(sumWithLoop(numbers))

# 4 HW4 Review: Lists

# 4.1 Lists

list = ['a', 'b', 'c']

def duplicateList(list):
    double_list = [] #create empty list
    for i in list:
        double_list.append(i) #appends element twice
        double_list.append(i)
    return double_list

print(duplicateList(list))

# 4.2 Debugging

def square(num):
    return num ** num

print(square(3))

#The error was that it was being mutliplied where '**' needed to be used instead.