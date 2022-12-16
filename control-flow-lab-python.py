# CONTROL FLOW LAB ! ! ! ! ! DELIVERABLE
# After lab checkout the Sending Email and Text Messages
# Web scraping

# 7 exercises ================

# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

# Answer ======================
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# letter = input('Please enter a letter from the alphabet (a-z or A-Z): ')
# print(f'The user entered {letter}')

# # if letter is in the vowels list
# if letter in vowels:
#     print(f'The letter {letter} is a vowel')

# else:
#     print(f'{letter} is a consonant')


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

#Answer: = == = = = = = ==   ==================
# phrase= ""
# # while loop
# while phrase != "quit":
#     phrase = input('Please enter a phrase: ')
#     print(f"You entered {phrase}")
#     print(f"What you entered is {len(phrase)} charaters long")
#     print("type quit to stop")


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

# Answer = = = = == = .  ==================================
# dog_age = 0
# dog_age_input = input('Enter your dogs age in humans years: ')
# # change it into an integer
# dog_age = int(dog_age_input)
# print(type(dog_age))

# if dog_age <= 2:
#     dog_age *= 10


# elif dog_age > 2:
#     dog_age = 20 + ((dog_age - 2) * 7)

# else: 
#     print('Blah')


# print(f"Your dogs age in dog years is {dog_age}")



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# ANSWER ===========================
# print("Enter the lengths of three sides of a triangle:")
# first_input = input("a: ")
# second_input = input("b: ")
# third_input = input("c: ")

# triangle_type = ""

# print(f"You chose {first_input}, {second_input}, {third_input}")

# if first_input == second_input and first_input == third_input:
#     triangle_type = "equalateral"

# elif first_input == second_input or second_input == third_input:
#     triangle_type = "isosceles"

# else:
#     triangle_type = "scalene"

# print(f"A triangle with sides of {first_input} {second_input} {third_input} is a {triangle_type}")




# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

# ANSWER ==============================================

# number_terms = 50
# n1 = 0
# n2 = 1
# count = 0

# print('The Fib Sequence')
# while count < number_terms:
#     num = n1 + n2
#     n1 = n2
#     n2 = num
#     count += 1
#     print(f"term: {count} / number: {num}")



# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month_input = input("Enter the month of the year as 3 characters ex:(jan, jul, dec): ").lower()
day_input = int(input("Enter the day of the month: "))

if month_input in ('dec', 'jan', 'feb', 'mar'):
    season = 'winter'
elif month_input in ('apr', 'may', 'june'):
    season = 'spring'
elif month_input in ('jul', 'aug', 'sep'):
    season = 'summer'
else:
    season = 'fall'

if month_input == 'mar' and (day_input < 19):
    season = 'winter'
elif month_input == 'jun' and (day_input < 20):
    season = 'spring'
elif month_input == 'sep' and (day_input < 21):
    season = 'summer'
elif month_input == 'dec' and (day_input < 20): 
    season = 'fall'

print(f'It is {season}')