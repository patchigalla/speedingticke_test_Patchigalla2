#MathsQuiz.py
#MathsQuiz app for primary students
#P.Patchigalla, Feb 21

'''importing required modules - tkinter, ttk and random'''
from tkinter import*
import tkinter.ttk as ttk
from random import* 
import datetime


'''Support class that inherits properties and attributes from main class (MathsQuiz),
  and supports the main class'''

class CorrectAnswer:

  def __init__(self, parent):
    answer = self.answer



  def display_answer(self):


    '''
    self.answer = answer
    self.correct_answer = correct_answer

    self.feedforward2 = Label(self.Questions, text = "")
    self.feedforward2.grid(row = 3, column = 1)    

    self.display_answer()
    self.feedforward2.configure(text = "The correct answer is: " + str(self.answer))
    '''

    return "The correct answer is ", str(self.answer)


    
'''Declare Parent class called MathsQuiz. All objects created from parent class'''
class MathsQuiz:
  '''use init method for all widgets'''
  def __init__(self, parent):

    #formatting constants
    PX = 30
    PY = 10

    '''Widgets for Welcome Frame'''

    self.welcome = Frame(parent)
    self.welcome.grid(row=0, column=0)

    self.title_label = Label(self.welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = PX, pady = PY,
                            font = ("Time", '14', "bold italic"))
    self.title_label.grid(columnspan = 2)

    self.IntroLabel = Label(self.welcome, text = 'The app helps primary students from 7-12 yrs.')
    self.IntroLabel.grid(row = 1, columnspan = 2)

    self.NextButton = Button(self.welcome, text = 'Next', command = self.show_Questions)
    self.NextButton.grid(row = 9, column = 1)
    self.NextButton.bind("<Return>", lambda event: self.show_Questions()) # binds NextButton to Enter key
    root.bind("<Return>", lambda event: self.show_Questions())

    

    self.DifficultyLabel = Label(self.welcome, text = "Choose Difficulty level", anchor=W,
                          fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
    self.DifficultyLabel.grid(row=5, column = 0)
    
    self.difficulty = ["Easy", "Medium", "Hard"]
    self.diff_lvl = StringVar() #use StringVar() for text in list or IntVar() for numbers in list
    self.diff_lvl.set(0) #.set is used so that when the radio buttons appear it is automatically set on the easy difficuty,
    self.diff_btns = []

    #The difficulty levels are stored in a list and the radion button selected cooresponds to the a number in the list, such as "easy"
    for i in range(len(self.difficulty)):      
        self.rb = Radiobutton(self.welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], 
                         anchor = W, padx = 30, width = "5", height = "2")                            
        self.diff_btns.append(self.rb)
        self.rb.grid(row = i+6, column = 0, sticky = W)

    
    '''Widgets for Questions Frame'''

    self.index = 0
    self.score = 0

    self.questions = Frame(parent)
    #self.Questions.grid(row=0, column=1)
    '''update QuestionsLabel configure method to print question number'''
    self.QuestionsLabel = Label(self.questions, text = "",
                            bg = "black", fg = "white", width = 30, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.QuestionsLabel.grid(columnspan = 3)

    self.Problems = Label(self.questions, text = "", pady = 10)
    self.Problems.grid(row = 1, column = 0)

    self.AnswerEntry = ttk.Entry(self.questions, width = 20)
    self.AnswerEntry.grid(row=1, column = 1)
    #Create ScoreLabel to display Score
    self.ScoreLabel = Label(self.questions, text = "")
    self.ScoreLabel.grid(row = 1, column = 2)

    self.feedback = Label(self.questions, text = "")
    self.feedback.grid(row = 2, column = 1)

    self.feedforward = Label(self.questions, text = "")
    self.feedforward.grid(row = 3, column = 1) 

    self.HomeButton = ttk.Button(self.questions, text = 'Home', command = self.show_welcome)
    self.HomeButton.grid(row = 8, column = 0)

    self.check_button = ttk.Button(self.questions, text = 'Check answer', command = self.check_answer)
    self.check_button.grid(row=8, column=1)
   

    

    '''A method that removes Questions Frame'''
  def show_welcome(self):
    self.questions.grid_remove() #removes Question frame
    self.welcome.grid()


  def show_Questions(self):

    self.welcome.grid_remove()
    self.questions.grid()
    self.next_question()# call next question function
    score_text = "Score = " + str(self.score)
    self.ScoreLabel.configure(text = score_text)


  def next_question(self):
    '''Creates questions stores answer'''
    x = randrange(10)
    y = randrange(10)

    #get method selects user choice of difficulty level
    self.select = self.diff_lvl.get()

    '''The following 'if conditions' decides set of questions
    depending on user choice'''

    easy_text = question_text = str(x) + " + " + str(y) + " = "
    self.answer = x + y
    self.index += 1 #keep adding to index number
    self.Problems.configure(text = easy_text)
    #update QuestionsLabel with question number
    self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index)+ "/5")


    #limit number questions to 5, then remove Questions frame and show Welcome frame    
    if self.index >= 6:
      self.questions.grid_remove()
      restart = MathsQuiz(root)
      

  def check_answer(self):
    try:
      ans = int(self.AnswerEntry.get())

      if ans == self.answer:
        self.feedback.configure(text = "Correct")
        self.score += 1 #add 1 to score for correct answer
        score_text = "Score = " + str(self.score)
        self.ScoreLabel.configure(text = score_text)
        self.feedforward.configure(text = "")
        self.AnswerEntry.delete(0, END)
        self.AnswerEntry.focus()
        self.next_question()

      else:
        self.feedback.configure(text = "Incorrect", fg = "red")
        self.feedforward.configure(text = CorrectAnswer.display_answer(self))      
        self.AnswerEntry.delete(0, END)
        self.AnswerEntry.focus()
        self.next_question()

    except ValueError:
      self.feedback.configure(text = "Enter a number")
      self.AnswerEntry.delete(0, END)
      self.AnswerEntry.focus()


#Main routine   
if __name__ == "__main__":
  root =Tk()
  frames = MathsQuiz(root)
  root.title("Quiz")
  root.mainloop()
