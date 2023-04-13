from tkinter import Tk, Toplevel
from Combat import combat_talents_interface
from Subtlety import subtlety_talents_interface
from Assassination import assassination_talents_interface

root = Tk()
root.configure(background='#1a1a1a')
# Create the windows
subtlety_window = Toplevel(root)
combat_window = Toplevel(root)
assassination_window = Toplevel(root)

# Set the positions of the windows
subtlety_window.geometry("400x800+620+0")
combat_window.geometry("400x800+310+0")
assassination_window.geometry("400x800+0+0")

# Create the GUI objects and pass in the windows
subtlety_gui = subtlety_talents_interface.SubtletyGUI(subtlety_window)
combat_gui = combat_talents_interface.CombatGUI(combat_window)
assassination_gui = assassination_talents_interface.AssassinationGUI(assassination_window)

root.mainloop()




















