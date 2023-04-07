ROWS = 11
COLS = 4
AVAILABLE_POINTS = 71
total_points = 0


def update_counter(button, available_points_label, row):
    global total_points, AVAILABLE_POINTS
    # print(row)
    row_required_points = row * 5

    # Get the current counter value from the counter label widget
    count = int(button.counter["text"].split('/')[0])
    max_count = int(button.counter["text"].split('/')[1])

    # If there are available points and the row points are less than or equal to the available points,
    # and the total points is greater than or equal to the required points for the current row, increment the counter
    if AVAILABLE_POINTS > 0 and total_points >= row_required_points and count < max_count:
        total_points += 1
        AVAILABLE_POINTS -= 1
        count += 1
    elif count == max_count:
        button['state'] = 'disable'
    else:
        return

    # Update the counter label widget to show the new counter value
    button.counter["text"] = f"{count}/{max_count}"
    available_points_label.config(text=f"Available Points: {AVAILABLE_POINTS}")

