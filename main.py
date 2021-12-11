import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

tk.Button(text="Hello").pack()
ttk.Button(text="Hello").pack()

tk.Checkbutton(text="Hello").pack()
ttk.Checkbutton(text="Hello").pack()

tk.Radiobutton(text="Hello").pack()
ttk.Radiobutton(text="Hellooog").pack()

root.mainloop()
