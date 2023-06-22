from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from lives import Lives
from badfood import BadFood
from mysterybox import MysteryBox
from mysteryMessage import MysteryMessage
from levels import Levels
import random
import time

# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize game objects
snake = Snake()
food = Food()
badfood1 = BadFood()
badfood2 = BadFood()
badfood3 = BadFood()
scoreboard = Scoreboard()
lives = Lives()
mysteryMessage = MysteryMessage()
mysterybox = MysteryBox(snake, mysteryMessage, scoreboard, lives)

# Set up keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize variables
updated_badfoods = False
updated_badfoods2 = False
num_badfoods = 3
badfoods = [badfood1, badfood2, badfood3]


# Puts all three badfoods in a random location every 3 seconds
def move_badfood():
    for Abadfood in badfoods:
        Abadfood.random_start()
    screen.ontimer(move_badfood, 3000)  # Call move_badfood function again after 3 seconds (3000 milliseconds)


# Moves the mystery box to a random location every 3 seconds
def move_mysterybox():
    mysterybox.random_start()
    screen.ontimer(move_mysterybox, 3000)  # Call move_mysterybox function again after 3 seconds (3000 milliseconds)


# Initialize game levels
levels = Levels()
levels.print_level()
move_badfood()
move_mysterybox()

quickness = 0.1
gameOn = True

# Game loop
while gameOn:
    screen.update()
    time.sleep(quickness)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score(1)
        snake.extend()

    # Level 2: Increase number of badfoods and speed of snake (update speed of screen - quickness)
    if scoreboard.score >= 5 and not updated_badfoods:
        num_badfoods += 2
        levels.level = 2
        levels.color("green")
        levels.print_level()  # Print level 2 to the screen
        updated_badfoods = True
        quickness = 0.05

        for _ in range(num_badfoods - len(badfoods)):
            new_badfood = BadFood()
            badfoods.append(new_badfood)

    # Level 3: Increase number of badfoods and speed of snake (update speed of screen - quickness)
    if scoreboard.score >= 10 and not updated_badfoods2:
        num_badfoods += 2
        levels.level = 3
        levels.color("red")
        levels.print_level()  # Print level 3 to the screen
        updated_badfoods2 = True
        quickness = 0.025

        for _ in range(num_badfoods - len(badfoods)):
            new_badfood = BadFood()
            badfoods.append(new_badfood)

    # Detect collision with badfood
    for Abadfood in badfoods:
        if snake.head.distance(Abadfood) < 20:
            Abadfood.random_start()
            lives.decrease_lives(1)
            scoreboard.decrease_score(2)

    # Activate a random powerup from the mystery box
    if snake.head.distance(mysterybox) < 30:
        randNum = random.randint(0, 5)
        randPowerup = mysterybox.powerups[randNum]
        randPowerup()
        mysterybox.random_start()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameOn = False
        scoreboard.game_over()
        print("Game Over!")

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            scoreboard.game_over()

    # Detect if lives == 0; if so, end the game
    if lives.lives == 0:
        gameOn = False
        scoreboard.game_over()
        print("Ran out of lives!")

    # Check if the player achieved the winning score
    if scoreboard.score >= 15:
        gameOn = False
        scoreboard.game_won()
        print("You won!")

# Exit the game when the screen is clicked
screen.exitonclick()
