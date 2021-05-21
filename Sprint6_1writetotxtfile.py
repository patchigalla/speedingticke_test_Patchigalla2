#MathsQuiz.py
#MathsQuiz app for primary students
#P.Patchigalla, March 21

'''importing required modules - tkinter, ttk and random'''
from tkinter import*
from tkinter import ttk
from random import*


'''Declare Parent class called MathsQuiz. All objects created from parent class'''
class MathsQuiz:
  '''use init method for all widgets'''
  def __init__(self, parent):

    '''Widgets for Welcome Frame'''

    self.Welcome = Frame(parent)
    self.Welcome.grid(row=0, column=0)

    self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.TitleLabel.grid(columnspan = 2)

    self.IntroLabel = Label(self.Welcome, text = 'The app helps primary students from 7-12 yrs.')
    self.IntroLabel.grid(row = 1, columnspan = 2)

    self.NextButton = Button(self.Welcome, text = 'Next', command = self.show_Questions)
    self.NextButton.grid(row = 9, column = 1)

    #Name and Age labels
    self.NameLabel = Label(self.Welcome, text = "Name", anchor = W,
                            fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
    self.NameLabel.grid(row = 2, column = 0)

    self.AgeLabel = Label(self.Welcome, text = "Age", anchor=W,
                          fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
    self.AgeLabel.grid(row=3, column = 0)

    #Name and Age Entry widgets and creating name and age instance variables
    self.name = StringVar()
    self.name.set("")
    self.NameEntry = ttk.Entry(self.Welcome, width = 20)
    self.NameEntry.grid(row=2, column = 1, columnspan =2)

    self.age = IntVar()
    self.age.set("")
    self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
    self.AgeEntry.grid(row=3, column = 1)

    #Warning, Difficulty level labels and Radio buttons
    self.WarningLabel = Label(self.Welcome, text = "", anchor=W,
                          fg = "red", width = 20, padx = 30, pady = 10)
    self.WarningLabel.grid(row=4, columnspan = 2)


    self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty level", anchor=W,
                          fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
    self.DifficultyLabel.grid(row=5, column = 0)
    
    self.difficulty = ["Easy", "Medium", "Hard"]
    self.diff_lvl = StringVar() #use StringVar() for text in list or IntVar() for numbers in list
    self.diff_lvl.set(0) #.set is used so that when the radio buttons appear it is automatically set on the easy difficuty,
    self.diff_btns = []

    #The difficulty levels are stored in a list and the radion button selected cooresponds to the a number in the list, such as "easy"
    for i in range(len(self.difficulty)):      
        self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], 
                         anchor = W, padx = 50, width = "5", height = "2")                            
        self.diff_btns.append(self.rb)
        self.rb.grid(row = i+6, column = 0, sticky = W)

    
    '''Widgets for Questions Frame'''

    self.index = 0
    self.score = 0

    self.Questions = Frame(parent)
    #self.Questions.grid(row=0, column=1)
    '''update QuestionsLabel configure method to print question number'''
    self.QuestionsLabel = Label(self.Questions, text = "",
                            bg = "black", fg = "white", width = 30, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.QuestionsLabel.grid(columnspan = 3)

    self.Problems = Label(self.Questions, text = "", pady = 10)
    self.Problems.grid(row = 1, column = 0)

    self.AnswerEntry = ttk.Entry(self.Questions, width = 20)
    self.AnswerEntry.grid(row=1, column = 1)
    #Create ScoreLabel to display Score
    self.ScoreLabel = Label(self.Questions, text = "")
    self.ScoreLabel.grid(row = 1, column = 2)

    self.feedback = Label(self.Questions, text = "")
    self.feedback.grid(row = 2, column = 1)

    self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
    self.HomeButton.grid(row = 8, column = 0)

    self.check_button = ttk.Button(self.Questions, text = 'Check answer', command = self.check_answer)
    self.check_button.grid(row=8, column=1)


   
    #self.next_button = ttk.Button(self.Questions, text = 'Next question', command = self.next_question)
    #self.next_button.grid(row=8, column=2)

    '''Widgets for Reprot Frame'''
   

    self.Report_frame = Frame(parent)
    self.Report_frame.grid_propagate(4)#progates four values

   
    Report_page = ["Name", "Age", "Score"] 
    self.report_labels = []

    for i in range(len(Report_page)):
      ColumnHeading = Label(self.Report_frame, text = Report_page[i], width = "7", height = "2", font = ("Times", "22", "bold"))
      self.report_labels.append(ColumnHeading)
      ColumnHeading.grid(row = 0, column = i+1)


    self.user_name = Label(self.Report_frame, textvariable = self.name)
    self.user_name.grid(row = 3, column = 1)
      

    self.user_age = Label(self.Report_frame, textvariable = self.age)
    self.user_age.grid(row = 3, column = 2)

    self.user_score = Label(self.Report_frame, text = "")
    self.user_score.grid(row = 3, column = 3)



    self.Home = ttk.Button(self.Report_frame, text = 'Restart', command = self.Restart)
    self.Home.grid(row = 8, column = 1)

    self.Exit = ttk.Button(self.Report_frame, text = 'Close', command = self.show_Welcome)
    self.Exit.grid(row = 8, column = 4)

    '''A method that removes Questions Frame'''
  def show_Welcome(self):
    self.Questions.grid_remove() #removes Question frame
    self.Report_frame.grid_remove() #removes 
    self.Welcome.grid()


  def show_Questions(self):

      try:
#Error checking for empty and non-text user entries for Name
        if self.NameEntry.get() == "":
          self.WarningLabel.configure(text = "Please enter name")
          self.NameEntry.focus()

        elif self.NameEntry.get().isalpha() == False:
          self.WarningLabel.configure(text = "Pleasae enter text")
          self.NameEntry.delete(0, END)
          self.NameEntry.focus()
#Error checking for empty and age limit cases
        elif self.AgeEntry.get() == "":
          self.WarningLabel.configure(text = "Please enter age")
          self.AgeEntry.focus()
        
        elif int(self.AgeEntry.get()) > 12:
          self.WarningLabel.configure(text = "You are too old!")
          self.AgeEntry.delete(0, END)
          self.AgeEntry.focus()
       
        elif int(self.AgeEntry.get()) < 0:
          self.WarningLabel.configure(text = "You are too old")
          self.AgeEntry.delete(0, END)
          self.AgeEntry.focus()
        elif int(self.AgeEntry.get()) < 7:
          self.WarningLabel.configure(text = "You are too young")
          self.AgeEntry.delete(0, END)
          self.AgeEntry.focus()
      
        else: #if all conditions are met, then show Questions frame
          self.name.set(self.NameEntry.get())
          self.age.set(self.AgeEntry.get())
          self.Welcome.grid_remove()
          self.Questions.grid()
          self.next_question()# call next question function
          score_text = "Score = " + str(self.score)
          self.ScoreLabel.configure(text = score_text)

      
      except ValueError:
        self.WarningLabel.configure(text = "Please enter a number")
        self.AgeEntry.delete(0, END)
        self.AgeEntry.focus()



  def next_question(self):
    '''Creates questions stores answer'''
    x = randrange(10)
    y = randrange(10)

    #get method selects user choice of difficulty level
    self.select = self.diff_lvl.get()

    '''The following 'if conditions' decides set of questions
    depending on user choice'''
    if self.select == "0":
      easy_text = question_text = str(x) + " + " + str(y) + " = "
      self.answer = x + y
      self.index += 1 #keep adding to index number
      self.Problems.configure(text = easy_text)
      #update QuestionsLabel with question number
      self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index)+ "/5")
      

    elif self.select == "1":
      medium_text = question_text = str(x) + " - " + str(y) + " = "
      self.answer = x - y
      self.index += 1 #keep adding to index number
      self.Problems.configure(text = medium_text)
      #update QuestionsLabel with question number
      self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index)+ "/5")

    else:
      
      hard_text = question_text = str(x) + " x " + str(y) + " = "
      self.answer = x * y
      self.index += 1 #keep adding to index number
      self.Problems.configure(text = hard_text)
      #update QuestionsLabel with question number
      self.QuestionsLabel.configure(text = "Quiz Question " + str(self.index)+ "/5")
      

    #limit number questions to 5, then remove Questions frame and show Welcome frame

      
    if self.index >= 6:
      self.Questions.grid_remove()
      self.Report_frame.grid(row =1, columnspan = 4)
      """Open and write user details to records.txt as data_file"""
      with open('records.txt', 'a+') as data_file:
        data_file.write(self.name.get() + ' ' + str(self.age.get()) + ' ' + str(self.score) + ' ' + '\n')


  def check_answer(self):
    try:
      ans = int(self.AnswerEntry.get())

      if ans == self.answer:
        self.feedback.configure(text = "Correct")
        self.score += 1 #add 1 to score for correct answer
        score_text = "Score = " + str(self.score)
        self.ScoreLabel.configure(text = score_text)
        self.user_score.configure(text = score_text)
        self.AnswerEntry.delete(0, END)
        self.AnswerEntry.focus()
        self.next_question()

      else:
        self.feedback.configure(text = "Incorrect", fg = "red")
        self.AnswerEntry.delete(0, END)
        self.AnswerEntry.focus()
        self.next_question()

    except ValueError:
      self.feedback.configure(text = "Enter a number")
      self.AnswerEntry.delete(0, END)
      self.AnswerEntry.focus()

    if self.score <= 5:
      self.user_score.configure(text = str(self.score))

  def Restart(self):
    self.Report_frame.grid_remove()
    restart = MathsQuiz(root)


#Main routine   
if __name__ == "__main__":
  root =Tk()
  frames = MathsQuiz(root)
  root.title("Quiz")
  root.mainloop()
