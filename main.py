import tkinter

window = tkinter.Tk()
window.title("Path Finding GUI")

buttons_grid = []
rows = 10
columns = 10


def button_click(x_axis, y_axis):
    print(x_axis, y_axis)
    buttons_grid[x_axis][y_axis].config(background="blue")


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
            tkinter.Label(window, text=label_text).grid(row=x, column=y)
        # Draw buttons
        else:
            button = tkinter.Button(window, fg="white", height=3, width=5, command=lambda z=x, w=y: button_click(z, w))
            button.grid(row=x, column=y)
            button_list.append(button)
    buttons_grid.append(button_list)
window.mainloop()
