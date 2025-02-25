#hw4.py
#Brandon Pestoni

# 2.1 Making a List Variable


my_list = list(range(21)) #list of numbers from 0 to 20 (not including 21)

print(my_list)

# 2.2 Working with List Elements

def square_list(arb_list): #square function using double asterick
    return [i ** 2 for i in arb_list]


my_list_squared = square_list(my_list) #assigns variable to called square fumction
print(f"The original list squared is:", my_list_squared) #prints assigned variable

# 2.3 Slicing

def slice_list(arb_list): #slice fucntion
    sliced_list = arb_list[:15] #jumps and grabs every element and stops at the 15th element
    return sliced_list

my_sliced_list = slice_list(my_list_squared) 
print(f"The sliced list is:",my_sliced_list) #prints assigned variable

# 2.4 Striding

def stride_list(arb_list): #stride function
    strided_list = arb_list[4::5] #starts at the 5 element (python starts at 0) and grabs every 5 element after
    return strided_list

my_strided_list = stride_list(my_list_squared)
print(f"The strided list is:",my_strided_list) #prints assigned variable

# 2.5 Slicing & Striding

def stride_and_slice_list(arb_list):
    sliced_list = arb_list[::-3] # slices and strides starting backwards and grabbing ever 3rd element
    reversed_list = sliced_list[::1]
    return reversed_list

my_final_list = stride_and_slice_list(my_list_squared)
print(f"The sliced and strided list is:", my_final_list) #prints assigned variable

 
# 3.1 Creating a 5x5 2D List

def create_2d_list():
    return [[(i * 5) + j + 1 for j in range(5)] for i in range(5)] 

matrix = create_2d_list()
print(f"The 2D matrix is:",matrix) #prints assigned variable


# 3.2 Replacing 2D List with Multiples of 3

def modified_2D_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0: #if the element is divisible by 3, it replaces with the character '?'
                matrix[i][j] = '?'
    return matrix

matrix = create_2d_list()
modified_matrix = modified_2D_list(matrix)
print(f"The 2D matrix with question marks replaced for multiples of 3 is:",modified_matrix) #prints assigned variable


# 3.3 Summing None-’ ?’ Elements

def sum_non_question_elements(matrix):
    matrix_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != '?': #if the character isn't a '?', then it adds that to the total sum of the elements of the matrix
                matrix_sum += matrix[i][j]
    return matrix_sum

matrix = create_2d_list()
new_matrix = modified_2D_list(matrix)
print(f"The 2D matrix summed over all integer values is:",sum_non_question_elements(new_matrix)) #prints total sum of the matrix by calling function


