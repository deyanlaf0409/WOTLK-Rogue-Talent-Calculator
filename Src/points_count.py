
ROWS = 11
COLS = 4
AVAILABLE_POINTS = 80
total_points = 0

# Define a function to update the button counter
def update_counter(button, available_points_label):
    global total_points, AVAILABLE_POINTS

    # Get the current counter value from the counter label widget
    count = int(button.counter["text"])

    # If total points exceed the maximum, prevent further increment
    if total_points >= 80:
        return

    # Increment the counter value
    count += 1

    # Update the counter label widget to show the new counter value
    button.counter["text"] = str(count)

    # Update the total points
    total_points += 1
    AVAILABLE_POINTS -= 1

    available_points_label.config(text=f"Available Points: {AVAILABLE_POINTS}")
