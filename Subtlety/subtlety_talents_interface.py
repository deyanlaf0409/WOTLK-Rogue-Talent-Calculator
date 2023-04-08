import tkinter as tk
from tktooltip import ToolTip
from PIL import ImageTk, Image
from Descriptions import dictionaries
from Src.points_count import *

# Create a window
window = tk.Tk()
window.title("Button Grid")
background_clr = '#1a1a1a'
button_clr = '#0d0d0d'
window['background'] = background_clr

# Define the images for each button
image_1 = ImageTk.PhotoImage(Image.open("Images/ability_warrior_decisivestrike.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("Images/spell_shadow_charm.jpg"))
image_3 = ImageTk.PhotoImage(Image.open("Images/ability_warrior_warcry.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("Images/ability_rogue_feint.jpg"))
image_5 = ImageTk.PhotoImage(Image.open("Images/ability_sap.jpg"))
image_6 = ImageTk.PhotoImage(Image.open("Images/ability_stealth.jpg"))
image_7 = ImageTk.PhotoImage(Image.open("Images/spell_magic_lesserinvisibilty.jpg"))
image_8 = ImageTk.PhotoImage(Image.open("Images/spell_shadow_curse.jpg"))
image_9 = ImageTk.PhotoImage(Image.open("Images/inv_sword_17.jpg"))
image_10 = ImageTk.PhotoImage(Image.open("Images/spell_nature_mirrorimage.jpg"))
image_11 = ImageTk.PhotoImage(Image.open("Images/spell_shadow_fumble.jpg"))
image_12 = ImageTk.PhotoImage(Image.open("Images/ability_rogue_ambush.jpg"))


# Create a label for displaying the available points
available_points_label = tk.Label(window, text=f"Available Points: {AVAILABLE_POINTS}")
available_points_label.grid(row=ROWS, column=0, columnspan=COLS)
desc = dictionaries
# Create a grid of buttons
for row in range(ROWS):
    for col in range(COLS):
        # Create a frame to hold the button and counter
        frame = tk.Frame(window, width=50, height=50, bg=background_clr)
        frame.grid(row=row, column=col, padx=5, pady=5)

        # Create the button
        if row == 0 and col == 0:
            button = tk.Button(frame, image=image_1, width=50, height=50, bg=button_clr)
            desc = dictionaries.description1
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = tk.Label(frame, text="0/5", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        elif row == 0 and col == 1:
            button = tk.Button(frame, image=image_2, width=50, height=50, bg=button_clr)
            desc = dictionaries.description2
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = tk.Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        elif row == 0 and col == 2:
            button = tk.Button(frame, image=image_3, width=50, height=50, bg=button_clr)
            desc = dictionaries.description3
            info = ToolTip(button, msg=desc[1], parent_kwargs={"bg": "black"}, fg="#ffffff", bg="#1c1c1c")
            counter = tk.Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
            button.info = info
        elif row == 1 and col == 0:
            button = tk.Button(frame, image=image_4, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 1 and col == 1:
            button = tk.Button(frame, image=image_5, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 1 and col == 2:
            button = tk.Button(frame, image=image_6, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 2 and col == 0:
            button = tk.Button(frame, image=image_7, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 2 and col == 1:
            button = tk.Button(frame, image=image_8, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/1", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 2 and col == 2:
            button = tk.Button(frame, image=image_9, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 3 and col == 0:
            button = tk.Button(frame, image=image_10, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 3 and col == 1:
            button = tk.Button(frame, image=image_11, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/3", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        elif row == 3 and col == 2:
            button = tk.Button(frame, image=image_12, width=50, height=50, bg=button_clr)
            counter = tk.Label(frame, text="0/2", width=2, height=1, bg="gray", fg="white")
            counter.pack(side=tk.RIGHT, anchor="se")
            button.counter = counter
        else:
            button = tk.Button(frame, width=6, height=3, bg=button_clr)

        button.pack(side=tk.LEFT)
        button.config(command=lambda row=row, desc=desc, btn=button: update_counter(btn, available_points_label, row, desc))


# Start the main event loop
window.mainloop()
