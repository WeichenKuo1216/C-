import curses
import random
import time

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialize game variables
snake_x = sw // 4
snake_y = sh // 2
snake = [[snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]]

food = [sh // 2, sw // 2]
special_food = None
obstacles = []
obstacles_count = (sh * sw) // 20

score_normal_food = 0
score_special_food = 0

# Initialize game settings
direction = curses.KEY_RIGHT
pause = False
game_over = False

# Function to generate food
def generate_food():
    global food
    while True:
        food = [random.randint(1, sh-2), random.randint(1, sw-2)]
        if food not in snake and food != special_food:
            break

# Function to generate special food
def generate_special_food():
    global special_food
    while True:
        special_food = [random.randint(1, sh-2), random.randint(1, sw-2)]
        if special_food not in snake and special_food != food:
            break

# Function to generate obstacles
def generate_obstacles():
    global obstacles
    obstacles = []
    obstacle_size = 1  # Minimum number of consecutive cells for an obstacle
    max_obstacle_size = min(sw, sh) // 4  # Maximum obstacle size based on game screen dimensions
    max_obstacle_count = int((sw * sh) * 0.05)  # Adjust the percentage as desired
    obstacle_count = random.randint(1, max_obstacle_count)
    for _ in range(obstacle_count):
        obstacle_direction = random.choice(["horizontal", "vertical"])
        if obstacle_direction == "horizontal":
            max_x = sw - obstacle_size - 1
            if max_x <= 0:
                continue
            obstacle_x = random.randint(1, max_x)
            obstacle_y = random.randint(1, sh - 2)
            for i in range(obstacle_size):
                obstacles.append([obstacle_y, obstacle_x + i])
        else:
            max_y = sh - obstacle_size - 1
            if max_y <= 0:
                continue
            obstacle_x = random.randint(1, sw - 2)
            obstacle_y = random.randint(1, max_y)
            for i in range(obstacle_size):
                obstacles.append([obstacle_y + i, obstacle_x])




generate_obstacles()

# Game loop
while not game_over:
    if not pause:
        # Get user input
        next_key = w.getch()
        direction = direction if next_key == -1 else next_key
        #generate obstacles
        
        # Update snake position based on direction
        snake.insert(0, [snake[0][0] + (direction == curses.KEY_DOWN and 1) + (direction == curses.KEY_UP and -1),
                         snake[0][1] + (direction == curses.KEY_RIGHT and 1) + (direction == curses.KEY_LEFT and -1)])

        # Check for collision with food
        if snake[0] == food:
            score_normal_food += 1
            generate_food()
        else:
            snake.pop()

        # Check for collision with special food
        if snake[0] == special_food:
            if len(snake) > 1:
                score_special_food += 1
                snake.pop()
                generate_special_food()

        # Check for collision with obstacles
        if snake[0] in obstacles:
            game_over = True
            end_reason = "Snake collided with an obstacle."

        # Check for collision with self
        if snake[0] in snake[1:]:
            game_over = True
            end_reason = "Snake collided with itself."

        # Check for out-of-bounds collision (wrap around the screen)
        if snake[0][0] == 0:
            snake[0][0] = sh - 2
        elif snake[0][0] == sh - 1:
            snake[0][0] = 1
        elif snake[0][1] == 0:
            snake[0][1] = sw - 2
        elif snake[0][1] == sw - 1:
            snake[0][1] = 1

    # Clear the screen
    w.clear()

    # Draw the snake
    # Draw the snake
    for i, c in enumerate(snake):
        if i == 0:
            w.addch(c[0], c[1], curses.ACS_DIAMOND)
            
        else:
            w.addch(c[0], c[1], curses.ACS_CKBOARD)


    # Draw the food
    w.addch(food[0], food[1], curses.ACS_PI)

    # Draw the special food
    if special_food is not None:
        w.addch(special_food[0], special_food[1], curses.ACS_CKBOARD)


    # Draw the obstacles
    for o in obstacles:
        w.addch(o[0], o[1], " ", curses.A_REVERSE)

    # Display scores
    w.addstr(0, sw // 2 - 5, f"Score: {score_normal_food} (N) {score_special_food} (S)")

    # Display game over message if the game is over
    if game_over:
        w.addstr(sh // 2, sw // 2 - len(end_reason) // 2, end_reason)
    else:
        # Display pause message if the game is paused
        if pause:
            w.addstr(sh // 2, sw // 2 - 4, "Paused")

    # Refresh the screen
    w.refresh()

    # Adjust game speed based on snake length
    time.sleep(0.1 - (len(snake) // 30))

    # Handle user input for pause/resume
    if next_key == ord(' '):
        pause = not pause

# End the game
time.sleep(2)
curses.endwin()
print(f"Normal Food Eaten: {score_normal_food}")
print(f"Special Food Eaten: {score_special_food}")
print(f"Game Over: {end_reason}")
