import math

'''
    Lesson: Math Library
    Author: Owais Ali Khan
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''

def q1(): 
  num = float(input("Input a number: "))
  print(math.sqrt(num))

def q2(): 
  num = int(input("Input a number: "))
  print(math.isqrt(num))


def q3(): 
  num = float(input("Input a number: "))
  print(math.floor(num))


def q4(): 
  num = float(input("Input a number: "))
  print(math.ceil(num))

def q5(): 
  num = float(input("Input a number: "))
  num2 = float(input("Input another number: "))
  num *= num2
  num = math.trunc(num/2)
  print(num)



#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''
