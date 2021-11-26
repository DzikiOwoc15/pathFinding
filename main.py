import time
import tkinter
from tkinter import RIGHT, X, TOP, BOTTOM, LEFT, RAISED, SUNKEN
import pyautogui

# Basic variables

# buttons grid is a list containing all buttons for a future reference
buttons_grid = []
# state matrix is a list containing states of all buttons (clicked or not)
# False meaning not pressed
state_matrix = []
rows = 10
columns = 10
button_height = 2
button_width = 5
start_x = None
start_y = None
is_window_maximized = False
is_set_start_button_pressed = False
is_set_finish_button_pressed = False
default_geometry = '900x1000'
window_previous_y = 0
window_previous_x = 0

# Define colors used
title_bar_color = "#121212"
background_color = "#1a1a1a"
blue_color = "#2962ff"
button_color = "#242424"
button_clicked_color = "#303030"

# Init window
window = tkinter.Tk()
window.configure(bg=background_color)

# Make a custom title bar
window.overrideredirect(True)
window.geometry(default_geometry)


def calc_path(grid):
    # TODO CREATE ALGORITHM THAT FINDS THE SHORTEST PATH
    foo = "foo"
    # do sth
    # do more


def move_window(event):
    start_x_pos = event.x_root
    start_y_pos = event.y_root
    time.sleep(0.0000000001)
    current_window_x = window.winfo_x()
    current_window_y = window.winfo_y()
    position = pyautogui.position()
    end_x = position[0]
    end_y = position[1]
    difference_x = end_x - start_x_pos
    difference_y = end_y - start_y_pos
    window.geometry('+{0}+{1}'.format(current_window_x + difference_x, current_window_y + difference_y))


def maximize_window():
    global is_window_maximized
    if is_window_maximized:
        window.geometry(default_geometry)
        window.state('normal')
        is_window_maximized = False
    else:
        window.state('zoomed')
        is_window_maximized = True


def set_start_button_click(self):
    global is_set_start_button_pressed, is_set_finish_button_pressed
    if is_set_start_button_pressed:
        print("button unclicked")
        is_set_start_button_pressed = False
        self.config(relief=RAISED)
    else:
        print("button clicked")
        is_set_start_button_pressed = True
        self.config(relief=SUNKEN)


def set_finish_button(self):
    global is_set_finish_button_pressed, is_set_start_button_pressed
    if is_set_finish_button_pressed:
        is_set_finish_button_pressed = False
        self.config(relief=RAISED)
    else:
        # TODO ONLY ONE BUTTON CAN BE SUNKEN AT THE SAME TIME
        is_set_finish_button_pressed = True
        self.config(relief=SUNKEN)


# Function to change color and state when button is clicked
def button_click(x_axis, y_axis):
    global is_set_start_button_pressed, start_x, start_y
    current_button = buttons_grid[x_axis - 1][y_axis - 1]
    if not is_set_start_button_pressed:
        button_clicked = state_matrix[x_axis - 1][y_axis - 1]
        if not button_clicked:
            state_matrix[x_axis - 1][y_axis - 1] = True
            current_button.config(background=blue_color)
        else:
            state_matrix[x_axis - 1][y_axis - 1] = False
            current_button.config(background=button_color)
    else:
        # TODO COMPLETE SET START
        start_x = x_axis - 1
        start_y = y_axis - 1
        current_button.config(background="green")


# initialize items on a title bar
title_bar = tkinter.Frame(window, bg=title_bar_color, relief="raised")
close_button = tkinter.Button(title_bar, text="X", command=window.destroy, bg=title_bar_color, fg="white",
                              borderwidth=0, activebackground=button_clicked_color, pady=3, padx=3)
maximize_button = tkinter.Button(title_bar, text="[  ]", command=maximize_window, bg=title_bar_color, fg="white",
                                 borderwidth=0, activebackground=button_clicked_color, pady=3, padx=3)
title_label = tkinter.Label(title_bar, bg=title_bar_color, text="PathFinding GUI", fg="white", borderwidth=0,
                            pady=3, padx=10)
python_logo = tkinter.PhotoImage(file="assets/python_small_logo.png")
logo_label = tkinter.Label(title_bar, bg=title_bar_color, borderwidth=0, image=python_logo)

# place items on a title bar
logo_label.pack(side=LEFT, padx=5)
title_bar.pack(side=TOP, expand=False, fill=X)
close_button.pack(side=RIGHT)
maximize_button.pack(side=RIGHT)
title_label.pack(side=LEFT)
title_bar.bind('<B1-Motion>', move_window)
title_label.bind('<B1-Motion>', move_window)
logo_label.bind('<B1-Motion>', move_window)

# TODO REMAKE TOP FRAME LAYOUT (MAKE IT PRETTIER)
# Define top frame (play button etc)
frame_top = tkinter.Frame(window)
frame_top.pack(side=TOP, pady=25)
frame_top.config(bg=background_color)

# Define bottom frame (main grid)
frame_bottom = tkinter.Frame(window)
frame_bottom.pack(side=BOTTOM, fill=None, expand=1, pady=25)
frame_bottom.config(bg=background_color)

play_button_image = tkinter.PhotoImage(file="assets/baseline_play_circle_white_24dp.png")
play_button = tkinter.Button(frame_top, image=play_button_image, bg=background_color, highlightthickness=0, bd=0,
                             activebackground=background_color,
                             command=lambda grid=state_matrix: calc_path(grid)).pack()
start_button = tkinter.Button(frame_top)
start_button.pack()
start_button.config(bg="green", text="Set start",
                    command=lambda self=start_button:
                    set_start_button_click(self),
                    activebackground="green")
start_button.bind('<Button-1>', set_start_button_click(start_button))
finish_button = tkinter.Button(frame_top)
finish_button.pack()
finish_button.config(bg="red", text="Set Finish",
                     activebackground="red",
                     command=lambda self=finish_button:
                     set_finish_button(self))

# Draw the board (Including the row and column labels)
for x in range(rows + 1):
    button_list = []
    matrix_list = []
    for y in range(columns + 1):
        # Draw row and column labels
        if x == 0 or y == 0:
            label_template = "{}"
            label_text = ""
            if x == 0 and y != 0:
                label_text = label_template.format(y)
            elif y == 0 and x != 0:
                label_text = label_template.format(x)
            tkinter.Label(frame_bottom, text=label_text, bg=background_color, fg="white").grid(row=x, column=y)
        # Draw buttons
        else:
            matrix_list.append(False)
            button = tkinter.Button(frame_bottom, bg=button_color, activebackground=button_clicked_color,
                                    height=button_height, width=button_width,
                                    command=lambda z=x, w=y: button_click(z, w))
            button.grid(row=x, column=y)
            button_list.append(button)
    if len(button_list) != 0:
        state_matrix.append(matrix_list)
        buttons_grid.append(button_list)

window.mainloop()
