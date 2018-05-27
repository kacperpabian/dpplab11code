import tkinter as tk

from lab6.classes.DBInterface import DBInterface


class GUI:
    def __init__(self, root):
        self.root = root
        self.DBinterface = DBInterface()
        self.initView()
        self.list = self.DBinterface.dbToList()

    def buttonAddCommand(self, eventName, eventDate, eventDesc,
                         eventCycle, listbox):
        self.DBinterface.addEvent(eventName.get(),
                                  eventDate.get(),
                                  eventDesc.get(),
                                  eventCycle.get())
        self.refreshList(listbox)

    def deleteRow(self, listbox):
        id = listbox.get(listbox.curselection())
        self.DBinterface.deleteRow(int(id))
        self.refreshList(listbox)

    def showEvent(self, listbox):
        id = listbox.get(listbox.curselection())
        for row in self.list:
            if (row[0] == id):
                print("Nazwa wydarzenia: " + row[1] + "\nData: " +
                      str(row[2]) + "\nOpis: " + row[3]
                      + "\nCykl: " + str(row[4]))

    def initView(self):
        labelName = tk.Label(self.root, text="Nazwa wydarzenia")
        eventName = tk.Entry(self.root)
        labelDate = tk.Label(self.root, text="Data wydarzenia (format Y-M-D)")
        eventDate = tk.Entry(self.root)
        labelDesc = tk.Label(self.root, text="Opis")
        eventDesc = tk.Entry(self.root)
        labelCycle = tk.Label(self.root,
                              text="Cykl (ustawić na ile kolejnych tygodni)")
        eventCycle = tk.Entry(self.root)

        listbox = tk.Listbox(self.root)

        buttonAdd = tk.Button(self.root, text="Dodaj wydarzenie",
                              command=lambda:
                              self.buttonAddCommand
                              (eventName, eventDate,
                               eventDesc, eventCycle,
                               listbox))

        buttonDelete = tk.Button(self.root, text="Usuń wybrane wydarzenie",
                                 command=lambda: self.deleteRow(listbox))

        buttonShowEvent = tk.Button(self.root,
                                    text="Pokaż szczagóły wydarzenia",
                                    command=lambda: self.showEvent(listbox))

        self.refreshList(listbox)

        labelName.grid(row=0, column=0)
        eventName.grid(row=0, column=1)
        labelDate.grid(row=1, column=0)
        eventDate.grid(row=1, column=1)
        labelDesc.grid(row=2, column=0)
        eventDesc.grid(row=2, column=1)
        labelCycle.grid(row=3, column=0)
        eventCycle.grid(row=3, column=1)
        buttonAdd.grid(row=4, column=1)
        listbox.grid(row=5)
        buttonDelete.grid(row=6, column=0)
        buttonShowEvent.grid(row=6, column=1)

    def refreshList(self, listbox):
        listbox.delete(0, tk.END)
        self.list = self.DBinterface.dbToList()
        for item in self.list:
            listbox.insert(tk.END, item[0])
