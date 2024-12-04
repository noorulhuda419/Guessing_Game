#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
# function define
def check_number():
    a = randint(1, 20) #co-efficent of x
    b = randint(-20, 20) # numbers
    c = randint(1, 60) # value of x
    return a, b, c
def math_game():
    print("Hey! Welcome to Math Solver Game")
    print("Your Aim To Solve the simple Linear Equation")  
#generate values
    a, b, c = check_number()
    answer = (c - b) // a  #to ensure the answer 
    print(f"solve for the x: {a}x + ({b}) = {c}")
    attempts = 5
    while attempts > 0:
        guess = float(input(f"you have remaining {attempts} give value for x:"))
        if guess == answer:
            print(f"congratulation! you solved it the value of x is {answer} ")
            return 
        elif guess > answer:
            print("Too High!")
        else: 
            print("Too Low!")
        attempts -= 1
    print(f"Out of attempts! the correct value of x : {answer}.")
            
math_game()

