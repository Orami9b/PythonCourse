import tkinter as tk
import database

def view_command():
   list_.delete(0, tk.END)
   for row in database.view():
      list_.insert(tk.END, row)

def search_command():
   list_.delete(0, tk.END)
   for row in database.search(
      title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
      list_.insert(tk.END, row)

def add_command():
   database.insert(
      title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
   list_.insert(tk.END, 
      (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selection(event):
   global selection 
   index = list_.curselection()[0]
   selection = list_.get(index)
   title_entry.delete(0, tk.END)
   title_entry.insert(tk.END, selection[1])
   author_entry.delete(0, tk.END)
   author_entry.insert(tk.END, selection[2])
   year_entry.delete(0, tk.END)
   year_entry.insert(tk.END, selection[3])
   isbn_entry.delete(0, tk.END)
   isbn_entry.insert(tk.END, selection[4])

def delete_command():
   database.delete(selection[0])

def update_command():
   database.update(selection[0], title_entry.get(), author_entry.get(),
      year_entry.get(), isbn_entry.get())

window = tk.Tk()
window.wm_title("Bookstore")

title_label = tk.Label(window, text = "Title")
title_label.grid(row = 0, column = 0)
title_text = tk.StringVar()
title_entry = tk.Entry(window, textvariable = title_text)
title_entry.grid(row = 0, column = 1)

author_label = tk.Label(window, text = "Author")
author_label.grid(row = 0, column = 2)
author_text = tk.StringVar()
author_entry = tk.Entry(window, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

year_label = tk.Label(window, text = "Year")
year_label.grid(row = 1, column = 0)
year_text = tk.StringVar()
year_entry = tk.Entry(window, textvariable = year_text)
year_entry.grid(row = 1, column = 1)

isbn_label = tk.Label(window, text = "ISBN")
isbn_label.grid(row = 1, column = 2)
isbn_text = tk.StringVar()
isbn_entry = tk.Entry(window, textvariable = isbn_text)
isbn_entry.grid(row = 1, column = 3)

list_ = tk.Listbox(window, height = 6, width = 36)
list_.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
scroll_bar = tk.Scrollbar(window)
scroll_bar.grid(row = 2, column = 2, rowspan = 6)

list_.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_.yview)

list_.bind('<<ListboxSelect>>', get_selection)

view_button = tk.Button(window, text = "View all", width = 12,
   command = view_command)
view_button.grid(row = 2, column = 3)

search_button = tk.Button(window, text = "Search entry", width = 12,
   command = search_command)
search_button.grid(row = 3, column = 3)

add_button = tk.Button(window, text = "Add entry", width = 12,
   command = add_command)
add_button.grid(row = 4, column = 3)

update_button = tk.Button(window, text = "Update selected", width = 12,
   command = update_command)
update_button.grid(row = 5, column = 3)

delete_button = tk.Button(window, text = "Delete selected", width = 12,
   command = delete_command)
delete_button.grid(row = 6, column = 3)

close_button = tk.Button(window, text = "Close", width = 12,
   command = window.destroy)
close_button.grid(row = 7, column = 3)

window.mainloop()