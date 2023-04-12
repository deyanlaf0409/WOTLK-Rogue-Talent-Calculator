from tkinter import *
from tktooltip import ToolTip
from Src.points_count import *
from PIL import ImageTk, Image
from Combat.resources import dictionaries

# Create a window
window = Tk()
window.title("Combat")
background_clr = '#1a1a1a'
button_clr = '#0d0d0d'
window.configure(background=background_clr)
desc = dictionaries
path = "resources/images/"

image_1 = ImageTk.PhotoImage(Image.open(path + "ability_gouge.jpg"))
image_2 = ImageTk.PhotoImage(Image.open(path + "spell_shadow_ritualofsacrifice.jpg"))
image_3 = ImageTk.PhotoImage(Image.open(path + "ability_dualwield.jpg"))

# Create a label for displaying the available points
available_points_label = Label(window, text=f"Available Points: {AVAILABLE_POINTS}")
available_points_label.grid(row=ROWS, column=0, columnspan=COLS)

# Create a grid of buttons
for row in range(ROWS):
    for col in range(COLS):
        # Create a frame to hold the button and counter
        frame = Frame(window, width=50, height=50, bg=background_clr)
        frame.grid(row=row, column=col, padx=5, pady=5)

        # Create the button
        if row == 0 and col == 0:
            button = Button(frame, image=image_1, width=50, height=50, bg=button_clr)
            desc = dictionaries.description1
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        elif row == 0 and col == 1:
            button = Button(frame, image=image_2, width=50, height=50, bg=button_clr)
            desc = dictionaries.description2
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        elif row == 0 and col == 2:
            button = Button(frame, image=image_3, width=50, height=50, bg=button_clr)
            desc = dictionaries.description3
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = Label(frame, text="0/5", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        else:
            button = Button(frame, width=6, height=3, bg=button_clr)

        button.pack(side=LEFT)
        button.bind("<Button-1>", lambda event, row=row, desc=desc, btn=button: increase_counter(event, btn,
                                                                                                 available_points_label,
                                                                                                 row, desc))

        button.bind("<Button-3>",
                    lambda event, row=row, desc=desc: decrement_counter(event, row, desc, available_points_label))

# Start the main event loop
window.mainloop()
