from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Lives(Turtle):
    """
    Represents the remaining lives of the player and displays the current number of lives on the screen.
    """

    def __init__(self):
        super().__init__()
        self.lives = 5  # Number of remaining lives
        self.color("white")
        self.penup()
        self.goto(-200, 260)  # Position the lives display on the screen
        self.update_lives()
        self.hideturtle()

    def update_lives(self):
        """
        Updates and displays the current number of lives on the screen.
        """
        self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT)  # Write the current number of lives on the screen

    def increase_lives(self, increase_value):
        """
        Increases the number of lives by the specified value and updates the lives display.
        """
        self.lives += increase_value
        self.clear()  # Clear the previous lives display
        self.update_lives()

    def decrease_lives(self, decrease_value):
        """
        Decreases the number of lives by the specified value and updates the lives display.
        """
        self.lives -= decrease_value
        self.clear()  # Clear the previous lives display
        self.update_lives()
