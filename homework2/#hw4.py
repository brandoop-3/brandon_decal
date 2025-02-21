#hw4.py
#Brandon Pestoni

# 2.1 Making a List Variable

# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually.

my_list = list(range(21))

print(my_list)

# 2.2 Working with List Elements

# Write a function that will take in your list from Part 2.1 and square each element
# in the list. Assign the result to a new variable.

def square_list(arb_list):
    return [i ** 2 for i in arb_list]

my_list_squared = square_list(my_list)
print(my_list_squared)

# 2.3 Slicing

def slice_list(arb_list):
    sliced_list = arb_list[:15]
    return sliced_list

my_sliced_list = slice_list(my_list_squared)
print(my_sliced_list)

# 2.4 Striding

def stride_list(arb_list):
    strided_list = arb_list[4::5]
    return strided_list

my_strided_list = stride_list(my_list_squared)
print(my_strided_list)

# 2.5 Slicing & Striding

# Write a function that takes your list from Part 2.2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.

def stride_and_slice_list(arb_list):
    sliced_list = arb_list[::-3]
    reversed_list = sliced_list[::1]
    return reversed_list

my_final_list = stride_and_slice_list(my_list_squared)
print(my_final_list)

 
# 3.1 Creating a 5x5 2D List

# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.

def create_2d_list():
    return [[(i * 5) + j + 1 for j in range(5)] for i in range(5)]

matrix = create_2d_list()
print(matrix)


# 3.2 Replacing 2D List with Multiples of 3

# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”.

# >>> matrix = create_2d_list()
# >>> modified_2d_list(matrix)
# [[1, 2, ‘?’, 4, 5],
# [‘?’, 7, 8, ‘?’, 10],
# [11, ‘?’, 13, 14, ‘?’],
# [16, 17, ‘?’, 19, 20],
# [‘?’, 22, 23, ‘?’, 25]]

# 3.3 Summing None-’ ?’ Elements

# Assign the result of your function from Part 3.2 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.

# >>> matrix = create_2d_list()
# >>> new_matrix = modified_2d_list(matrix)
# >>> sum_non_question_elements(new_matrix)


