from tkinter import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        # First Label of Checking the status of our Task
        self.status = Label(self, text="STATUS")
        self.status.grid(row=0, column=0, columnspan=2, sticky=W)

        # Second Label for the task Description
        self.description = Label(self, text="TASK DESCRIPTION")
        self.description.grid(row=0, column=3, columnspan=3, sticky=W)


# Main Programs Begins here
root = Tk()
root.title("To Do List Application")
root.geometry("250x200")
APP = Application(root)
root.mainloop()
