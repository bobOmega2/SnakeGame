from turtle import Turtle

FONT = ("Courier", 24, "bold")


class MysteryMessage(Turtle):
    """Represents the message displayed for each power-up in the game."""

    def __init__(self):
        super().__init__()
        self.message = " "
        self.color("white")
        self.penup()
        self.goto(-200, -270)  # Set the initial position of the message
        self.hideturtle()

    def update_message(self):
        """Updates and displays the current power-up message."""
        self.write(f"Powerup: {self.message}", font=FONT)

    def speedup(self):
        """Displays the 'Speeding Up!' message for the speed-up power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Speeding Up!"
        self.clear()  # Clear the previous message
        self.update_message()

    def slowdown(self):
        """Displays the 'Slowing Down!' message for the slow-down power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Slowing Down!"
        self.clear()  # Clear the previous message
        self.update_message()

    def remove_segment(self):
        """Displays the 'Removed Segment!' message for the remove-segment power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Removed Segment!"
        self.clear()  # Clear the previous message
        self.update_message()

    def double_score(self):
        """Displays the 'Doubled Score!' message for the double-score power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Doubled Score!"
        self.clear()  # Clear the previous message
        self.update_message()

    def zero_score(self):
        """Displays the 'Score is Zero :(' message for the zero-score power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Score is Zero :("
        self.clear()  # Clear the previous message
        self.update_message()

    def double_lives(self):
        """Displays the 'Lives Doubled!' message for the double-lives power-up."""
        self.showturtle()  # Make the turtle visible
        self.message = "Lives Doubled!"
        self.clear()  # Clear the previous message
        self.update_message()

    def no_powerup(self):
        """Displays the 'None!' message when no power-up is active."""
        self.showturtle()  # Make the turtle visible
        self.message = "None!"
        self.clear()  # Clear the previous message
        self.update_message()
