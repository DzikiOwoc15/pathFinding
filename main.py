import tkinter

# Basic variables
from tkinter import RIGHT, BOTH, X, TOP, BOTTOM

buttons_grid = []
rows = 10
columns = 10
button_height = 3
button_width = 5

# Define colors used
background_color = "#1a1a1a"
blue_color = "#2962ff"
button_color = "#242424"
button_clicked_color = "#303030"

# Init window
window = tkinter.Tk()
window.configure(bg=background_color)
window.title("Path Finding GUI")

frame_top = tkinter.Frame(window)
frame_top.pack(side=TOP, fill=X)
frame_top.config(bg=background_color)

frame_bottom = tkinter.Frame(window)
frame_bottom.pack(side=BOTTOM, fill=X)
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
