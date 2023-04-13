# CombatGUI.py
from tkinter import *
from tktooltip import ToolTip
from PIL import ImageTk, Image
from Src.points_count import *
from Combat.resources import dictionaries


class CombatGUI:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Combat")
        parent.configure(background='#1a1a1a')
        self.desc = dictionaries
        self.path = "Combat/resources/images/"

        self.image_1 = ImageTk.PhotoImage(Image.open(self.path + "ability_gouge.jpg"))

        # Create a label for displaying the available points
        self.available_points_label = Label(parent, text=f"Available Points: {shared_data.AVAILABLE_POINTS}")
        self.available_points_label.grid(row=ROWS, column=0, columnspan=COLS)

        # Create a grid of buttons
        for row in range(ROWS):
            for col in range(COLS):
                # Create a frame to hold the button and counter
                frame = Frame(parent, width=50, height=50, bg='#1a1a1a')
                frame.grid(row=row, column=col, padx=5, pady=5)

                # Create the button
                if row == 0 and col == 0:
                    button = Button(frame, image=self.image_1, width=50, height=50, bg='#0d0d0d')
                    self.desc = dictionaries.description1
                    info = ToolTip(button, msg=self.desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                else:
                    button = Button(frame, width=6, height=3, bg='#0d0d0d')

                button.pack(side=LEFT)
                button.bind("<Button-1>", lambda event, row=row, desc=self.desc, btn=button: increase_counter(event, btn, self.available_points_label, row, self.desc))
                button.bind("<Button-3>", lambda event, row=row, desc=self.desc: decrement_counter(event, row, self.desc, self.available_points_label))
                GUI_LIST.append(self)