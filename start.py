from tkinter import Tk, Toplevel
from Combat import combat_talents_interface
from Subtlety import subtlety_talents_interface

root = Tk()

subtlety_window = Toplevel(root)
subtlety_gui = subtlety_talents_interface.SubtletyGUI(subtlety_window)

combat_window = Toplevel(root)
combat_gui = combat_talents_interface.CombatGUI(combat_window)

root.mainloop()



















