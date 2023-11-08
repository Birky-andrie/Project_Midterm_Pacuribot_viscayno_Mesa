import tkinter as tk

# This is the variable to store the current calculation
calculation = ""


# This is the function use to add a symbol to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")  # Clear the text field
    text_result.insert(1.0, calculation)  # Update the text field with new calculation


# This is the function to evaluate current calculation
def evaluate_calculation():
    global calculation
    if calculation:
        try:
            calculation = str(eval(calculation))  # Use eval() to calculate the result
            text_result.delete(1.0, "end")  # CLear the text field
            text_result.insert(1.0, calculation)  # Display the result
        except:
            clear_field()
            text_result.insert(1.0, "Error!")  # Display an error message if an exception occurs
    else:
        clear_field()


# This is the function to clear current calculation
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")  # Clear the text field


# This is used to create GUI window
root = tk.Tk()
root.geometry("300x275")

# This is used to create a text field to display the current calculation
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# This is the GUI function buttons for digits (0-9), basic operators, parentheses, clear, and equals

# This is the function button for digit 1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)  # Display "1" and add 1 to the calculation

# This is the function button for digit 2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)  # Display "2" and add 2 to the calculation

# This is the function button for digit 3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)  # Display "3" and add 3 to the calculation

# This is the function button for digit 4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)  # Display "4" and add 4 to the calculation

# This is the function button for digit 5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)  # Display "5" and add 5 to the calculation

# This is the function button for digit 6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)  # Display "6" and add 6 to the calculation

# This is the function button for digit 7
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)  # Display "7" and add 7 to the calculation

# This is the function button for digit 8
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)  # Display "8" and add 8 to the calculation

# This is the function button for digit 9
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)  # Display "9" and add 9 to the calculation

# This is the function button for digit 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)  # Display "0" and add 0 to the calculation

# This is the function button for addition
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)  # Display "+" and add "+" to the calculation

# This is the function button for subtraction
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)  # Display "-" and add "-" to the calculation

# This is the function button for multiplication
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)  # Display "*" and add "*" to the calculation

# This is the function button for division
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)  # Display "/" and add "/" to the calculation

# This is the function button for opening parenthesis
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)  # Display "(" and add "(" to the calculation

# This is the function button for closing parenthesis
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)  # Display ")" and add ")" to the calculation

# This is the function button clear field
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1)  # Display "C" to clear the calculation

# This is the function button to evaluate the calculation
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)  # Display "=" to calculate the result

# Start the GUI main loop
root.mainloop()
