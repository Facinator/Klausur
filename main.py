import time
from tkinter import *
from tkinter import ttk

NAME = "Richard"
GEOMETRY = "600x600"


class Window:
    root = Tk()
    frame = ttk.Frame(root)

    alive = True

    def __init__(self):
        self.root.title(NAME)
        self.root.geometry(GEOMETRY)

        self.__ui__()

    def __ui__(self):
        self.label_1_var = StringVar()
        self.label_1_var.set('Label 1')
        self.label_1 = Label(textvariable=self.label_1_var)
        self.label_1.place(x=10, y=10)

        self.entry_1_var = StringVar()
        self.entry_1 = Entry(textvariable=self.entry_1_var)
        self.entry_1.place(x=10, y=50)

        self.check_1_var = IntVar()
        self.check_1 = Checkbutton(text='check', variable=self.check_1_var)
        self.check_1.place(x=20, y=70)

        self.radio_var = IntVar()
        self.radio_1 = Radiobutton(text='one', variable=self.radio_var, value=1)
        self.radio_1.place(x=20, y=90)

        self.radio_2 = Radiobutton(text='two', variable=self.radio_var, value=2)
        self.radio_2.place(x=20, y=110)

        self.combo_list = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
        self.combo_1 = ttk.Combobox(values=self.combo_list)
        self.combo_1.set('Choose')
        self.combo_1.place(x=10, y=150)

        self.listbox = Listbox()
        self.listbox.place(x=210, y=10)
        self.listbox.insert(1, 'One')
        self.listbox.insert(2, 'Two')
        self.listbox.insert(3, 'Three')
        self.listbox.insert(4, 'Four')

        self.quit_button = Button(text="Quit", command=self.__die__)
        self.quit_button.place(x=550, y=550)

    def __event__(self):
        self.root.bind('<KeyPress>', self.__keys__)
        self.root.protocol("WM_DELETE_WINDOW", self.__die__)

    def __keys__(self, event):
        key = event.keysym

        if key == 'w' or key == 's':
            self.label_1_var.set(key)

    def __draw__(self):
        self.root.update()

    def __die__(self):
        self.alive = False

    def mainloop(self):
        while self.alive:
            self.__event__()
            self.__draw__()
            time.sleep(1/20)


w = Window()
w.mainloop()
