#import client, server
import tkinter as tk

class Application(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        self.root.bind('<Return>', self.parseText)

        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

    def listBoxAdd(self, item):



    def parseText(self, event):
        var = self.entry.get()
        #
        # Her skal koden til at sende beskeden fra clienten til server kaldes
        #
        print(var)
        self.entry.delete(0, 'end')
       

    def start(self):
        self.root.mainloop()


Application().start()
