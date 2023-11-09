import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import matplotlib.pyplot as plt
from linear_regression import *

def update_result_label():
    try:
        m = float(m_entry.get())
        b = float(b_entry.get())

        global result
        result = find_smallest_error([m], [b], datapoints)
        result_label.config(text=f"Best slope (m): {result[0]:.1f}\nBest interception (b): {result[1]:.1f}\nSmallest Error: {result[2]:.1f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

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

calculate_button = ttk.Button(app, text="Calculate", command=update_result_label)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

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
plot_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
