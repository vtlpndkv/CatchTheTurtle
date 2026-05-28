from turtle import *
from random import *
from time import *

print('CatchTheTurtle')
print('Лови черепашку! Для победы необходимо набрать 30 очков')

t = Turtle()
t.shape('turtle')
t.color('purple')
t.penup()

score = Turtle()
score.hideturtle()
score.penup()
score.color('purple')
score.goto(-100, 150)
score.score = 0
score.write(f'Счёт: {score.score}', font=('Arial', 20)) 

def rand_move():
    x = randint(-200, 200)
    y = randint(-200, 200)
    t.goto(x, y)

def catch(x, y):
    t.write('👾', font=('Arial', 15))
    score.clear()
    score.score +=1
    score.write(f'Счёт: {score.score}', font=('Arial', 20))
    rand_move()

t.onclick(catch)

i = 1
while i == 1:
    sleep(0.4)
    rand_move()
    if score.score >= 30:
        t.hideturtle()
        t.goto(-100, 125)
        t.write('Победа!', font=('Arial', 20))
        t.hideturtle()
        print('Хотите сыграть ещё раз?')
        print('да/нет')
        again = input().lower()
        if again != 'нет':
            t.showturtle()
            i = 1
            score.clear()
            score.score = 0
            score.write(f'Счёт: {score.score}', font=('Arial', 20))
            t.clear()
            t.showturtle()
        else: 
            i = 0
            t.color('red')
            t.goto(-100, 100)
            t.write('Игра окончена!', font=('Arial', 20))
        
    