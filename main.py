from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        # First Label of Checking the status of our Task
        Label(self, text="STATUS", bg="Light Blue", font=("Calibri", 14)).grid(row=0, column=0, columnspan=1, sticky=W)
        # since we dont need to access these labels anywhere in the progrmas they are just gonna stay there so we are not assigning them to any variable

        # Second Label for the task Description
        Label(self, text="TASK DESCRIPTION", bg="Light Green", font=("Calibri", 14)).grid(row=0, column=2, columnspan=25,sticky=W)
        # since we dont need to access these labels anywhere in the programs they are just gonna stay there so we are not assigning them to any variable

        # creating Checkbox for the Task completion Status
        checkvar = IntVar()
        Checkbutton(variable=checkvar,font=("Calibri",13)).grid(row=1,column=0, columnspan=1, sticky=W)

        # creating Task Description Entry Box where we'll be entering our text
        self.task_entry = ScrolledText(self,font=("Seoge UI",13),width=15,height=1,wrap = WORD,).grid(row=1,column=2,columnspan=25,sticky=W)
        # now we need to positioned our entry text box just in front of our previously created checkbox




# Main Programs Begins here
if __name__ == "__main__":
    root = Tk()
    root.title("To Do List Application")
    root.geometry("500x200")
    app = Application(root)
    root.mainloop()
