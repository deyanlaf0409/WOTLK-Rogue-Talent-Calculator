from shared_data import *
from tkinter import Toplevel
from Combat.combat_talents_interface import CombatGUI
from Subtlety.subtlety_talents_interface import SubtletyGUI
from Assassination.assassination_talents_interface import AssassinationGUI


# Create the windows
subtlety_window = Toplevel(root)
combat_window = Toplevel(root)
assassination_window = Toplevel(root)

# Set the positions of the windows
subtlety_window.geometry("400x800+800+0")
combat_window.geometry("400x800+400+0")
assassination_window.geometry("400x800+0+0")

# Create the GUI objects and pass in the windows
subtlety_gui = SubtletyGUI(subtlety_window)
combat_gui = CombatGUI(combat_window)
assassination_gui = AssassinationGUI(assassination_window)

root.mainloop()
