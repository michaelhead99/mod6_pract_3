# functions.py

import tkinter as tk
import math

def convert_temperature(celsius_entry, fahrenheit_entry, result_label):
    try:
        if celsius_entry.get():
            celsius_value = float(celsius_entry.get())
            fahrenheit_result = (celsius_value * 9/5) + 32
            result_label.config(text=f"Result: {celsius_value}°C = {round(fahrenheit_result, 2)}°F")
        elif fahrenheit_entry.get():
            fahrenheit_value = float(fahrenheit_entry.get())
            celsius_result = (fahrenheit_value - 32) * 5/9
            result_label.config(text=f"Result: {fahrenheit_value}°F = {round(celsius_result, 2)}°C")
        else:
            result_label.config(text="Please enter a value in one of the textboxes.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def clear_fahrenheit_entry(fahrenheit_entry):
    fahrenheit_entry.delete(0, tk.END)

def clear_celsius_entry(celsius_entry):
    celsius_entry.delete(0, tk.END)
