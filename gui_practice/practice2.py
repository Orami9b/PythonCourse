import tkinter as tk

window = tk.Tk()

def convert():
   input_ = entry_variable.get()
   kg_to_gram = 1000
   kg_to_lb = 2.20462
   kg_to_oz = 35.274
   if (any(i.isdigit() for i in input_)):
      output_gram = str(float(input_) * kg_to_gram)
      output_lb = str(float(input_) * kg_to_lb)
      output_oz = str(float(input_) * kg_to_oz)
   else:
      output_gram = "N/A"
      output_lb = "N/A"
      output_oz = "N/A"
   text_gram.delete("1.0", tk.END)
   text_gram.insert(tk.END, output_gram)
   text_lb.delete("1.0", tk.END)
   text_lb.insert(tk.END, output_lb)
   text_oz.delete("1.0", tk.END)
   text_oz.insert(tk.END, output_oz)

label = tk.Label(window, text = "kg")
label.grid(row = 0, column = 0)

entry_variable = tk.StringVar()
entry = tk.Entry(window, textvariable = entry_variable)
entry.grid(row = 0, column = 1)

button = tk.Button(window, text = "Convert", command = convert)
button.grid(row = 0, column = 2)

text_gram = tk.Text(window, height = 1, width = 15)
text_gram.grid(row = 1, column = 0)
text_lb = tk.Text(window, height = 1, width = 15)
text_lb.grid(row = 1, column = 1)
text_oz = tk.Text(window, height = 1, width = 15)
text_oz.grid(row = 1, column = 2)

window.mainloop()