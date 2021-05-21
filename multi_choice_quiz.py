""" Chapter 3, Task 5. A multiple choice quiz with questions read in from a file
    and enhancements such as the ability to retake/resume the quiz """

from tkinter import *

import random

class Question:

    def __init__(self, question, answer, dummies):
        """
            Accepts a question, the correct answer and a list of incorrect
            answers as parameters.
        """
        self.question = question
        self.answer = answer
        self.dummies = dummies
        self.set_answers()

    def set_answers(self):
        """
            Inserts the correct answer into a random position of the
            list of possible answers.
        """
        self.answers = self.dummies
        self.answers.insert(random.randrange(len(self.dummies)+1), self.answer)
  
class Quiz:

    def __init__(self, parent):
        """
            Sets up the GUI, including ensuring space is preserved for the
            message to the user to be displayed.The number of choices provided
            for each question is assumed to be the same.
        """ 
        self.parent = parent
        self.index = 0 # for keeping track of which question we are up to
        self.correct = 0 # for keeping track of how many the user has got correct
        #formatting constants
        PX = 10
        PY = 10
        PY_RADIO = 3

        # Creates a list of Question objects
        self.questions = []
        q_file = open("questions.txt")
        q_list = q_file.readlines()
        for line in q_list:
            line = line[:-1] # removing newline character from the end
            tokens = line.split(",")
            self.questions.append(Question(tokens[0], tokens[1], tokens[2:]))

        #Sets up the GUI
        self.question_section_label = Label(parent, text = "Question:", anchor = NW, width = 10, pady = PY, padx = PX)
        self.question_section_label.grid(row = 0, column = 0, sticky = NW)
        
        self.question_label = Label(parent, text = "",  anchor = NW, pady = PY, padx = PX, wraplength = 220, height = 2, width = 40)
        self.question_label.grid(row = 0, column = 1, sticky = NW)

        self.question_label.configure(text = self.questions[self.index].question)

        #Creates variable for Radiobuttons and sets it to zero so that
        #no options are shown as selected
        self.var = StringVar()
        self.var.set(0)

        # Radiobuttons are now stored in a list so that they may be easily
        # reconfigured for the next question. The number of choices provided
        # for each question is assumed to be the same
        self.rbs = []
        self.num_choices = len(self.questions[self.index].answers)
        for i in range(self.num_choices):
            ans_txt = self.questions[self.index].answers[i]
            self.rbs.append(Radiobutton(self.parent, text = ans_txt, variable = self.var, value = ans_txt, command = self.process_question, pady = 3))
            self.rbs[i].grid(row = i+1, column = 1,  sticky = NW)
            
        self.feedback = Label(parent, text = "", height = 3, font = ("Times", "12", "bold"), wraplength = 200)
        self.feedback.grid(row = self.num_choices + 1,  columnspan = 2)
        
        self.finish_btn = Button(parent, text = "Finish", width = 4, command = self.finish_quiz)
        self.finish_btn.grid(row = self.num_choices + 2, column = 0, sticky = W, padx = PX, pady = PY)
        
        self.next_btn = Button(parent, text = "Next", width = 4, command = self.next_question)
        self.next_btn.grid(row = self.num_choices + 2, column = 1, sticky = E, padx = PX, pady = PY)
 


    def process_question(self):
        """
            Disables the RadioButtons. Checks if the selected answer is the correct one and provides appropriate feedback
        """
        for rb in self.rbs:
            rb.configure(state = DISABLED)
        if self.var.get()==self.questions[self.index].answer:           
            self.correct += 1
            self.feedback.config(text = "Correct!  " + str(self.correct) + "/" + str(self.index + 1))
        else:
            self.feedback.config(text = "Incorrect! The answer is "+ self.questions[self.index].answer + "  " +
                                 str(self.correct) + "/" + str(self.index + 1))
    
            
    def next_question(self):
        """
            If the end of the question list has not been reached, the index is incremented and
            the question Label and Radiobuttons are reconfigured with the appropriate text from
            the next Question object. 
        """
        # There is still another question to ask                    
        if self.index < len(self.questions) - 1:
            for rb in self.rbs:
                rb.configure(state = NORMAL)
            self.index+=1
            self.question_label.configure(text = self.questions[self.index].question)

            self.var = StringVar()
            self.var.set(0)
            for i in range(len(self.questions[self.index].answers)):
                ans_txt = self.questions[self.index].answers[i]
                self.rbs[i].configure(text = ans_txt, variable = self.var, value = ans_txt )
            self.feedback.config(text = "", height = 3)
        else:
            self.finish_quiz()

    def finish_quiz(self):
        """ The question Labels and Radionbuttons are removed and the feedback label
            is reconfigured to display a message informing the user that the quiz is
            over and the number they got correct. The height of the feedback Label is
            also reconfigured to stop the window resizing too dramatically."""
        self.question_section_label.configure(text = "")
        self.question_label.configure(text = "")
        for rb in self.rbs:
            rb.grid_remove()
        self.feedback.config(text = "Quiz over. You got " + str(self.correct) + " out of " + str(self.index + 1),
                              height = 10)
        self.next_btn.grid_remove()
        self.finish_btn.configure( width = 15, command = self.resume_quiz)
        if self.index + 1 == len(self.questions):
            self.finish_btn.configure(text = "Retake Quiz")
        else:
            self.finish_btn.configure(text = "Resume Quiz")

            
    def resume_quiz(self):
        """ Presents either the next question from where they were up to (resume) or question 1(retake)"""
        if self.index + 1 == len(self.questions):
            self.correct = 0
            self.index = -1
        for rb in self.rbs:
            rb.grid()
        # replacing a few bits not covered in self.next_question
        self.question_section_label.configure(text = "")
        self.finish_btn.configure(text = "Finish", width = 10, command = self.finish_quiz)
        self.next_btn.grid()
        # Presents either the next question from where they were up to or question 1
        self.next_question()
        
#main routine
if __name__ == "__main__":
    root= Tk()
    buttons = Quiz(root)
    root.mainloop()




