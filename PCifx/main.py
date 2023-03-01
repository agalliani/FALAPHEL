from tkinter import *


from MasterView import MasterView

root = Tk()
root.title("AFE Falaphel Charge Scan Utility")



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

MasterView(root)

root.mainloop()
