import plugins
import tkinter as tk
from tkinter import ttk

class PluginGui(plugins.Base):
    def __init__(self,main):
        super().__init__(main)
        try:
            self.insert_into_gui()
        except:
            print("Count not insert into parent GUI")

    def start(self):
        print("Plugin A started")

    def insert_into_gui(self):
        self.my_menu = tk.Menu(self.main_cls.menubar)
        self.main_cls.menubar.add_cascade(label="GUI Plugin", menu=self.my_menu)
        self.my_menu.add_command(label="Run Plugin", command=lambda: print("This has been inserted by the Plugin"))
