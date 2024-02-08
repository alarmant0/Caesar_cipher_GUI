import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class OptionsWindow:
    def __init__(self, parent_gui):
        self.parent_gui = parent_gui
        self.options_window = tk.Toplevel(parent_gui.master)
        self.options_window.title("Options")
        self.options_window.geometry("300x100") 
        self.options_window.resizable(False, False)  
        self.options_window.transient(parent_gui.master)  

        self.font_size_label = tk.Label(self.options_window, text="Font Size:")
        self.font_size_label.grid(row=0, column=0, padx=5, pady=5)
        self.font_size_entry = tk.Entry(self.options_window, width=10)
        self.font_size_entry.grid(row=0, column=1, padx=5, pady=5)
        self.font_size_entry.insert(0, "12")  

        self.apply_button = tk.Button(self.options_window, text="Apply", command=self.apply_options)
        self.apply_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def apply_options(self):
        font_size = self.font_size_entry.get()
        try:
            font_size = int(font_size)
            self.parent_gui.output_area.configure(font=("Helvetica", font_size))
            self.options_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for font size.")

class CaesarCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher Encoder/Decoder")
        master['background']='#856ff8'
        master.geometry("900x550")

        self.input_label = tk.Label(master, text="Enter Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.shift_label = tk.Label(master, text="Enter Shift:")
        self.shift_label.grid(row=1, column=0, padx=5, pady=5)

        self.shift_entry = tk.Entry(master, width=10)
        self.shift_entry.grid(row=1, column=1, padx=5, pady=5)

        self.encode_button = tk.Button(master, text="Encode", command=self.encode)
        self.encode_button.grid(row=2, column=0, padx=5, pady=5)

        self.decode_button = tk.Button(master, text="Decode", command=self.decode)
        self.decode_button.grid(row=2, column=1, padx=5, pady=5)

        self.brute_force_button = tk.Button(master, text="Brute Force", command=self.brute_force)
        self.brute_force_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.output_label = tk.Label(master, text="Result:")
        self.output_label.grid(row=4, column=0, padx=5, pady=5)

        self.output_area = scrolledtext.ScrolledText(master, width=50, height=10, wrap=tk.WORD, state='disabled')
        self.output_area.grid(row=4, column=1, padx=5, pady=5)
        self.output_area.configure(bg="black", fg="green", font=("Comic Sans", 20))  
        self.options_button = tk.Button(master, text="Options", command=self.open_options)
        self.options_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def open_options(self):
        OptionsWindow(self)

    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():  
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                result += chr(shifted)
            else:
                result += char
        return result

    def encode(self):
        input_text = self.input_entry.get()
        shift_text = self.shift_entry.get()
        if shift_text.isdigit():
            shift_value = int(shift_text)
            encoded_text = self.caesar_cipher(input_text, shift_value)
            self.output_area.config(state='normal')
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, encoded_text)
            self.output_area.config(state='disabled')
        else:
            self.output_area.config(state='normal')
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, "Invalid shift value. Please enter an integer.")
            self.output_area.config(state='disabled')

    def decode(self):
        input_text = self.input_entry.get()
        shift_text = self.shift_entry.get()
        if shift_text.isdigit(): 
            shift_value = -int(shift_text)
            decoded_text = self.caesar_cipher(input_text, shift_value)
            self.output_area.config(state='normal')
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, decoded_text)
            self.output_area.config(state='disabled')
        else:
            self.output_area.config(state='normal')
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, "Invalid shift value. Please enter an integer.")
            self.output_area.config(state='disabled')

    def brute_force(self):
        input_text = self.input_entry.get()
        results = []
        for shift in range(26):
            decoded_text = self.caesar_cipher(input_text, shift)
            results.append(f"Shift {shift}: {decoded_text}")
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', tk.END)
        for result in results:
            self.output_area.insert(tk.END, result + '\n\n')
        self.output_area.config(state='disabled')

root = tk.Tk()
caesar_cipher_gui = CaesarCipherGUI(root)
root.mainloop()
