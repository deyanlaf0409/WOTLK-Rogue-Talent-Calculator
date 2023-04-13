# SubtletyGUI.py
from tkinter import *
from tktooltip import ToolTip
from PIL import ImageTk, Image
from Src.points_count import *
from Subtlety.resources import dictionaries


class SubtletyGUI:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Subtley")
        parent.configure(background='#1a1a1a')
        self.desc = dictionaries
        self.path = "Subtlety/resources/images/"

        self.image_1 = ImageTk.PhotoImage(Image.open(self.path + "ability_warrior_decisivestrike.jpg"))
        self.image_2 = ImageTk.PhotoImage(Image.open(self.path + "spell_shadow_charm.jpg"))
        self.image_3 = ImageTk.PhotoImage(Image.open(self.path + "ability_warrior_warcry.jpg"))
        self.image_4 = ImageTk.PhotoImage(Image.open(self.path + "ability_rogue_feint.jpg"))
        self.image_5 = ImageTk.PhotoImage(Image.open(self.path + "ability_sap.jpg"))
        self.image_6 = ImageTk.PhotoImage(Image.open(self.path + "ability_stealth.jpg"))
        self.image_7 = ImageTk.PhotoImage(Image.open(self.path + "spell_magic_lesserinvisibilty.jpg"))
        self.image_8 = ImageTk.PhotoImage(Image.open(self.path + "spell_shadow_curse.jpg"))
        self.image_9 = ImageTk.PhotoImage(Image.open(self.path + "inv_sword_17.jpg"))
        self.image_10 = ImageTk.PhotoImage(Image.open(self.path + "spell_nature_mirrorimage.jpg"))
        self.image_11 = ImageTk.PhotoImage(Image.open(self.path + "spell_shadow_fumble.jpg"))
        self.image_12 = ImageTk.PhotoImage(Image.open(self.path + "ability_rogue_ambush.jpg"))

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
                    counter = Label(frame, text="0/5", width=2, height=1, bg="gray", fg="white")
                    counter.pack(side=RIGHT, anchor="se")
                    button.counter = counter
                    button.info = info
                else:
                    button = Button(frame, width=6, height=3, bg='#0d0d0d')

                button.pack(side=LEFT)
                button.bind("<Button-1>", lambda event, row=row, desc=self.desc, btn=button: increase_counter(event, btn, self.available_points_label, row, self.desc))
                button.bind("<Button-3>", lambda event, row=row, desc=self.desc: decrement_counter(event, row, self.desc, self.available_points_label))
                GUI_LIST.append(self)
