#ScienceQuiz_V7.py
#Version 7 of my Science Quiz Assignment
#Divesh Chand, May 2020


#This imports the tool kit interface(tkinter) and the ttk interface, which is a GUI package.
from tkinter import *
import random
from tkinter import ttk


#This is a class for this Science Quiz. The use of the class function is that it allows objects to be created.
class SCI_Quiz:
    #The __init__ method can be called when an object is created from the class, and access is required to initialize the attributes of the class.
    def __init__ (self, parent):

        
        #Widgets which are being used for the loginframe frame. This includes all labels, entry widgets and buttons(including radio buttons).
        self.loginframe = Frame(parent)
        self.loginframe.grid(row = 0, column = 0)
        
        #Title Widget
        #This is a label where the text greets the user to the quiz.
        self.title_label = Label(self.loginframe, bg = "purple", fg = "white", width = 20, padx = 30, pady = 10,
                                 text = "Welcome to my Science Quiz!", font=("Calibri", "20", "bold italic"))
        self.title_label.grid(columnspan = 3)
        
        #Name Widgets
        #This name label asks the user to enter their name.
        self.name_label = Label(self.loginframe, text = "Enter your First Name: ")
        self.name_label.grid(row = 2, column = 1)#The grid function adjusts the position of the label.
        #Below is a String Var , holds the stringvalue.
        self.name = StringVar()
        #This sets the answer entered into the name variable.
        self.name.set("")
        #This is a textbox where the user can enter their name.
        self.name_entry = ttk.Entry(self.loginframe, textvariable = self.name)
        self.name_entry.grid(row = 3, column = 1)
        
        #Age Widgets
        #This label is where it asks the user to enter their age.
        self.age_label = Label(self.loginframe, text = "Enter your Age: ")
        self.age_label.grid(row = 4, column = 1)
        #Below is a Integer Var , holds the integer value.
        self.age = IntVar ()
        #This sets the answer entered into the age variable.
        self.age.set("")
        #This is a textbox where the user can enter their age.
        self.age_entry = ttk.Entry(self.loginframe, textvariable = self.age)
        self.age_entry.grid(row = 5, column = 1)

        #Year Level Widgets
        #This label is where it asks user to enter their year level
        self.yearlvl_label = Label(self.loginframe, text = "Enter your Year Level: ")
        self.yearlvl_label.grid(row = 6, column = 1)
        #Below is a Integer Var , holds the integer value.
        self.yearlvl = IntVar()
        #This sets the answer entered into the yearlvl variable.
        self.yearlvl.set("")
        #This is a textbox where the user can enter their year level.
        self.yearlvl_entry = ttk.Entry(self.loginframe, textvariable = self.yearlvl)
        self.yearlvl_entry.grid(row = 7, column = 1)

        #Warning Label - this is needed for the programming logic to work. 
        self.warning_label = Label(self.loginframe, text = "")
        self.warning_label.grid(row = 8, column = 1)

        #Difficulty Widgets
        #This is a label where it asks the user to select a difficulty level.
        self.SelectLabel = Label(self.loginframe, text = "Select a Difficulty Level: ", width = 20, font = ("Calibri", "14", "bold italic"))
        self.SelectLabel.grid(row = 9, column = 1)

        #Radio Buttons
        #This labels each if the indiviual level radio buttons.
        self.diff = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        #This makes sure at the start of the quiz, it will stay at the easy level.
        self.diff_lvl.set(0)
        #Makes a list of the difficulty level radio buttons, which is used for different level questions.
        self.diff_btns = []

        #Makes positioning and size of the radio buttons. 
        for i in range(len(self.diff)):
            rb = Radiobutton(self.loginframe, variable = self.diff_lvl, value = i, text = self.diff[i], anchor = W, padx = 50, width = "10", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+10, column = 1, sticky = W)

        #This is a submit button where it will go to the question frame.
        self.submit_button = Button(self.loginframe, text = "Submit", anchor = W, command = self.display_questionframe)
        self.submit_button.grid(row = 14, column = 1)

        #This is an image button, where it can display an image which is entered.
        #This finds the image in the folder, and uses it in the code.
        '''
        self.pic = PhotoImage(file="chempic.png")
        #This makes sure the image used is in the loginframe.
        self.pic_label = Label(self.loginframe, image = self.pic)
        #This connects the image and the label together.
        self.pic_label.image = self.pic
        #Sets the row and position for the image.
        self.pic_label.grid(row = 15, column = 1)
        '''



        #Widgets which will be used for the questionframe frame.
        #This make the self.index value to 0 once the quiz starts.
        self.index = 0
        #This makes sure the user's score value is 0 once the quiz starts.
        self.score = 0
        #This sets up the questionframe frame.
        self.questionframe = Frame(parent, height = "450", width = "400")

        #This acts as a title for the questionframe frame, where it displays the Science Quiz Questions.
        self.questions = Label(self.questionframe, bg = "purple", fg = "white", width = 50, padx = 30, pady = 10, text = "Science Quiz Questions", font=("Calibri", "20", "bold italic"))
        self.questions.grid(row = 0, columnspan = 3)

        #This acts as a empty placeholder, where the questions being asked will be displayed. 
        self.QuestionLabel = Label(self.questionframe, text = "Click Next", width = 45, height = 3, font = ("Calibri", "11", "italic"))
        self.QuestionLabel.grid(row = 2, column = 0, sticky = E)

        #This is an entry text box where the user enters their answer to the questions.
        self.ans_entry = Entry(self.questionframe, width = 20)
        self.ans_entry.grid(row = 2, column = 1, sticky = W)

        #This is the question number is displayed, where it will change based on the progression of the code.
        self.quiz_label = Label(self.questionframe, text = "Problems", font = ("Calibri", "14", "bold italic"))
        self.quiz_label.grid(row = 1, column = 0, columnspan = 8, sticky = "EW")

        #This is a label where feedback will be displayed on what the user enters, whether answer is correct or not.
        self.feedback = Label(self.questionframe, text = "Start the quiz by answering question", font = ("Calibri", "10", "italic"))
        self.feedback.grid(row = 3, column = 0, columnspan = 4)

        #This is a button where it allows the user to go back to the loginframe screen.
        self.home = Button(self.questionframe, text = "Back", anchor = W, command = self.display_loginframe)
        self.home.grid(row = 4, column = 0)

        #This allows the user to enter their answer and go to the next picture.
        self.check = Button(self.questionframe, text = "Next", anchor = W, command = self.check_solution)
        self.check.grid(row = 4, column = 1)




        #Widgets for Report Frame
        self.report_frame = Frame(parent, height = "250", width = "450")
        self.report_frame.grid_propagate(0)

        #This displays the titles for the user's age, name and score
        report_page = ["Name", "Age", "Year Level", " Score"]
        self.report_labels = []

        #This shows the positioning and size of the different labels of the name, age and score.
        for i in range(len(report_page)):
            lb = Label(self.report_frame, bg = "purple", fg = "white", text = report_page[i], anchor = W, width = "9", height = "2", font=("Calibri", "18", "bold italic"))
            lb.grid(row = 2, column = i+1, sticky = "EW")

        #This is a entry where the user's name gets displayed.
        self.report_name = Label(self.report_frame, textvariable = self.name)
        self.report_name.grid(row = 4, column = 1, sticky = "EW")

        #This is a entry where the user's age gets displayed.
        self.report_age = Label(self.report_frame, textvariable = self.age)
        self.report_age.grid(row = 4, column = 2, sticky = "EW")

        #This is a entry where the user's year level gets displayed
        self.report_yearlvl = Label(self.report_frame, textvariable = self.yearlvl)
        self.report_yearlvl.grid(row = 4, column = 3, sticky = "EW")

        #This is a entry where the user's report gets displayed.
        self.report_score = Label(self.report_frame, text = "")
        self.report_score.grid(row = 4, column = 4)


        #This is an image button, where it can display an image which is entered.
        #This finds the image in the folder, and uses it in the code.
        '''
        self.reportpic = PhotoImage(file="resultpic.png")
        #This makes sure the image used is in the loginframe.
        self.reportpic_label = Label(self.report_frame, image = self.reportpic)
        #This connects the image and the label together.
        self.reportpic_label.image = self.reportpic
        #Sets the row and position for the image.
        self.reportpic_label.grid(row = 6, column = 2)
        '''
        #This is a button for the user to restart the quiz once it has been completed.
        self.replay_button = Button(self.report_frame, text = "Play Again", anchor = W, command = self.replay)
        self.replay_button.grid(row = 7, column = 2)

        




    def display_loginframe(self):
        #This removes the questionframe frame.
        self.questionframe.grid_remove()
        #This makes sure that the loginframe frame appears.
        self.loginframe.grid()






    def display_questionframe(self):
        try:
            #This makes sure that the user enters a value when asked for a name.
            if self.name.get() == "":
                #This will display a message to tell the user they can't access the quiz without entring a name value.
                self.warning_label.configure(text = "ERROR: Please enter your name to start the Science Quiz.")
                self.name_entry.focus()
                
            #This will make sure that the user enters a single name, not 2 names. This is indicated if there is a space between words, or preventing if the user only uses the spacebar fot a name.
            elif self.name.get().isalpha() == False:
                #This will display a message to the user telling them they need to enter a singular name, first name.
                self.warning_label.configure(text = "ERROR: Please enter your first name to continue.")
                #This deletes the age entered
                self.name_entry.delete(0, END)
                self.name_entry.focus()

            #This makes sure that the user enters a value when asked for an age.
            elif self.age_entry.get() == "":
                #This will display a message to tell the user they can't access the quiz without entring an age value.
                self.warning_label.configure(text = "ERROR: Please enter your age to start the Science Quiz.")
                #This deletes the age entered
                self.age_entry.delete(0, END)

            #This will make sure the user is meets the age requirements, only ages between 9-13.This means if they enter a age value larger than 13 they will recieve a denial message.
            elif self.age.get() > 13:
                #This displays an error message that the user is too old to play the game.
                self.warning_label.configure(text = "ERROR: The age entered means you are too old to play.")
                #This deletes the age entered
                self.age_entry.delete(0, END)

            #This will make sure the user is meets the age requirements, only ages between 9-13.This will ensure the user enters a positive number.                
            elif self.age.get() <= 0:
                #This displays an error message for the user to enter an appropriate number, which is higher than 0.
                self.warning_label.configure(text = "ERROR: Please enter an appropriate age number.")
                #This deletes the age entered
                self.age_entry.delete(0, END)

            #This will make sure the user is meets the age requirements, only ages between 9-13. This means if the user enters a age lower than 9 they will recieve a denial message. 
            elif self.age.get() <= 8:
                #This displays an error message for the user, telling them they are too young to play this game.
                self.warning_label.configure(text = "ERROR: The age entered means you are too young to play.")
                self.age_entry.delete(0, END)

            #This makes sure that the user enters a value when asked for a year level.
            elif self.yearlvl_entry.get() == "":
                #This will display a message to tell the user they can't access the quiz without entring a year level.
                self.warning_label.configure(text = "ERROR: Please enter your year level to start the Science Quiz.")
                #This deletes the year level entered.
                self.yearlvl_entry.delete(0, END)

            #This will make sure the user is meets the year level, which meet the age requirements of only ages between 9-13.
            elif self.yearlvl.get() > 9:
                #This displays an error message that the user is too old to play the game
                self.warning_label.configure(text = "ERROR: The year level entered doesn't fit the age requirements.")
                #This deletes the age entered
                self.yearlvl_entry.delete(0, END)

            #This will make sure the user is meets the year level requirements, only years between 5-9.This will ensure the user enters a positive number
            elif self.yearlvl.get() <= 0:
                #This displays an error message for the user to enter an appropriate number, which is higher than 0.
                self.warning_label.configure(text = "ERROR: Please enter an appropriate year level.")
                #This deletes the year level entered.
                self.yearlvl_entry.delete(0, END)

            #This will make sure the user is meets the year level requirements, only ages between 5-9. This means if the user enters a year level lower than 5 they will recieve a denial message.
            elif self.yearlvl.get() < 4:
                #This displays an error message for the user, telling them they are too young to play this game
                self.warning_label.configure(text = "ERROR: Year level entered doesn't meet the age requirements.")
                #This deletes the year level entered
                self.yearlvl_entry.delete(0, END)

            else:
                #This is when the login details have been filled in appropraitely.
                self.loginframe.grid_remove()#Removes the loginframe screen.
                self.questionframe.grid(row = 1, columnspan = 4)
                self.next_query()#It will run the quiz_questions function.

        #This is when the user enters an unappropriate value.       
        except TclError:
            #Displays a message for the user to enter an appropriate value.
            self.warning_label.configure(text = "ERROR: Please enter appropraite value.")
            #This deletes the age entered.
            self.age_entry.focus()








    #This makes sure the solution is correct or not.
    def check_solution(self):
        try:
            #This makes sure the answer the user entered is equal to the real answer of the question.
            ans = self.ans_entry.get()

            #The .lower(), allows for the user's answer to be lower case or upper case. The other part of the code makes sure the answer the user entered is the same as the question answer.
            if ans.lower() == self.answer.lower():
                #This will display a correct message if the user gets the answer right.
                self.feedback.configure(text = "Correct. Well Done")
                #This will add one to the score of the user.
                self.score += 1
                #This will delete the answer the user previously entered.
                self.ans_entry.delete(0, END)
                self.ans_entry.focus()
                #This will ask the user the next question once the previous question has been answered.
                self.next_query()
            else:
                #This will display a message that the answer entered is incorrect.
                self.feedback.configure(text = "Incorrect. Nice Try.")
                #This will delete the answer the user previously entered, this is so the user can enter another answer.
                self.ans_entry.delete(0, END)
                self.ans_entry.focus()
                #This will ask the user the next question once the previous question has been answered.
                self.next_query()

        #This is used when the answer entered receives an innapropriate value.
        except ValueError:
            #This displays an error message that the message is inappropriate.
            self.feedback.configure(text = "Enter an appropriate answer.")
            #This deletes the answer entered from the text box, this is so the user can enter another answer.
            self.ans_entry.delete(0, END)
            self.ans_entry.focus()

        if self.score <= 5:
            self.report_score.configure(text = str(self.score))






    #This is a function for the replay widget above, where the user can start the quiz again.
    def replay(self):
        #Removes the question frame screen
        self.questionframe.grid_remove()
        #Removes the report frame screen
        self.report_frame.grid_remove()
        #Restarts the quiz
        replay = SCI_Quiz(root)





    def next_query(self):
        #These display all the questions which will be asked in my science quiz.
        questions = {1: {'True or False? The element H stands for Hydrogen?':'true', 'Is earth the largest planet':'no', 'Is the earth flat?':'no', 'True or False:Humans breathe in Carbon Dioxide?':'false',
                         'True or False:The griaffe is fastest animal.':'false', 'Is the sky blue?':'yes', 'Do cats have wings?':'no', 'True or False: He represents helium in peridoic table?':'true', 'Is the earth a planet?':'yes', 'Can kiwis fly?':'no'},
                     2: {'Is Potassium represented by Po?':'no', 'Is sponge a state of matter?':'no', 'True or False:The elephant is the largest animal.':'false', 'Is Jupiter the largest planet?':'yes',
                         'True or False: From Solid to liquid, the process is called melting.':'true', 'Can dogs drown in water?':'yes', 'Do moving objects have balanced forces?':'no', 'What is the smallest planet?':'mercury', 'True or False: Speed is measured in m/s.':'true', 'Is pluto an active planet?':'no'},
                     3: {'What element does C represent?.':'carbon', 'True or False: Centripetal force is a outward directed force?':'false', 'Is the wolf a mammal?':'true', 'True or False:Law of conservation states energy can be destroyed.':'false',
                         'Which planet has the most moons?':'jupiter', 'Do all bears have tails?':'yes', 'Does NZ use metric or imperial measuring system?':'metric', 'Are all forces balanced when object is in constant speed?':'yes', 'What element does Na represent?':'sodium', 'Do hampsters hibernate?':'yes'}}
        #This will make sure that the gui runs the easy level questions.
        if int(self.diff_lvl.get()) == 0:
            #This will run the questions in the easy level.
            question = random.choice(list(questions[1].keys()))

            #This will make sure the answer is correct with the answer given in the lists.
            self.answer = questions[1][question]
            self.index += 1

            #This will display the question where the QuestionLabel is placed.
            self.QuestionLabel.configure(text = question)
            #This is the question number, and it will chnage as the quiz runs.
            self.quiz_label.configure(text = "Question " + str(self.index)+ "/5")

        #This will make sure that the gui runs the medium level questions.
        elif int(self.diff_lvl.get()) == 1:
            #This will run the questions in the medium level.
            question = random.choice(list(questions[2].keys()))

            #This will make sure the answer is correct with the answer given in the lists.
            self.answer = questions[2][question]
            self.index += 1

            #This will display the question where the QuestionLabel is placed.
            self.QuestionLabel.configure(text = question)
            #This is the question number, and it will change as the quiz runs.
            self.quiz_label.configure(text = "Question " + str(self.index)+ "/5")


        else:
            #This will run the questions in the hard level.
            question = random.choice(list(questions[3].keys()))

            #This will make sure the answer is correct with the answer given in the lists.
            self.answer = questions[3][question]
            self.index += 1

            #This will display the question where the QuestionLabel is placed.
            self.QuestionLabel.configure(text = question)
            #This is the question number, and it will change as the quiz runs.
            self.quiz_label.configure(text = "Question " + str(self.index)+ "/5")

        #This makes sure only 5 questions are being asked.
        if self.index >= 6:
            #This removes the question screen.
            self.questionframe.grid_remove()
            #This displays the reportframe screen.
            self.report_frame.grid(row = 1, columnspan = 4)
            
        
            
        
        


#Main Routine
if __name__ == "__main__":#This checks to see if the class name is the same as the main module.
    #This is a variable which calls the module which allows the GUI to be created. 
    root = Tk()
    frames = SCI_Quiz(root)
    #This is the title of the window that the GUI is placed on.
    root.title("Divesh Chand's Science Quiz Application")
    #This runs the code in its entirity
    root.mainloop()
    

