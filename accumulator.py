'''
Simple Accumulator

Created on Jul 22 13:40 2022

@author: Jordin Kolman
'''

def accumulator():
    sum = 0
    count = 1
    while count <= 5:
        num = int(input("Enter a number: "))
        sum = sum + num
        count = count + 1
    print("The sum of the numbers is:", sum)

def accumulator_v2():
    #Accumulator built as a class challenge
    sum = 0
    number = 1
    while number != 0:
        number = int(input("Enter a number. 0 ends the list: "))
        sum = sum + number
    print("The sum of the numbers is:", sum)

def accumulator_v3():
    #Same function as above, but built out a different way
    sum = 0
    number = 0
    while True:
        number = int(input("Enter a number. 0 ends the list: "))
        if number == 0:
            break
        sum += number
    print("The sum of the numbers is:", sum)


accumulator_v3()