from turtle import Turtle, Screen
import random

class TurtleRace():
    def __init__(self):
        self.colors = ["blue","red","violet","yellow","green","orange"]

    def create_turtles(self):
        """Creates all the turtle object for the race with their respective colors"""
        self.turtles = dict()
        for color in range(len(self.colors)):
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.color(self.colors[color])
            self.turtles[color] = new_turtle

    def starting_position(self):
        """Moves all the turtles to the starting position"""
        self.create_turtles()
        y_axis = [75,45,15,-15,-45,-75]
        for turtle_no,turtle in self.turtles.items():
            turtle.up()
            turtle.goto(x=-230,y=y_axis[turtle_no])
            turtle.down()
            
    def start_race(self):
        """Creates the screen, asks for the bet and starts the race"""
        my_screen = Screen()
        my_screen.setup(width=500,height=400)
        user_bet = my_screen.textinput(title="Make your Bet",prompt=f"Which turtle will win the race? Enter a color({self.colors}): ")
        self.starting_position()
        if user_bet:
            race_is_on = True
        winner = ""
        while race_is_on:
            for turtle_no,turtle in self.turtles.items():
                move = random.randint(0,10)
                turtle.forward(move)
                if turtle.xcor() >230:
                    race_is_on = False
                    winner = turtle_no
        
        if user_bet == self.colors[winner]:
            print(f"Conratulations, your {self.colors[winner]} turtle has won the race")
        else:
            print(f"You lose. The {self.colors[winner]} turtle won the race")
        my_screen.exitonclick()

if __name__ == "__main__":
    race = TurtleRace()
    race.start_race()
