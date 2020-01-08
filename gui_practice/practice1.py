import tkinter as tk

window = tk.Tk()

def km_to_miles():
   input_ = entry1_value.get()
   if (any(i.isdigit() for i in input_)):
      output = str(float(input_) * 1.6)
   else:
      output = input_
   text1.insert(tk.END, output + "\n")

button1 = tk.Button(window, text = "Execute", command = km_to_miles)
button1.grid(row = 0, column = 0)

entry1_value = tk.StringVar()
entry1 = tk.Entry(window, textvariable = entry1_value)
entry1.grid(row = 0, column = 1)

text1 = tk.Text(window, height = 5, width = 20)
text1.grid(row = 0, column = 2)

window.mainloop()