from turtle import Turtle
import random

FOOD_SIZE = 1  # Will be (20 * FOOD_SIZE) pixels


class BadFood(Turtle):
    """
    Represents the bad food objects in the game that the snake should avoid.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color("red")
        self.speed("fastest")

    def random_start(self):
        """
        Sets a random starting position for the bad food.
        The bad food will be placed within the game screen bounds.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
