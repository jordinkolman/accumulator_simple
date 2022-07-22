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

accumulator()