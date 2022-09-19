from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

color_list = ['pink', 'black', 'green', 'yellow', 'blue', 'grey']
y_positions = [-125, -75, -25, 25, 75, 125]
turtle_dict = {
    'pink':"hase_the_passion_turtle",
    'black':"marsh_the_relative_turtle",
    'green':"yorck_the_sidetracking_turtle",
    'yellow':"arber_the_EM_turtle",
    'blue':"robbo_the_mighty_turtle",
    'grey':"robin_the_crotch_burgling_turtle"
}

all_turtles = []
for turtle_index in range(len(turtle_dict)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(x=-200, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

mytitle = "Make your bet sir."
myprompt = "Which turtle will win the race? The turtles are:\n\nHase: Pink\nMarsh: Black\nYorck: Green\nArber: " \
           "Yellow\nRobbo: Blue\nRobin Ball: Grey\nEnter a color: "
user_bet = (screen.textinput(title=mytitle, prompt=myprompt)).lower()

if user_bet in color_list:
    is_race_on = True
else:
    print(f"You have not entered one of the list colors. FAIL.")

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:  # Turtle is a 40 x 40 object with end line at 250.
            winner = turtle.pencolor()  # .color is either a method or attribute. We want only the attribute and so use .pencolor.
            if winner == 'grey' and user_bet == 'grey':
                line1 = "The winner is {winner}; {turtle_dict[winner]}."
                line2 = "You don't win when Robin Ball does. No one does. A spree of crotch-burgling occurs, " \
                        "you finish your drink and a shot for everyone else. How do you feel?"
                user_response = (screen.textinput(title=line1, prompt=line2)).lower()
            elif winner == 'grey':  # Not linked to dictionary, hard-coded. Could be improved.
                line1 = "The winner is Robin Ball. You don't win. No-one wins. Everyone finish their drink."
                line2 = "How do you feel?"
                user_response = (screen.textinput(title=line1, prompt=line2)).lower()
            elif winner == user_bet:
                line1 = "The winner is " + winner + ";" +  turtle_dict[winner]
                line2 = "You win! Inflict a shot on a person of your choosing. How do you feel?"
                user_response = (screen.textinput(title=line1, prompt=line2)).lower()
            else:
                line1 = "The winner is " + winner + ";" + turtle_dict[winner]
                line2 = "You lose. Four fingers. How do you feel?"
                user_response = (screen.textinput(title=line1, prompt=line2)).lower()
            is_race_on = False
        else:
            rand_distance = random.randint(0,10) #randint is inclusive.
            turtle.forward(rand_distance)

screen.exitonclick()



