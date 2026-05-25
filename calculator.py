import tkinter
import math

button_values = [
    ["+/-", "%", "÷", "C"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],   
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
    ["AC", "", "", ""]       
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["+/-", "%", "C"]
bottom_symbol = ["AC"]

row_count = len(button_values)
column_count = len(button_values[0])

color_white = "#FFFFFF"
color_dark_graygreen = "#48504c"
color_light_gray = "#d9d9d9"
color_black = "#000000"

#Window Setup
window = tkinter.Tk() #Creating the main window
window.title("Python Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 24), bg=color_dark_graygreen, fg=color_white, anchor="e",width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        if value == "": 
            continue # Skip empty buttons
        button = tkinter.Button(frame, text=value, font=("Arial", 18), width=column_count-1, height=1, command=lambda value=value: button_clicked(value))

        if value == "AC":
            button.grid(row=row+1, column=column, columnspan=4, sticky="we")
        else:
            button.grid(row=row+1, column=column)

frame.pack()

#a+b, a-b, a*b, a/b
a = "0"
operator = None
b = None

#Fuction for AC button
def clear_all():
    global  a, operator, b
    a = "0"
    operator = None
    b = None

#Function for removing 0 after decimal while using +/-
def remove_zero_decimal(num):
    if num % 1 ==0:
        num = int(num)
    return str(num)

#Making the buttons work
def button_clicked(value):
    global right_symbols, top_symbols, label, a, b, operator

    if value in right_symbols: #÷, ×, -, +, =
        if value == "=":
            if a is not None and operator is not None:
                b = label["text"]
                numA = float(a)
                numB = float(b)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
                
                clear_all()

        elif value in "+-×÷": 
            if operator is None:
                a = label["text"]
                label["text"] = "0"
                b = "0"
            
            operator = value

    elif value in top_symbols: #AC, +/-, %, C
        if value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)         

        elif value == "C":
            current_text = label["text"]
            if current_text == "0" or current_text == "Error" or len(current_text) <= 1:
                label["text"] = "0"
            else:
                label["text"] = current_text[:-1]  

    elif value in bottom_symbol: #AC
        if value == "AC":
            clear_all()
            label["text"] = "0"

    else: #digits, √ or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        
        elif value == "√":
            current_value = float(label["text"])
            if current_value < 0:
                label["text"] = "Error" # Prevents crashing on negative numbers
            else:
                result = math.sqrt(current_value)
                label["text"] = remove_zero_decimal(result)

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace 0
            else:
                label["text"] += value #append digit

#Centering the window on the screen
window.update() #Update the window to get the correct dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()