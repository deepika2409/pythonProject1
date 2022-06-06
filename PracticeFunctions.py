# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def myfunc(*args):
#     index_count = 0
#     x = ''
#
#     for y in args[index_count]:
#         if index_count % 2 == 0:
#             z = y.lower()
#             x = x+z
#
#         else:
#             z = y.upper()
#             x = x+z
#
#         index_count += 1
#     return x
#
# print(myfunc('asdfghjkl'))
#
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a,b):
#     if (a % 2 ==0 and b % 2 ==0):
#         if a < b:
#             return a
#         else:
#             return b
#
#     elif (a % 2 != 0 or b % 2 != 0):
#         if a < b:
#             return b
#         else:
#             return a
#
# print(lesser_of_two_evens(2,8))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
