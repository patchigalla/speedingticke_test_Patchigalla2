# welcome.py
# First screen to inform users about the programme
# P.Patchigalla Feb 21

# Import all tool kit interface (tkinter) modules
from tkinter import *
from tkinter import ttk

# change
# Parent class
class MathQuiz:
    def __init__(self, parent):
      
      self.welcome = Frame(parent)
      self.welcome.grid(row=0, column=0)

      self.title_label = Label(self.welcome, text="welcome to Maths Quiz",
                                bg="black", fg="white", width=20, padx=30, pady=10,
                                font=("Time", '14', "bold italic"))
      self.title_label.grid(columnspan=2)  # Lable spans over two columns

      self.next_button = ttk.Button(self.welcome, text='Next')  # ttk prefit gives modern Button
      self.next_button.grid(row=8, column=1)


# Main routine
if __name__ == "__main__":  # checks if condition - name of Parent class is main module
    root = Tk() 
    frames = MathQuiz(root) 
    root.title("Quiz")
    root.mainloop()  # binds the above commands togeter
