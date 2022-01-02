############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

#=======================================




#
# def add(n1, n2):
#     return n1 + n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1,n2):
#     return n1 / n2
#
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }
#
# num1 = int(input("Whats the first number?: "))
# num2 = int(input("Whats the second number?: "))
# for symbol in operations:
#     print(symbol)
# operations_symbol = input("Pick and operation from the line above: ")
# calculation_function = operations[operations_symbol]
# print(calculation_function)
# answer = calculation_function(num1, num2)
#
#
# print(f"{num1} {operations_symbol} {num2} = {answer}")
#


#
# def format_name(fname, lname):
#     return(fname.title() + " " + lname.title()
#
# )
#
# print(format_name("sdf","tttt"))

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict["class"]["student"]["marks"]["history"])

#
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 60, 'Fourty': 40, 'Fifty': 50}
#
#
# dict3 = {**dict1, ** dict2}
# print(dict3)
# dict4 = dict1.copy()
# dict4.update(dict2)
# print(dict4)


#dl = dict(zip(keys, values))
#print(dl)

# dl = {}
# for i in range(len(keys)):
#     k = keys[i]
#     v = values[i]
#     #dl[keys[i]] = values[i]
#     dl.update({keys[i]: values[i]})



#print(dl)

# programming_dictionary = {
#     "Bug":"Code issue",
#     "Function":"repeating code",
#     "Loop":"hhhh"
# }
#
# print(programming_dictionary["Loop"])
#
# programming_dictionary["Loop"] = "Round and round"
#
# print(programming_dictionary)
#
# # empty_dictionary = {}
# #
# # programming_dictionary = {}
#
# for thing in programming_dictionary:
#     print(thing)
#     print(programming_dictionary[thing])
#




