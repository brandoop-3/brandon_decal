#Brandon Pestoni

# 1 Prime Clusters

import numpy as np

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])


def contains_primes(arr):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    filtered_rows = []  # empty list for new array

    for row in arr:  # iterate through each row in array
        has_prime = False  #initialize variable to false for checking if number is prime or not

        for num in row:  #interate through each number in list
            if is_prime(num):  # check if the number is prime
                has_prime = True  #if number is prime, change variable to true
                break  #since we found a number thats prime, we don't have to check the rest if there is any
        if has_prime:  # If the row contains at least one prime, add it to the list
            filtered_rows.append(row)

    return np.array(filtered_rows)  # Convert the list back to a NumPy array
        
print(contains_primes(arr))


# 2 Let’s play Checkers!

# 2.1
# Start by writing a function that creates a 8x8 square matrix with only zeros.

def checkerboard():
    return np.zeros((8,8)) #initializes an 8x8 matrix of zeroes

print(checkerboard()) #prints matrix

# 2.2
# For only the odd rows, make an alternating pattern of ones and zeroes.

board = checkerboard() #assign 8x8 matrix of zeroes to variable

def checkerboard_oddrows():
    for i in range(0, 8, 2):  # iterating over odd rows (1, 3, 5, 7) #index = row -1
        board[i] = [1, 0, 1, 0, 1, 0, 1, 0] #assign row to odd rows
    return board

print(checkerboard_oddrows()) 

# 2.3
# Finish the checkerboard with the even rows.

board2 = checkerboard()
def checkerboard_evenrows():
    for i in range(1, 8, 2):  # iterating over even rows (2, 4, 6, 8) #index = row -1
        board2[i] = [0, 1, 0, 1, 0, 1, 0, 1] #assings row to even rows
    return board2

full_checkboard = checkerboard_oddrows() + checkerboard_evenrows()
print(full_checkboard)

# 2.4
# Re-write your function such that the checkerboard begins with a 0 instead.

def reverse_checkboard():
    board3 = np.zeros((8,8))
    for i in range(1, 8, 2):  # Iterating over even rows (1, 3, 5, 7)
        board3[i] = [1, 0, 1, 0, 1, 0, 1, 0]
    for i in range(0, 8, 2):  # Iterating over odd rows (1, 3, 5, 7)
        board3[i] = [0, 1, 0, 1, 0, 1, 0, 1]
    return board3


print(reverse_checkboard())

# 3 The Expanding Universe
# You have now become fascinated with how dark energy is making galaxies ac-
# celerate away from us. Write a function that takes in a string and a number,
# and returns the string with the specified number of spaces inserted between each
# letter, simulating the expansion of space! For example:

universe = np.array(['galaxy', 'clusters'])

result = ''
def expansion(str, int):
    result = '' #assign variable to space character
    for row in str:
        for i in row:
            result = result + i + int*' ' #adds an integer number of spaces between each iterated character of the string
    return result

print(expansion(universe, 1))
print(expansion(universe, 2))

# 4 Second-Dimmest Star
# While analyzing a dataset of star luminosities, you need to identify the second-
# dimmest star in each cluster. Write a function that takes a 2D NumPy array
# and returns an array containing only the second-smallest value in each column.
# For example:

np.random.seed(1234)
stars = np.random.randint(500, 2000, (5, 5))

print(stars)

def secondDimmest(data):
    sec_dim_array = [] #initialize new array
    for col in data.T: #
        sorted_col = np.sort(col)
        sec_dim_array.append(sorted_col[1])  #takes the second value in the newlysorted column (second smallest value)
                                             # and adds it to initialized array above
    return np.array(sec_dim_array)

print(secondDimmest(stars))


