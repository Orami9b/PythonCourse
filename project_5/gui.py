import tkinter as tk

window = tk.Tk()

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

view_button = tk.Button(window, text = "View all", width = 12)
view_button.grid(row = 2, column = 3)
search_button = tk.Button(window, text = "Search entry", width = 12)
search_button.grid(row = 3, column = 3)
add_button = tk.Button(window, text = "Add entry", width = 12)
add_button.grid(row = 4, column = 3)
update_button = tk.Button(window, text = "Update selected", width = 12)
update_button.grid(row = 5, column = 3)
delete_button = tk.Button(window, text = "Delete selected", width = 12)
delete_button.grid(row = 6, column = 3)
close_button = tk.Button(window, text = "Close", width = 12)
close_button.grid(row = 7, column = 3)

window.mainloop()