# here is a comment

total_guitars = 7
#snake_case <-- convention for naming variables

# Print is pythons console.log
# print(total_guitars, 'total number of guitars')
# total_guitars += 1

# print(total_guitars, '<-- total guitars')

# msg = "I have " + str(total_guitars) + " guitars you bozo"
# print(msg)

# # preferred way
# msg = f"I have {total_guitars} guitars homie"
# print(msg)

# # template = "my name is {} and I like {}"

# # print(template.format('jim', 'tacos'))

# print(dir(msg))
# print(msg.upper())
# print(msg.split(' '))
# print(len(msg))


######## Data Types

#type()
# type(235)
# print(type(235))
# print(type(42.111))
# print(type('hello'))
# print(type('goodbye'))
# print(type([]), '<--- array brackets')
# print(type({}), '<--- object braces')
# print(type(True), 'true')
# print(type(False), 'false')

# SSince everything comes from a class
# EVERYTHING IN PYTHON IS AN OJBECT

#Object - properties (Values) - and have methods (functions)

#How to look inside a datatype for its methods
# dir()

# print(dir([]))

# my_closet = ['shirt', 'long shirt']
# print(dir(my_closet))

# sum = 1.5 + 1
# print(sum, type(sum))


# Python we dont have null we have none
# print(type(None))


# LOGICAL OPERATORS

# returns the first operand if truthy otherwise return second

# is21 = 21 or 'not'

# isOld = 0 or True

# print(isOld)

# print(is21)

floor = 'sticky'

if floor == 'sticky':
    print('clean the floor idiot')
