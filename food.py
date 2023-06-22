from turtle import Turtle
import random

FOOD_SIZE = 0.5  # Size of the food item (20 * FOOD_SIZE) pixels


class Food(Turtle):
    """Represents a food item in the game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set shape as a circle
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)  # Set size of the food
        self.color("blue")  # Set color to blue
        self.speed("fastest")  # Set movement speed to the fastest
        self.refresh()  # Position the food item randomly on the screen

    def refresh(self):
        """Positions the food item randomly on the screen."""
        random_x = random.randint(-280, 280)  # Generate random x-coordinate
        random_y = random.randint(-280, 280)  # Generate random y-coordinate
        self.goto(random_x, random_y)  # Move the food item to the generated coordinates
