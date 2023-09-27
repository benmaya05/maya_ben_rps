# This file was created by: Ben Maya on 09/08/2023

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
# setup the width and height for the window
WIDTH, HEIGHT = 1000, 800

rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170
# 3 lines of code above setup width and height for each image for R, P, and S


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="black")

# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates "idioting proofing"
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = 300
rock_pos_y = 250
# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 300
paper_pos_y = -55
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = -305
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# 5 lines below are a function checks if mouse clicks within the clickboxes for R, P, or S
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
# function that passes through wn onlick
def mouse_pos(x, y):
# this code runs when ROCK is chosen
    if collide (x,y,rock_instance,rock_w,rock_h):
        print("it is " + str(collide(x,y,rock_instance,rock_w,rock_h)) + " that I collided with rock")
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        '''https://holypython.com/python-turtle-tutorial/turtle-hideturtle-showturtle/#:~:text=Just%20add%20.,turtle.
            2 lines above hide the images that were not chosen... the link helped me code that'''
        turtle.color('light blue')
        style = ('Courier', 18, 'italic')
        turtle.write("You Chose Rock                     ", font=style, align='right')
        # spaces after "You Chose Rock" makes sure the following text does not overlap
        # font/style/align/turtle.color manipulates the text's position, color, font, font size
        turtle.hideturtle()
        import time
        time.sleep(2)
        # "time.sleep(2)" for suspense :)
        from random import randint
        choices = ["Rock", "Paper", "Scissors"]
        x = (choices[randint(0,2)])
        # three lines above randomly choose R, P, or S
        turtle.color('deep pink')
        style = ('Courier', 18, 'italic')
        turtle.write("Computer Chose...    ", font =style, align='right' )
        turtle.hideturtle()
        time.sleep(2)
        # "time.sleep(2)" for suspense :)
# below are the different outcomes for when user chose Rock
        if x == "Scissors":
            turtle.color('light green')
            style = ('Courier', 18, 'italic')
            turtle.write("          SCISSORS, YOU WIN!!", font =style, align = 'center')
        if x == "Paper":
            turtle.color('red')
            style = ('Courier', 18, 'italic')
            turtle.write("        PAPER, YOU LOSE!!", font =style, align = 'center')
        elif x == "Rock":
            turtle.color('light blue')
            style = ('Courier', 18, 'italic')
            turtle.write("              ROCK, TIE!! TRY AGAIN!!", font =style, align = 'center')
# this code runs when PAPER is chosen
    elif collide (x,y,paper_instance,paper_w,paper_h):
        print("it is " + str(collide(x,y,paper_instance,paper_w,paper_h)) + " that I collided with paper")
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        turtle.color('light blue')
        style = ('Courier', 18, 'italic')
        turtle.write( "You Chose Paper                     ", font=style, align='right')
        import time
        time.sleep(2)
        from random import randint
        choices = ["Rock", "Paper", "Scissors"]
        x = (choices[randint(0,2)])
        turtle.color('deep pink')
        style = ('Courier', 18, 'italic')
        turtle.write("Computer Chose...    ", font =style, align='right' )
        turtle.hideturtle()
        time.sleep(2)
# below are the different outcomes for when user chose Paper
        if x == "Scissors":
            turtle.color('red')
            style = ('Courier', 18, 'italic')
            turtle.write("           SCISSORS, YOU LOSE!!", font =style, align = 'center')
        if x == "Rock":
            turtle.color('light green')
            style = ('Courier', 18, 'italic')
            turtle.write("        ROCK, YOU WIN!!", font =style, align = 'center')
        elif x == "Paper":
            turtle.color('light blue')
            style = ('Courier', 18, 'italic')
            turtle.write("               PAPER, TIE!! TRY AGAIN!!", font =style, align = 'center')
# this code runs when SCISSORS is chosen
    elif collide (x,y,scissors_instance,scissors_w,scissors_h):    
        print("it is " + str(collide(x,y,scissors_instance,scissors_w,scissors_h)) + " that I collided with scissors")
        rock_instance.hideturtle()
        paper_instance.hideturtle()
        turtle.color('light blue')
        style = ('Courier', 18, 'italic')
        turtle.write("You Chose Scissors                 ", font=style, align='right')
        turtle.hideturtle()
        import time
        time.sleep(2)
        from random import randint
        choices = ["Rock", "Paper", "Scissors"]
        x = (choices[randint(0,2)])
        turtle.color('deep pink')
        style = ('Courier', 18, 'italic')
        turtle.write("Computer Chose...", font =style, align='right' )
        turtle.hideturtle()
        time.sleep(2)
# below are the different outcomes for when user chose SCISSORS
        if x == "Paper":
            turtle.color('light green')
            style = ('Courier', 18, 'italic')
            turtle.write("                PAPER, YOU WIN!!", font =style, align = 'center')
        if x == "Rock":
            turtle.color('red')
            style = ('Courier', 18, 'italic')
            turtle.write("                ROCK, YOU LOSE!!", font =style, align = 'center')
        elif x == "Scissors":
            turtle.color('light blue')
            style = ('Courier', 18, 'italic')
            turtle.write("                           SCISSORS, TIE!! TRY AGAIN!!", font =style, align = 'center')

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()

