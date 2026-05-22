import random  # يجب استخدام "random" بحروف صغيرة
import curses

# Initialize curses library to create our screen
screen = curses.initscr()

# Hide the mouse cursor
curses.curs_set(0)

# Get the max screen height and width
height_screen, width_screen = screen.getmaxyx()

# Create new window
window = curses.newwin(height_screen, width_screen, 0, 0)

# Allow window to receive input from the keyboard
window.keypad(1)

# Set the delay for updating the screen
window.timeout(100)

# Set the x, y coordinates of the initial position of the snake's head
snk_x = width_screen // 4
snk_y = height_screen // 2

# Define the initial position of the snake body
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

# Create the food in the middle of the window
food = [height_screen // 2, width_screen // 2]

# Add the food using the PI character from the curses module
window.addch(food[0], food[1], curses.ACS_PI)

# Set the initial movement direction to right
key = curses.KEY_RIGHT

# Create the game loop that loops forever until the player loses or quits the game
while True:
    # Get the next key that will be pressed by user
    next_key = window.getch()

    # If user doesn't input anything, key remains the same; else key will be set to the new pressed key
    key = key if next_key == -1 else next_key

    # Check if the snake collided with the walls or itself
    if (snake[0][0] in [0, height_screen] or
        snake[0][1] in [0, width_screen] or
        snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Set the new position of the snake's head based on the direction
    new_head = [snake[0][0], snake[0][1]]  # يجب أن تكون قائمة لتعديلها

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # Insert the new head at the first position of the snake list
    snake.insert(0, new_head)

    # Check if the snake ate the food
    if snake[0] == food:  # هذا السطر يجب أن يكون بشكل صحيح
        food = None
        while food is None:
            new_food = [random.randint(1, height_screen - 1), random.randint(1, width_screen - 1)]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Remove the last part of the snake's tail
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Draw the snake's new head
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
