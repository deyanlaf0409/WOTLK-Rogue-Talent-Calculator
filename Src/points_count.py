
ROWS = 11
COLS = 4
total_points = 0


class SharedData:
    def __init__(self, AVAILABLE_POINTS):
        self.AVAILABLE_POINTS = AVAILABLE_POINTS

    def increment_points(self):
        self.AVAILABLE_POINTS -= 1

    def decrement_points(self):
        self.AVAILABLE_POINTS += 1


shared_data = SharedData(71)


def increase_counter(event, button, available_points_label, row, desc):
    global total_points
    button = event.widget

    # Get the current counter value from the counter label widget
    count = int(button.counter["text"].split('/')[0])
    max_count = int(button.counter["text"].split('/')[1])

    # If there are available points and the row points are less than or equal to the available points,
    # and the total points is greater than or equal to the required points for the current row, increment the counter
    if shared_data.AVAILABLE_POINTS > 0 and total_points >= (row*5) and count < max_count:
        total_points += 1
        shared_data.AVAILABLE_POINTS -= 1
        count += 1
    else:
        return


    # Update the counter label widget to show the new counter value
    button.counter["text"] = f"{count}/{max_count}"
    available_points_label.config(text=f"Available Points: {shared_data.AVAILABLE_POINTS}")
    button.info.msg = desc[count]


def decrement_counter(event, row,  desc, available_points_label):
    global total_points
    # Get the button that was clicked
    button = event.widget
    count = int(button.counter["text"].split('/')[0])
    max_count = int(button.counter["text"].split('/')[1])
    # next_row_required_points = (row+1)*5

    # total_points <= next_row_required_points

    # Decrement the counter if it's greater than zero
    if int(count) > 0:
        new_value = str(int(count) - 1) + button.counter["text"][1:]
        total_points -= 1
        shared_data.AVAILABLE_POINTS += 1
        count -= 1
        button.counter.config(text=new_value)
    else:
        return

    button.counter["text"] = f"{count}/{max_count}"
    available_points_label.config(text=f"Available Points: {shared_data.AVAILABLE_POINTS}")
    button.info.msg = desc[count]
