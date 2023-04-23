from tkinter import Tk, Label, Button


ROWS = 11
COLS = 4
AVAILABLE_POINTS = 71
total_points = 0
GUI_LIST = []


def update_available_points_label(new_value):
    available_points_label.config(text=f"Available Points: {new_value}")


def reset_counters():
    for gui in GUI_LIST:
        for button in gui.buttons:
            count = int(button.counter["text"].split('/')[0])
            max_count = int(button.counter["text"].split('/')[1])
            button.counter["text"] = f"0/{max_count}"


def reset():
    AVAILABLE_POINTS = 71
    total_points = 0
    update_available_points_label(AVAILABLE_POINTS)
    reset_counters()


root = Tk()
root.title("Control Panel")
root.configure(background='#1a1a1a')
root.geometry("300x200+1200+0")

available_points_label = Label(root, text=f"Available Points: {AVAILABLE_POINTS}")
available_points_label.grid(row=0, column=0, columnspan=1)

reset_button = Button(root, text="Reset", command=reset)
reset_button.grid(row=1, column=0)
