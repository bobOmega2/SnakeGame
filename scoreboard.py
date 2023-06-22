from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """Represents the scoreboard in the game."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)  # Position the scoreboard
        self.update_scoreboard()  # Update the initial scoreboard
        self.hideturtle()

    def update_scoreboard(self):
        """Updates and displays the current score on the scoreboard."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, increase_value):
        """Increases the score by the given value and updates the scoreboard."""
        self.score += increase_value
        self.clear()  # Clear the previous scoreboard
        self.update_scoreboard()

    def decrease_score(self, decrease_value):
        """Decreases the score by the given value and updates the scoreboard if score is not negative."""
        if self.score >= 0:
            self.score -= decrease_value
            self.clear()  # Clear the previous scoreboard
            self.update_scoreboard()

    def game_over(self):
        """Resets the score to zero, updates and displays the game over message on the scoreboard."""
        self.score = 0
        self.clear()  # Clear the previous scoreboard
        self.update_scoreboard()
        self.goto(0, 0)  # Position the message
        self.write("Lmao Bad", align=ALIGNMENT, font=FONT)  # Display the game over message

    def game_won(self):
        """Displays the game won message on the scoreboard and prints the message."""
        self.goto(0, 0)  # Position the message
        self.write("You Won!", align=ALIGNMENT, font=FONT)  # Display the game won message
        print("You Won!")  # Print the game won message
