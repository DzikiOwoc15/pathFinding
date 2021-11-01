import tkinter

window = tkinter.Tk()
window.title("Path Finding GUI")

buttons_grid = [[]]
rows = 10
columns = 10

# Draw the board (Including the row and column labels)
for x in range(rows + 1):
    for y in range(columns + 1):
        # Draw row and column labels
        if x == 0 or y == 0:
            label_template = "{}"
            label_text = ""
            if x == 0:
                label_text = label_template.format(y)
            else:
                label_text = label_template.format(x)
            tkinter.Label(window, text=label_text).grid(row=x, column=y)
        # Draw buttons
        else:
            button_text = "{}{}"
            button = tkinter.Button(window, text=button_text.format(x, y), fg="white").grid(row=x, column=y)
            buttons_grid.append(button)
window.mainloop()
