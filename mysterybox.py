from turtle import Turtle
import random

FOOD_SIZE = 2  # Will be (20 * FOOD_SIZE) pixels


class MysteryBox(Turtle):
    """
    Represents a mystery box object in the game. When the snake collides with the box, it triggers a random power-up.
    """

    def __init__(self, snake, mysteryMessage, scoreboard, lives):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color("orange")
        self.speed("fastest")
        self.snake = snake  # Reference to the snake object
        self.mysteryMessage = mysteryMessage  # Reference to the mystery message object
        self.scoreboard = scoreboard  # Reference to the scoreboard object
        self.lives = lives  # Reference to the lives object
        self.random_start()
        self.powerups = [self.speedup, self.slowdown,
                         self.remove_segment, self.double_score,
                         self.zero_score, self.double_lives]  # List of available power-up functions

    def random_start(self):
        """
        Places the mystery box in a random location on the screen.
        """
        self.showturtle()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def speedup(self):
        """
        Speeds up the snake and updates the mystery message.
        """
        self.hideturtle()
        self.snake.increase_speed()
        self.mysteryMessage.speedup()
        print("Speeding Up!")

    def slowdown(self):
        """
        Slows down the snake and updates the mystery message.
        """
        self.hideturtle()
        self.snake.decrease_speed()
        self.mysteryMessage.slowdown()
        print("Slowing Down!")

    def remove_segment(self):
        """
        Removes a segment from the snake and updates the mystery message.
        """
        self.hideturtle()
        self.snake.remove_segment()
        print("Removed segment!")
        self.mysteryMessage.remove_segment()

    def double_score(self):
        """
        Doubles the player's score and updates the mystery message.
        """
        self.hideturtle()
        self.scoreboard.increase_score(self.scoreboard.score)
        self.scoreboard.update_scoreboard()
        self.mysteryMessage.double_score()

    def zero_score(self):
        """
        Resets the player's score to zero and updates the mystery message.
        """
        self.hideturtle()
        self.scoreboard.score = 0
        self.scoreboard.clear()
        self.scoreboard.update_scoreboard()
        self.mysteryMessage.zero_score()

    def double_lives(self):
        """
        Doubles the number of lives and updates the mystery message.
        """
        self.hideturtle()
        self.lives.increase_lives(self.lives.lives)
        self.mysteryMessage.double_lives()
