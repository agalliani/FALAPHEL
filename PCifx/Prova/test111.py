import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.spinbox = tk.Spinbox(root)
        self.spinbox.pack()
        self.spinbox.bind("<Return>", self.get_spinbox_value)

    def get_spinbox_value(self, event):
        value = self.spinbox.get()
        print(value)
        
root = tk.Tk()
app = MyApp(root)
root.mainloop()