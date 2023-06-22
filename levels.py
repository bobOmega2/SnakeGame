from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Levels(Turtle):
    """
    Represents the game levels and displays the current level on the screen.
    """

    def __init__(self):
        super().__init__()
        self.level = 1  # Current level of the game
        self.color("white")
        self.penup()
        self.goto(200, 260)  # Position the level display on the screen
        self.hideturtle()

    def print_level(self):
        """
        Prints the current level on the screen.
        """
        self.clear()  # Clear any previous level display
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)  # Write the current level on the screen
