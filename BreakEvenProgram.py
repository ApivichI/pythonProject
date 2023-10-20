import tkinter as tk

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

calculate_button = tk.Button(text="Calculate Break-Even")
calculate_button.pack(anchor='center')

app.mainloop()