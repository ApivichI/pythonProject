import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None

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

            break_even_value = break_even_point * selling_price
            result_amount_label.config(text=f"Break-Even Value: {break_even_value:.2f}")

            plot_break_even(fixed_costs, variable_costs, selling_price, break_even_point)
    except ValueError:
        clear_input()
        result_label.config(text="Please enter valid numbers")

def plot_break_even(fixed_costs, variable_costs, selling_price, break_even_point):
    global canvas          
    units = []
    for x in range(0, int(break_even_point) * 2):
        units.append(x)
    revenue = []
    for x in units:
        revenue.append(selling_price * x)
    costs = []
    for x in units:
        costs.append(fixed_costs + variable_costs * x)
        
    plt.figure(figsize=(6, 4))
    plt.plot(units, revenue, label="Total Revenue")
    plt.plot(units, costs, label="Total Costs")
    plt.axvline(x=break_even_point, color='r', linestyle='--', label="Break-Even Point")

    plt.xlabel("Units")
    plt.ylabel("Amount")
    plt.title("Break-Even Analysis")
    plt.legend()
    
    if canvas is not None:
        canvas.get_tk_widget().pack_forget() 

    app.geometry('800x700')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=app)
    canvas.get_tk_widget().pack()

def clear_input():
    global canvas  
    fixed_costs_entry.delete(0, "end")
    variable_costs_entry.delete(0, "end")
    selling_price_entry.delete(0, "end")
    result_label.config(text="")
    result_amount_label.config(text="")

    if canvas is not None:
        canvas.get_tk_widget().pack_forget()  
        canvas = None
        app.geometry('600x300')

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

cleargraph_button = tk.Button(text="Clear Form And Graph", command=clear_input)
cleargraph_button.pack(anchor='center')

result_label = tk.Label(text="")
result_label.pack()

result_amount_label = tk.Label(text="")
result_amount_label.pack()

app.mainloop()