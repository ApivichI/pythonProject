import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate_break_even():
    try:
        fixed_costs = float(fixed_costs_entry.get())
        variable_costs = float(variable_costs_entry.get())
        selling_price = float(selling_price_entry.get())

        if variable_costs >= selling_price:
            result_label.config(text="No Break-Even Point")
        else:
            break_even_point = fixed_costs / (selling_price - variable_costs)
            result_label.config(text=f"Break-Even Point: {break_even_point:.2f} units")

            plot_break_even(fixed_costs, variable_costs, selling_price, break_even_point)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def plot_break_even(fixed_costs, variable_costs, selling_price, break_even_point):
    global canvas

    units = list(range(0, int(break_even_point) * 2))
    revenue = [selling_price * x for x in units]
    costs = [fixed_costs + variable_costs * x for x in units]

    plt.figure(figsize=(6, 4))
    plt.plot(units, revenue, label="Total Revenue")
    plt.plot(units, costs, label="Total Costs")
    plt.axvline(x=break_even_point, color='r', linestyle='--', label="Break-Even Point")

    plt.xlabel("Units")
    plt.ylabel("Amount")
    plt.title("Break-Even Analysis")
    plt.legend()

    app.geometry('800x700')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=app)
    canvas.get_tk_widget().pack()

        
app = tk.Tk()
app.title("Break-Even Analysis Program")
app.geometry('600x300')

fixed_costs_label = tk.Label(text="Fixed Costs:")
fixed_costs_label.pack(anchor='center')
fixed_costs_entry = tk.Entry()
fixed_costs_entry.pack()

variable_costs_label = tk.Label(text="Variable Costs per Unit:")
variable_costs_label.pack(anchor='center')
variable_costs_entry = tk.Entry()
variable_costs_entry.pack()

selling_price_label = tk.Label(text="Selling Price per Unit:")
selling_price_label.pack(anchor='center')
selling_price_entry = tk.Entry()
selling_price_entry.pack(anchor='center')

calculate_button = tk.Button(text="Calculate Break-Even", command=calculate_break_even)
calculate_button.pack(anchor='center')

result_label = tk.Label(text="")
result_label.pack()

app.mainloop()