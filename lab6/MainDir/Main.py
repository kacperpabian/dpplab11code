import tkinter as tk
from lab6.classes.DBInterface import DBInterface
from lab6.classes.GUI import GUI

if __name__ == '__main__':
    DBInterface = DBInterface()
    root = tk.Tk()
    GUI = GUI(root)

    root.mainloop()
