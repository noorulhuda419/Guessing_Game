#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
#global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer, turns):
    if guess > answer:
        print("You Have Guess Too High!")
        return turns-1
    elif guess < answer:
        print("You Have Guess Too Low!")
        return turns-1
    else:
        print(f"You got it! the answer was {answer} Hurray You Won!!")

        
def set_difficuty():
    level = input("choose a difficulty level. type 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print("Welcome to the Guessing Game")
    print("I'm Thinking Of An Number Between 1 and 100")
    #the final answer
    answer = randint(1,100)
    guess = 0
    turns = set_difficuty()
    while guess != answer:
        print(f" you have {turns} attempts remaining")
        guess = int(input("Make a Guess"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guess .you lose... Better luck next time")
            return
        elif guess != answer:
            print("Guess Again")
game()


# In[ ]:




