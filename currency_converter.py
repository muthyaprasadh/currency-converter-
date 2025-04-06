import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to fetch exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates'].get(target_currency, None)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rate: {e}")
        return None

# Function to perform conversion
def convert_currency():
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    amount = amount_var.get()
    
    if not amount:
        messagebox.showerror("Input Error", "Please enter a valid amount")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number")
        return
    
    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate:
        converted_amount = amount * rate
        result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        messagebox.showerror("Conversion Error", "Could not fetch exchange rate")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Input fields
amount_var = tk.StringVar()
base_currency_var = tk.StringVar()
target_currency_var = tk.StringVar()

ttk.Label(root, text="Amount:").pack(pady=5)
ttk.Entry(root, textvariable=amount_var).pack(pady=5)

ttk.Label(root, text="From Currency:").pack(pady=5)
ttk.Entry(root, textvariable=base_currency_var).pack(pady=5)

ttk.Label(root, text="To Currency:").pack(pady=5)
ttk.Entry(root, textvariable=target_currency_var).pack(pady=5)

ttk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()