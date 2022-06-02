import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#load the plugins
from plugins import Base
class App(tk.Tk):
    loaded_plugins={}
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('2022: Project')
        self.geometry('300x150')

        # label
        self.label = ttk.Label(self, text='Hello, h_da!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        #menubar:
        self.menubar = tk.Menu(self)
        self.menubar.add_command(label="File", command=lambda: print("File Menu"))
        self.plugins_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Plugins", menu=self.plugins_menu)
        self.config(menu=self.menubar)

        #load the plugins:
        self.load_plugins()

    def load_plugins(self):
        '''
        1. This function retrieves all classes that are available for Plugins.
        2. It creates an instance of each class and stores it into the loaded_plugins dict
        :return:
        '''
        for name, plugin in Base.plugins.items():
            inst = plugin(self)  # create instance
            self.loaded_plugins[name] = inst
            self.plugins_menu.add_command(label=name, command=inst.start)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')


if __name__ == "__main__":
    app = App()
    app.mainloop()