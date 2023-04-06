from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
ROWS = 11
COLS = 4
AVAILABLE_POINTS = 80

# Define a function to update the button counter
def update_counter(button):
    global total_points, AVAILABLE_POINTS, available_points_label

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


# Create a window
window = tk.Tk()
window.title("Button Grid")

# Define the images for each button
image1 = ImageTk.PhotoImage(Image.open("Images/ability_warrior_decisivestrike.jpg"))
image2 = ImageTk.PhotoImage(Image.open("Images/spell_shadow_charm.jpg"))
image3 = ImageTk.PhotoImage(Image.open("Images/ability_warrior_warcry.jpg"))
image4 = ImageTk.PhotoImage(Image.open("Images/ability_rogue_feint.jpg"))
image5 = ImageTk.PhotoImage(Image.open("Images/ability_sap.jpg"))
image6 = ImageTk.PhotoImage(Image.open("Images/ability_stealth.jpg"))

# Create a grid of buttons
total_points = 0
for row in range(ROWS):
    for col in range(COLS):
        # Create a frame to hold the button and counter
        frame = tk.Frame(window, width=50, height=50)
        frame.grid(row=row, column=col, padx=5, pady=5)

        # Create the button
        if row == 0 and col == 0:
            button = tk.Button(frame, image=image1, width=50, height=50)
        elif row == 0 and col == 1:
            button = tk.Button(frame, image=image2, width=50, height=50)
        elif row == 0 and col == 2:
            button = tk.Button(frame, image=image3, width=50, height=50)
        elif row == 1 and col == 0:
            button = tk.Button(frame, image=image4, width=50, height=50)
        elif row == 1 and col == 1:
            button = tk.Button(frame, image=image5, width=50, height=50)
        elif row == 1 and col == 2:
            button = tk.Button(frame, image=image6, width=50, height=50)
        else:
            button = tk.Button(frame, width=6, height=3)

        button.pack(side=tk.LEFT, padx=5)
        button.config(command=lambda btn=button: update_counter(btn))

        # Create the counter label
        counter = tk.Label(frame, text="0", width=2, height=1, bg="gray", fg="white")
        counter.pack(side=tk.RIGHT, anchor="se")

        # Associate the counter label widget with the button widget
        button.counter = counter

# Create a label for displaying the available points
available_points_label = tk.Label(window, text=f"Available Points: {AVAILABLE_POINTS}")
available_points_label.grid(row=ROWS+1, column=0, columnspan=COLS)

# Start the main event loop
window.mainloop()