from tkinter import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        # First Label of Checking the status of our Task
        Label(self, text="STATUS", bg="Light Blue", font=("Calibri", 14)).grid(row=0, column=0, columnspan=2, sticky=W)
        # since we dont need to access these labels anywhere in the progrmas they are just gonna stay there so we are not assigning them to any variable

        # Second Label for the task Description
        Label(self, text="TASK DESCRIPTION", bg="Light Green", font=("Calibri", 14)).grid(row=0, column=2, columnspan=3,sticky=W)
        # since we dont need to access these labels anywhere in the progrmas they are just gonna stay there so we are not assigning them to any variable

        # creating Checkbox for the Task completion Status


        checkvar = IntVar()
        Checkbutton(text="First Task",variable=checkvar).grid(row=1,column=0, columnspan=2, sticky=W)

# Main Programs Begins here
root = Tk()
root.title("To Do List Application")
root.geometry("250x200")
APP = Application(root)
root.mainloop()
