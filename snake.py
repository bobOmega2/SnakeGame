from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Represents the snake object in the game.
    """

    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Reference to the head segment
        self.move_distance = 20  # Distance to move in each step

    def create_snake(self):
        """
        Creates the initial snake with three segments.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_segment(self):
        """
        Removes the last segment from the snake.
        """
        if len(self.segments) > 1:
            removed_segment = self.segments.pop(-1)
            removed_segment.hideturtle()  # Hide the segment turtle from the screen

    def extend(self):
        """
        Extends the snake by adding a new segment at the end.
        """
        if len(self.segments) != 1:
            self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake forward by updating the positions of its segments.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head segment separately
        self.head.forward(self.move_distance)

    def up(self):
        """
        Changes the snake's direction to up if it's not already moving down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the snake's direction to down if it's not already moving up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the snake's direction to left if it's not already moving right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the snake's direction to right if it's not already moving left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_speed(self):
        """
        Increases the speed of the snake by increasing the move distance.
        """
        self.move_distance += 10

    def decrease_speed(self):
        """
        Decreases the speed of the snake by decreasing the move distance.
        """
        if self.move_distance > 1:
            self.move_distance -= 5
