# import turtle, random
# import turtle as t, random
from turtle import *
import random

# for aa in range(4):
#     turtle.forward(100)
#     turtle.right(90)

speed(10)
renk = ["red","blue"]
# turtle.goto(100,200)
for x in range(random.randint(5,20)):
    color(random.choice(renk))
    up()
    goto(random.randint(-200,200),random.randint(-200,200))
    down()
    ku = random.randint(30,100)
    for aa in range(4):
        forward(ku)
        right(90)


input()
