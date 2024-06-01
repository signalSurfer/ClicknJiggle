import pyautogui
import random
import time

def is_outside_jiggler_zone(x, y, jiggler_zone):
    # Check if the mouse position is outside the jiggler zone
    return x < jiggler_zone['min_x'] or x > jiggler_zone['max_x'] or y < jiggler_zone['min_y'] or y > jiggler_zone['max_y']

# Get the initial mouse position
initial_x, initial_y = pyautogui.position()

# Set the range of coordinates for the mouse movement (20 pixels in each direction)
jiggler_zone = {
    'min_x': initial_x - 20,
    'max_x': initial_x + 20,
    'min_y': initial_y - 20,
    'max_y': initial_y + 20
}

# Set the range of intervals for mouse movement and clicks
min_interval, max_interval = 0.1, 0.5
min_click_interval, max_click_interval = 30, 45

# Set the range for the number of frantic clicks
min_clicks, max_clicks = 2, 5

# Continuously move the mouse and perform random clicks within the defined range
while True:
    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Check if the mouse is outside the jiggler zone
    if is_outside_jiggler_zone(current_x, current_y, jiggler_zone):
        print("Mouse moved outside the jiggler zone. Pausing mouse jiggler for 1 minute.")
        time.sleep(60)  # Pause for 1 minute
        print("Resuming mouse jiggler.")
        pyautogui.moveTo(initial_x, initial_y)  # Move the cursor back to the starting position

    # Generate random coordinates within the jiggler zone
    x = random.randint(jiggler_zone['min_x'], jiggler_zone['max_x'])
    y = random.randint(jiggler_zone['min_y'], jiggler_zone['max_y'])

    # Move the mouse to the random coordinates within the jiggler zone
    pyautogui.moveTo(x, y, duration=0.25)

    # Generate a random interval for the next mouse movement
    interval = random.uniform(min_interval, max_interval)

    # Wait for the random interval before the next movement
    time.sleep(interval)

    # Generate a random interval for the next mouse click
    click_interval = random.uniform(min_click_interval, max_click_interval)

    # Perform frantic clicks if the click interval has passed
    if time.time() % click_interval < 0.5:
        # Generate a random number of clicks between min_clicks and max_clicks
        num_clicks = random.randint(min_clicks, max_clicks)
        for _ in range(num_clicks):
            pyautogui.click()
            time.sleep(0.1)