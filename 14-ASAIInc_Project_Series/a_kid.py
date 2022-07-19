# module random's choice() function

from random import choice


questions = ['What is the meaning Life? ; ', 'Why Life? ; ','Why this Life & Universe? ; ',  "Where did the humans came from? ; ", "What's our purpose? ; "]

question = choice(questions)

answer = 'just because'

print('\nHey, Could You Tell Me The Answer Of My Questions_\n')

user = input(question).strip()


while user != answer:
    user = input('But Why? ; ')
    

print('Okay, I Understood!\n')

