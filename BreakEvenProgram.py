import tkinter as tk

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

    except ValueError:
        result_label.config(text="Please enter valid numbers")

app = tk.Tk()
app.title("Break-Even Analysis Program")
app.geometry("600x300")

fixed_costs_label = tk.Label(text = "Fixed Costs:")
fixed_costs_label.pack(anchor = "center")
fixed_costs_entry = tk.Entry()
fixed_costs_entry.pack(anchor = "center")

variable_costs_label = tk.Label(text = "Variable Costs per Unit:")
variable_costs_label.pack(anchor = "center")
variable_costs_entry = tk.Entry()
variable_costs_entry.pack(anchor = "center")

selling_price_label = tk.Label(text = "Selling Price per Unit:")
selling_price_label.pack(anchor = 'center')
selling_price_entry = tk.Entry()
selling_price_entry.pack(anchor = 'center')

calculate_button = tk.Button(text="Calculate Break-Even", command=calculate_break_even)
calculate_button.pack(anchor='center')

result_label = tk.Label(text="")
result_label.pack()

app.mainloop()