#ScienceQuiz - Science quiz built with python, with a gui,
#robert_sefaj_scienceQuiz6.py
#R.Sefaj, April 2020

from tkinter import*
from tkinter import ttk
from random import*



class ScienceQuiz:   #class used to house all frames, with their widgets and other functions and the instance variables,sucha s my widgets for frames
    def __init__(self, parent): #self is used to represent the instance of a class, allowing us to acces its atributs, while self acts as a widget

#---Frame1 widgets-----------------------------------------------------------------------------------------------------------------------------------------
        self.frame1 = Frame(parent)
        self.frame1.grid(row = 0, column = 0)

        self.HeadingLabel = Label(self.frame1, bg = "DodgerBlue4", fg = "white", width = 30,
                                padx = 30, pady = 10, text = "Science Quiz", font = ("Arial", "16", "bold"))
        self.HeadingLabel.grid(columnspan = 2) #grid is a geometry manager which allows us to move widgets in a table like structure

        self.NameLabel = Label(self.frame1, text = "Name", width = 20, font = ("Arial", "12",
                                                                               "bold"))
        self.NameLabel.grid(row = 2, column = 0, sticky = W)# sticky w defines the cell that the widget is in, w means it is in the west of the cell
  #--Entry box for name------------------------------------------------------------------------------------------------------------------------------------
        self.name = StringVar() #stringvar is used to detect a change in hte variable, specifically to see if the user has imputed an answer
        self.name.set("")
        self.NameEntry = ttk.Entry(self.frame1, textvariable = self.name, width = 20)
        self.NameEntry.grid(row = 3, column = 0)

  #--Entrybox for age-----------------------------------------------------------------
        self.AgeLabel = Label(self.frame1, text = "Age", width = 20, font = ("Arial",
                                                                             "12", "bold"))
        self.AgeLabel.grid(row = 2, column = 1, sticky = W)

        self.age = IntVar() #IntVar detects that the change of the variable is an integer
        self.age.set("")
        self.AgeEntry = ttk.Entry(self.frame1, width = 20, textvariable = self.age)
        self.AgeEntry.grid(row = 3, column = 1, columnspan = 3)

        self.warning = Label(self.frame1, text = "")  #Warning message label which is configured on what the user types, such as warning if they input letters  instead of numbers
        self.warning.grid(row = 5, column = 1, columnspan = 3)

        self.DifficultyLabel = Label(self.frame1, text = "Select Difficulty", width = 20,
                                 font = ("Arial", "12", "bold"))
        self.DifficultyLabel.grid(row = 5, column = 0, sticky = W)

#-----------------------------------------------------difficulty buttons-----------------------
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0) #.set is used so that when the radio buttons appear it is automatically set on the easy difficuty,
        self.diff_btns = []

        for i in range(len(self.difficulty)):      
            rb = Radiobutton(self.frame1, variable = self.diff_lvl, value = i, text = self.difficulty[i], #the level are stored in a list and the radion button slected
                             anchor = W, padx = 50, width = "10", height = "2")                           #cooresponds to the anumber in the list, such as "easy" has a place value of 0
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)

        self.submit = ttk.Button(self.frame1, text = "Next", command = self.show_frame2)
        self.submit.grid(row = 9, column = 1)

#---Frame 2 widgets------------------------------------------------------------------------------------

        self.QuestionNumber = 0   #question number and running_score a set to zero at the start of frame 2, helpful when the user restarts the quiz
        self.running_score = 0
        self.frame2 = Frame(parent, height = "450", width = "400")

        self.ScienceQuestions = Label(self.frame2, bg = "DodgerBlue4", fg = "white", width = 30,
        padx = 100, pady = 10, text = "Questions", font = ("Arial", "20", "bold"))
        self.ScienceQuestions.grid(row = 0, columnspan = 3)

        self.Question_Label = Label(self.frame2, text = "", width = 40, height = 3, padx = 50, font = ("Comic Sans MS", "10", "bold"))
        self.Question_Label.grid(row = 1, columnspan = 4)

        self.Answer_Input = ttk.Entry(self.frame2, width = 20)
        self.Answer_Input.grid(row = 2, columnspan = 5)

        self.quiz_label = Label(self.frame2, text = "Problems", font = ("Arial", "14", "bold"))
        self.quiz_label.grid(row = 1, column = 0)

        self.placeholder1 = Label(self.frame2) #placeholder labels are added to be able to space out widegts
        self.placeholder1.grid(row = 3, column = 0)

        self.placeholder2 = Label(self.frame2)
        self.placeholder2.grid(row = 4, column = 0)
        

        self.feedback = Label(self.frame2, text = "Check your Answer", font = ("Arial", "8", "bold"))
        self.feedback.grid(row = 5, column = 0, columnspan = 4)

        self.Home_Button = Button(self.frame2, text = "Home", anchor = W, command = self.show_frame1) #home button so the user can return to home 
        self.Home_Button.grid(row = 6, column = 0)

        self.check = Button(self.frame2, text = "check answer", anchor = W,
                            command = self.check_answer)  #check answer button, so user can check his answer and also moves on to the next quesitonn
        self.check.grid(row = 2, column = 1, columnspan = 3)

        self.placeholder3 = Label(self.frame2)
        self.placeholder3.grid(row = 7, column = 0)

#-----Widgets for frame 3-----------------------------------------------------------------------

        self.report_frame3 = Frame(parent, height = "450", width = "500")
        self.report_frame3.grid_propagate(0)

        self.HeadingLabel3 = Label(self.report_frame3, bg = "DodgerBlue4", fg = "white", width = 30,
                                padx = 10, pady = 10, text = "Science Quiz", font = ("Arial", "18", "bold"))
        self.HeadingLabel3.grid(row = 1, columnspan = 5) #grid is a geometry maangare which allows us to move widgets in a table like structure  

        ReportPage_info = ["Name", "Age", "Score"]
        self.report_labels = []
        

        for i in range(len(ReportPage_info)):   #reportpage information is stored as a list so it can be printed together.
            lb = Label(self.report_frame3, text = ReportPage_info[i], anchor = W, width = "7",
                     height = "2", font = ("Arial", "16", "bold"))
            self.report_labels.append(lb)
            lb.grid(row = 2, column = i+1, sticky = "EW")  #the users variable information, will be printed inr row  but 1 more column forward then its corresponding label

        self.report_name = Label(self.report_frame3, textvariable = self.name) #blank label to print out users, name
        self.report_name.grid(row = 3, column = 1, sticky = "W")

        self.report_age = Label(self.report_frame3, textvariable = self.age)  #blank label to print out users age
        self.report_age.grid(row = 3, column = 2, sticky = "W")
 
        self.report_score = Label(self.report_frame3,text = "") #blank label to print out users, score        
        self.report_score.grid(row = 3, column = 3, sticky = "W")

        self.placeholder3 = Label(self.report_frame3)
        self.placeholder3.grid(row = 4, column = 0)

        self.placeholder4 = Label(self.report_frame3)
        self.placeholder4.grid(row = 5, column = 0)        

        self.Restart_Button = Button(self.report_frame3, text = "Restart", anchor = W, command = self.restart)
        self.Restart_Button.grid(row = 6, column = 3)

#-------------- functions for frames and widgets------------------------------------------------

    def show_frame1(self):
        self.frame2.grid_remove() #grid removes frame 2 grid from frame 1
        self.report_frame3.grid_remove() #this removes the report
        self.frame1.grid()

    def show_frame2(self):
#-------------------Name input error checking-------------------------------------------------------------
        try:
            if self.name.get() == "":
                self.warning.configure(text = "Please enter your name", font = ("Arial", "8"))
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False: #isalpha has been used to check if user has entered letters, which means it detects when the user has entered numbers
                self.warning.configure(text = "Please enter text") #I have used .confgure to change the text, based on the users inputs
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
#---Age input error checking---------------------------------------------------------------------------------
            elif self.AgeEntry.get() == "":   #elif statement is for when the user does not enter anything they will get a warining message
                self.warning.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 14:         #when the users age inputed is more than 14, he will get a warnign message and cannot play the quiz
                self.warning.configure(text = "Sorry, You are to old")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <= 0:
                self.warning.configure(text = "Please enter a number number other than 0")
                self.age_entry.delete(0, END)
            elif self.age.get() <= 7:
                self.warning.configure(text = "Sorry, You are to young")
            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.Questions_func()

            

        except TclError: #TCLError is used in the except statement opposed to value error as we wspecifically need the program to detect
            #numbers coming into the entry box and can give a warnig message back
            self.warning.configure(text = "Please enter a number") #Warning message when user enters something other than a number
            self.AgeEntry.delete(0,END)
            self.AgeEntry.focus()

    def restart(self): #this dunction is so that at the end of the quiz the user can restart it if they want, it corresponds to a button
        self.frame2.grid_remove() 
        self.report_frame3.grid_remove()
        restart = ScienceQuiz(root)


#----------------------------------------Checking question answers---------------------------------------------------------------------------------
    def check_answer(self):
        try:
            ans = self.Answer_Input.get()
       
            if ans.lower() == self.answer.lower(): #here we are using .lower, on the answer given and ond the stored answer,
#this only works as it tells the program that the question is not case sensative, and also th answer is not case sensitive. 
                self.feedback.configure(text = "Correct!")
                self.running_score += 1                      #when the user's answer matches the answer in the dictionary, a correct message is displayed,  
                self.Answer_Input.delete(0, END)             #the points system is updated, the question number is updated
                self.Answer_Input.focus()
                self.Questions_func()
            else:
                self.feedback.configure(text = "Incorrect") #I have used a else statement for an incorrect statement so that when the user,
                self.Answer_Input.delete(0, END)            #enters anything but the answer it prints out an incrorect message and does not give them a point
                self.Answer_Input.focus()   
                self.Questions_func()
           
        except ValueError:
            self.feedback.configure(text = "Incorrect")
            self.Answer_Input.delete(0, END)
            self.Answer_Input.focus()
       
        if self.running_score <= 5: 
            self.report_score.configure(text = str(self.running_score))

#----------------------------------------Displaying the Questions-----------------------------------------------------------------------------------------------------
#questions function, which houses the questions which are stored in dictionaries, a dictionary is a unordered, changable and indexed collection, items in thee dictionary are key's
#and comee in pairs
    def Questions_func(self):
        ScienceQuestions = {1:{'What star shines in the day and gives us light? ':'sun', 'What is the young one of a cow called?':'calf',
                        'What do birds use to fly? ':'wings', 'what gas do humans use to breath?':'oxygen','what insect has 8 legs?':'spider','What do Chickens lay?':'eggs','What do Cows produce?':'milk'},

                    2:{"What do Bee's collect from flowers?":'pollen', 'Is a Tomato conidered a fruit or a vegetable?':'fruit', 'How many bones do humans have?':'206',
                       'What body part allows us to smell?':'nose', 'How many planets are in the solar system?':'8', "Pluto is a planet, true or false":"false","What season has the most rain?":'winter',
                       'What measuring system do we use in New Zealand?':'metric'},                     

                    3:{'Which organ covers the entire body and protects it?':'skin', 'If one boils water it will convert into?':'steam', 'When you push something, you apply a?':'force',
                       'Animals that eat both plants and meat, called?':'omnivores', 'Which is the closest planet to the sun?':'mercury', 'Where is lightning formed during thunderstorms?'
                       :'clouds','Atoms with a positive charge is called?':'proton'}}
        
#--------Easy Level Questions----------------------------------------------------------------
        
        if int(self.diff_lvl.get()) == 0:   #the collection of questions are called, when the user selects a difficulty level, the corresponding level to the collection will be printed out,
            question = choice(list(ScienceQuestions[1].keys())) #such as down below when the user selects the easy level, question set 1 or the easy questions will print out
            self.answer = ScienceQuestions[1][question]
            self.QuestionNumber += 1
            self.Question_Label.configure(text = question)
            self.quiz_label.configure(text = "Q. " + str(self.QuestionNumber)+ "/5")

#--------Medium Level Questions----------------------------------------------------------------

        elif int(self.diff_lvl.get()) == 1: #when the medium radio button is selected the corresponind collection will print, this case being set 2
            question = choice(list(ScienceQuestions[2].keys())) #the choice method is used to selected any random question out of the dictionary, it is a method included in the "random" module
           
            self.answer = ScienceQuestions[2][question]
            self.QuestionNumber += 1
           
            self.Question_Label.configure(text = question)
            self.quiz_label.configure(text = "Q. " + str(self.QuestionNumber)+ "/5")

#--------Hard Level Questions----------------------------------------------------------------
       
        else:
           
            question = choice(list(ScienceQuestions[3].keys()))
           
            self.answer = ScienceQuestions[3][question]
            self.QuestionNumber += 1
           
            self.Question_Label.configure(text = question)
            self.quiz_label.configure(text = "Q. " + str(self.QuestionNumber)+ "/5")   #while doing the questions the question number will appear, it is updated after the user checks the question
#it is printed by a constant text "Q", and added with a variable which changes based on the number of questions hte user has answered
           
        if self.QuestionNumber >= 6:
            self.frame2.grid_remove()
            self.report_frame3.grid(row = 1, columnspan = 4)

#----------------Main-Routine---------------------------------------------------------------------                  
if __name__ == "__main__":
    root = Tk()                  #this forms the gui
    frames = ScienceQuiz(root) 
    root.title("ScienceQuiz")    #the title of the gui 
    root.mainloop()
        
        
        

        
        
        
        
        
        
        

    


                                                                            
                                                                               
                                                                            
                                
        
