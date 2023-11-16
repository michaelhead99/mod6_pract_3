# main.py

import tkinter as tk
from functions import convert_temperature, clear_fahrenheit_entry, clear_celsius_entry

def main():
    root = tk.Tk()
    root.title("Temperature Converter")

    celsius_label = tk.Label(root, text="Celsius:")
    celsius_label.grid(row=0, column=0, padx=10, pady=10)

    celsius_entry = tk.Entry(root, width=10)
    celsius_entry.grid(row=0, column=1, padx=10, pady=10)
    celsius_entry.bind('<FocusIn>', lambda event: clear_fahrenheit_entry(fahrenheit_entry))

    fahrenheit_label = tk.Label(root, text="Fahrenheit:")
    fahrenheit_label.grid(row=1, column=0, padx=10, pady=10)

    fahrenheit_entry = tk.Entry(root, width=10)
    fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)
    fahrenheit_entry.bind('<FocusIn>', lambda event: clear_celsius_entry(celsius_entry))

    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=2, column=0, columnspan=2)

    convert_button = tk.Button(root, text="Convert", command=lambda: convert_temperature(celsius_entry, fahrenheit_entry, result_label))
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
