import tkinter
from tkinter import RIGHT, BOTH, X, TOP, BOTTOM, CENTER, LEFT

# Basic variables
buttons_grid = []
rows = 10
columns = 10
button_height = 3
button_width = 5
is_window_maximized = False

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
window.geometry('700x650')


def mouse_click(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


def move_window(event):
    x = event.x
    y = event.y
    window.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


def maximize_window():
    global is_window_maximized
    if is_window_maximized:
        window.geometry('700x650')
        window.state('normal')
        is_window_maximized = False
    else:
        window.state('zoomed')
        is_window_maximized = True


# initialize items on a title bar
title_bar = tkinter.Frame(window, bg=title_bar_color, relief="raised")
close_button = tkinter.Button(title_bar, text="X", command=window.destroy, bg=title_bar_color, fg="white",
                              borderwidth=0, activebackground=button_clicked_color, pady=3, padx=3)
maximize_button = tkinter.Button(title_bar, text="[  ]", command=maximize_window, bg=title_bar_color, fg="white",
                                 borderwidth=0, activebackground=button_clicked_color, pady=3, padx=3)
title_label = tkinter.Label(title_bar, bg=title_bar_color, text="PathFinding GUI", fg="white", borderwidth=0,
                            pady=3, padx=10)
python_logo = tkinter.PhotoImage(file="python_small_logo.png")
logo_label = tkinter.Label(title_bar, bg=title_bar_color, pady=3, borderwidth=0, padx=10, image=python_logo)


# place items on a title bar
title_bar.pack(side=TOP, expand=False, fill=X)
close_button.pack(side=RIGHT)
maximize_button.pack(side=RIGHT)
title_label.pack(side=LEFT)
logo_label.pack(side=LEFT)
title_bar.bind('<B1-Motion>', move_window)
title_label.bind('<B1-Motion>', move_window)
title_bar.bind('<Button-1>', mouse_click)

# Define top frame (play button etc)
frame_top = tkinter.Frame(window)
frame_top.pack(side=TOP, fill=X)
frame_top.config(bg=background_color)

# Define bottom frame (main grid)
frame_bottom = tkinter.Frame(window)
frame_bottom.pack(side=BOTTOM, fill=None, expand=1, pady=50)
frame_bottom.config(bg=background_color)

play_button = tkinter.Button(frame_top, bg="white", text="P", height=button_height, width=button_width).pack()


# Function to change color when button is clicked
def button_click(x_axis, y_axis):
    current_button = buttons_grid[x_axis - 1][y_axis - 1]
    color = current_button.cget("bg")
    if color != blue_color:
        current_button.config(background=blue_color)
    else:
        current_button.config(background=button_color)


# Draw the board (Including the row and column labels)
for x in range(rows + 1):
    button_list = []
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
            button = tkinter.Button(frame_bottom, bg=button_color, activebackground=button_clicked_color,
                                    height=button_height, width=button_width,
                                    command=lambda z=x, w=y: button_click(z, w))
            button.grid(row=x, column=y)
            button_list.append(button)
    if len(button_list) != 0:
        buttons_grid.append(button_list)

window.mainloop()
