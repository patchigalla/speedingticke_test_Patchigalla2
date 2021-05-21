#MathsQuiz.py
#MathsQuiz app for primary students
#P.Patchigalla, Feb 21

'''importing all modules from tkinter'''
from tkinter import*
from tkinter import ttk

'''Declare Parent class called MathsQuiz. All objects created from parent class'''
class MathsQuiz:
  '''use init method for all widgets'''
  def __init__(self,parent):

    '''Widgets for Welcome Frame'''

    self.Welcome = Frame(parent)
    self.Welcome.grid(row=0, column=0)

    self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.TitleLabel.grid(columnspan = 2)

    self.NextButton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
    self.NextButton.grid(row = 8, column = 1)

    
    '''Widgets for Questions Frame'''

    self.Questions = Frame(parent)
    #self.Questions.grid(row=0, column=1)

    self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.QuestionsLabel.grid(columnspan = 2)

    self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
    self.HomeButton.grid(row = 8, column = 1)

    '''A method that removes Questions Frame'''
  def show_Welcome(self):
    self.Questions.grid_remove()
    self.Welcome.grid()

  def show_Questions(self):
    self.Welcome.grid_remove()
    self.Questions.grid(row = 0, column = 1)



#Main routine   
if __name__ == "__main__":
  root =Tk()
  frames = MathsQuiz(root)
  root.title("Quiz")
  root.mainloop()
