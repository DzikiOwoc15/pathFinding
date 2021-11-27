import time
import tkinter
from tkinter import RIGHT, X, TOP, BOTTOM, LEFT, RAISED, SUNKEN
import pyautogui

# Basic variables

# buttons grid is a list containing all buttons for a future reference
buttons_grid = []
# state matrix is a list containing states of all matrix buttons (clicked or not)
# False meaning not pressed
state_matrix = []
move_list = []
rows = 10
columns = 10
button_height = 2
button_width = 5
start_x = None
start_y = None
finish_x = None
finish_y = None
is_window_maximized = False
is_set_start_button_pressed = False
is_set_finish_button_pressed = False
default_geometry = '900x1000'

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


def calc_path():
    # TODO FINISH THIS
    global finish_x, finish_y, start_y, start_x, move_list
    # Create seen matrix
    seen = []
    for row in range(rows + 1):
        temp = []
        for col in range(columns + 1):
            temp.append(False)
        seen.append(temp)
    # Check each cell
    move_list = []
    move_list.append((finish_x, finish_y, 0))
    seen[finish_x][finish_y] = True
    for move in move_list:
        check_adjacent_cells(move, seen)


def check_adjacent_cells(move, seen):
    current_x = move[0]
    current_y = move[1]
    counter = move[2]
    global move_list
    # Check up
    if current_x - 1 >= 0:
        if not matrix_list[current_x - 1][current_y] and not seen[current_x - 1][current_y]:
            move_list.append((current_x - 1, current_y, counter + 1))
            seen[current_x - 1][current_y] = True
    # Check down
    if current_x + 1 < len(matrix_list):
        if not matrix_list[current_x - 1][current_y] and not seen[current_x + 1][current_y]:
            move_list.append((current_x + 1, current_y, counter + 1))
            seen[current_x + 1][current_y] = True
    # Check left
    if current_y - 1 >= 0:
        if not matrix_list[current_x][current_y - 1] and not seen[current_x][current_y - 1]:
            move_list.append((current_x, current_y - 1, counter + 1))
            seen[current_x][current_y - 1] = True
    # Check right
    if current_y + 1 < len(matrix_list[current_x]):
        if not matrix_list[current_x][current_y + 1] and not seen[current_x][current_y - 1]:
            move_list.append((current_x, current_y + 1, counter + 1))
            seen[current_x][current_y + 1] = True


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


def set_start_button_click(self, button_to_unclick):
    global is_set_start_button_pressed, is_set_finish_button_pressed
    if is_set_start_button_pressed:
        is_set_start_button_pressed = False
        self.config(relief=RAISED)
    else:
        # Unclick the finish button
        is_set_finish_button_pressed = False
        button_to_unclick.config(relief=RAISED)
        # Click the start button
        is_set_start_button_pressed = True
        self.config(relief=SUNKEN)


def set_finish_button_click(self, button_to_unclick):
    global is_set_finish_button_pressed, is_set_start_button_pressed
    if is_set_finish_button_pressed:
        is_set_finish_button_pressed = False
        self.config(relief=RAISED)
    else:
        # Unclick the start button
        button_to_unclick.config(relief=RAISED)
        is_set_start_button_pressed = False
        # Click the finish button
        is_set_finish_button_pressed = True
        self.config(relief=SUNKEN)


# Function to change color and state when button is clicked
def matrix_button_click(x_axis, y_axis):
    # TODO FIX BUG - CLICKING ON A FINISH/START BUTTON CHANGES COLOR BUT DOES NOT REMOVE POSITION VARIABLES
    global is_set_start_button_pressed, start_x, start_y, finish_x, finish_y
    current_button = buttons_grid[x_axis - 1][y_axis - 1]
    if not is_set_start_button_pressed and not is_set_finish_button_pressed:
        button_clicked = state_matrix[x_axis - 1][y_axis - 1]
        if not button_clicked:
            state_matrix[x_axis - 1][y_axis - 1] = True
            current_button.config(background=blue_color)
        else:
            state_matrix[x_axis - 1][y_axis - 1] = False
            current_button.config(background=button_color)
    elif is_set_start_button_pressed:
        # Unclick previous start button
        if start_x is not None:
            old_start_button = buttons_grid[start_x][start_y]
            old_start_button.config(background=button_color)
        start_x = x_axis - 1
        start_y = y_axis - 1
        current_button.config(background="green")
    elif is_set_finish_button_pressed:
        # Unclick previous finish button
        if finish_x is not None:
            old_finish_button = buttons_grid[finish_x][finish_y]
            old_finish_button.config(background=button_color)
        finish_x = x_axis - 1
        finish_y = y_axis - 1
        current_button.config(background="red")


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
                             command=lambda: calc_path()).pack()

start_button = tkinter.Button(frame_top)
start_button.pack()
# start_button.bind('<Button-1>', set_start_button_click(start_button))
finish_button = tkinter.Button(frame_top)
finish_button.pack()

finish_button.config(bg="red", text="Set Finish",
                     activebackground="red",
                     command=lambda self=finish_button, button_to_unclick=start_button:
                     set_finish_button_click(self, start_button))
start_button.config(bg="green", text="Set start",
                    command=lambda self=start_button, button_to_unclick=finish_button:
                    set_start_button_click(self, button_to_unclick),
                    activebackground="green")

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
                                    command=lambda z=x, w=y: matrix_button_click(z, w))
            button.grid(row=x, column=y)
            button_list.append(button)
    if len(button_list) != 0:
        state_matrix.append(matrix_list)
        buttons_grid.append(button_list)

window.mainloop()
