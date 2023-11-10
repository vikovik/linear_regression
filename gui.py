import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import matplotlib.pyplot as plt
from linear_regression import *

"""
    The function `update_result_label` updates a result label with the best slope, best interception,
    and smallest error based on user input.
"""
def update_result_label():
    try:
        m = float(m_entry.get())
        b = float(b_entry.get())

        possible_ms = [float(ms) for ms in possible_ms_entry.get().split(",")]
        possible_bs = [float(bs) for bs in possible_bs_entry.get().split(",")]
        datapoints = [(float(x), float(y)) for x, y in [p.split(",") for p in datapoints_entry.get().split(";")]]

        global result
        result = find_smallest_error(possible_ms, possible_bs, datapoints, [m], [b])
        result_label.config(text=f"Best slope (m): {result[0]:.1f}\nBest interception (b): {result[1]:.1f}\nSmallest Error: {result[2]:.1f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def exit_program():
    app.destroy()

# Create the main application window
app = tk.Tk()
app.title("Linear Regression Calculator")

# Create and set up the input fields and labels
m_label = ttk.Label(app, text="Enter slope value (m):")
m_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
m_entry = ttk.Entry(app)
m_entry.grid(row=0, column=1, padx=10, pady=5)

b_label = ttk.Label(app, text="Enter interception value (b):")
b_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
b_entry = ttk.Entry(app)
b_entry.grid(row=1, column=1, padx=10, pady=5)

possible_ms_label = ttk.Label(app, text="Enter possible slope values m (comma-separated, without whitespaces):")
possible_ms_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
possible_ms_entry = ttk.Entry(app)
possible_ms_entry.grid(row=2, column=1, padx=10, pady=5)

possible_bs_label = ttk.Label(app, text="Enter possible interception values b (comma-separated, without whitespaces):")
possible_bs_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
possible_bs_entry = ttk.Entry(app)
possible_bs_entry.grid(row=3, column=1, padx=10, pady=5)

datapoints_label = ttk.Label(app, text="Enter data points (x,y) separated by semicolon (e.g., '1,2;2,0;3,4'):")
datapoints_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
datapoints_entry = ttk.Entry(app)
datapoints_entry.grid(row=4, column=1, padx=10, pady=5)

calculate_button = ttk.Button(app, text="Calculate", command=update_result_label)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Create and set up a plot button
def plot_data():
    x = [point[0] for point in datapoints]
    y = [point[1] for point in datapoints]
    plt.scatter(x, y, label="Data Points")
    plt.plot(x, [get_y(result[0], result[1], xi) for xi in x], label="Regression Line", color='red')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

plot_button = ttk.Button(app, text="Show Plot Data", command=plot_data)
plot_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

exit_button = ttk.Button(app, text="Exit Program", command=exit_program)
exit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
