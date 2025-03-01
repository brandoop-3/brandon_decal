#Brandon Pestoni
#HW 3 - Data Types, Functions, Conditionals, and Loops

#1 Oski Stole Your Power

#Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
#a different way (by writing a function) that can compute x raised to the power
#of y

def computePower(x, y):
    result = 1
    for i in range(y):
        result *= x    
    return result

x = 2
y = 3
print(computePower(2,3))

#2 What Should I Wear?

#You are trying to decide what to wear to the Python DeCal lecture, but you
# are only concerned about the day’s lowest and highest temperatures. Write a
# function that takes in a list as input and returns a tuple with the min and max
# as two values.

def temperatureRange(temps):
    return (min(temps), max(temps)) #pulls min and max from the list

readings = [15, 14, 17, 20, 23, 28, 20] #temperatures
print(temperatureRange(readings))

#3 Check if its the Weekend

# All your classes have assigned problem sets due next week, and you want to
# check if it’s the weekend so you have time to work on them. Write a function
# that takes a day of the week (represented as an integer, where 1 = Monday, 2
# = Tuesday, etc) and returns True if its a weekend and False if otherwise.

def isWeekend(int):
    if int == 6: #checks if int = saturday(6) adn returns true
        return True
    if int == 7: #checks if int = sunday(7) and returns true
        return True
    else:        #checks if int is other day of the week (1-5) and returns false
        return False
    
day = 6 #Saturday
print(isWeekend(day))

#4 Fuel Efficiency Calculator

# The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
# CA) and they want to pick the best car. Write a function that takes the distance
# traveled (in miles) and the amount of fuel consumed (in gallons) as input and
# returns the fuel efficiency.

def fuel_efficiency(distance, fuel):
    result = distance / fuel #fuel efficeincy formula
    return result

distance = 70 # miles
fuel = 21.5 #gallons
print(round(fuel_efficiency(distance, fuel), 2))

#5 Secret Code

# Write a function that takes an integer as input and moves its last digit to the
# front of the number. You may NOT convert the input to a string. Hint: Try
# modulus (%) and floor division. (\\) to solve this problem.

def decodeNumbers(n):
    last_digit = n % 10  #this gets the last digit of the integer
    remaining_part = n // 10  # Remove the last digit

    # Find the place value for the last digit
    place_value = 1
    temp = remaining_part
    while temp > 0:
        temp = temp // 10
        place_value = place_value * 10

    #moving last digit to front of the integer
    new_number = last_digit * place_value + remaining_part
    return new_number

# Example usage:
n = 12345
print(decodeNumbers(n))  # Output: 51234

#6 Min & Max but with Loops!

# 6.1 For Loops

# Write two functions to manually find the minimum and maximum values in a
# list of numbers with for loops.

def find_min_with_for_loop(nums):
    min_value = nums[0]  # assign min value to first element
    for i in nums:
        if i < min_value: #check if next element is less than assigned min value
            min_value = i  # update min_value if it is smaller
    return min_value  


def find_max_with_for_loop(nums):
    max_value = nums[0]  # assign max value to first element
    for i in nums:
        if i > max_value: #check if next element is greater than assigned max value
            max_value = i  # update max value if it is greater than
    return max_value  

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))     
print(find_max_with_for_loop(nums))

# 6.2 While Loops

# Write two functions to manually find the minimum and maximum values in a
# list of numbers with while loops

def find_min_with_while_loop(nums):
    min_value = nums[0]  # Start with the first element
    i = 1  # Start checking from the second element

    while i < len(nums):
        if nums[i] < min_value:
            min_value = nums[i]  # Update if a smaller element is found
        i += 1  # Move to the next index
    return min_value

def find_max_with_while_loop(nums):
    max_value = nums[0]  # assign max to first element
    i = 1  # start with second element

    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]  # update if a larger number is found
        i += 1  # next element
    return max_value


nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))
print(find_max_with_while_loop(nums))

# 7 Counting Vowels

# Write a function that takes a string as an input and returns the number of vowels
# in the string and the number of consonants in the string as tuple. Don’t forget
# about capital letters! Hint: You can use .isalpha() to check if a character is
# a letter.

def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():  # built-in function to see is charcter is a letter in the alphabet
            if char in vowels:
                vowel_count += 1 #checks if the character is a vowel in the defined string of vowels above and counts it
            else:
                consonant_count += 1 #if not a vowel, then counts it as a consonant
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))  

# 8 Calculate Digital Root
# Write a function that takes an integer as an input and returns the sum of its
# digits.

def digital_root(num):
    total = 0
    while num > 0: #runs through loop until all digits have been removed
        total += num % 10  # adds last digit to total
        num //= 10  # Removes the last digit
    return total

num = 2468
print(digital_root(num))  