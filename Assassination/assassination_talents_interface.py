# AssassinationGUI
from tkinter import *
from tktooltip import ToolTip
from PIL import ImageTk, Image
from Src.points_count import *
from Assassination.resources import dictionaries


class AssassinationGUI:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Assassination")
        parent.configure(background='#1a1a1a')
        desc = dictionaries

        self.path = "Assassination/resources/images/"
        self.images = []
        for filename in ["ability_rogue_eviscerate.jpg", "ability_fiegndead.jpg", "ability_racial_bloodrage.jpg",
                         "ability_druid_disembowel.jpg", "ability_rogue_bloodsplatter.jpg", "ability_backstab.jpg"]:
            self.images.append(ImageTk.PhotoImage(Image.open(self.path + filename)))


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
                    button = Button(frame, image=self.images[0], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description1
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                elif row == 0 and col == 1:
                    button = Button(frame, image=self.images[1], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description2
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                elif row == 0 and col == 2:
                    button = Button(frame, image=self.images[2], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description3
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/5", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                elif row == 1 and col == 0:
                    button = Button(frame, image=self.images[3], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description4
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                elif row == 1 and col == 1:
                    button = Button(frame, image=self.images[4], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description5
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                elif row == 1 and col == 3:
                    button = Button(frame, image=self.images[5], width=50, height=50, bg='#0d0d0d')
                    desc = dictionaries.description6
                    info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
                    counter = Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                else:
                    button = Button(frame, width=6, height=3, bg='#0d0d0d')

                button.pack(side=LEFT)
                button.bind("<Button-1>", lambda event, row=row, desc=desc, btn=button: increase_counter(event, btn, self.available_points_label, row, desc))
                button.bind("<Button-3>", lambda event, row=row, desc=desc: decrement_counter(event, row, desc, self.available_points_label))
                GUI_LIST.append(self)



