from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.__CANVAS_WIDTH=300
        self.__CANVAS_HEIGHT=250
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score=Label(text="Score: 0",font=("Arial",15))
        self.score.config(padx=5,pady=5,bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)
        self.canvas = Canvas( width=self.__CANVAS_WIDTH, height=self.__CANVAS_HEIGHT,bg="white")
        # self.canvas.create_rectangle((10,10,30,30),fill="red")
        self.text=self.canvas.create_text(150,125,width=280,text="Some question here",font=FONT,fill=THEME_COLOR)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.r_img=PhotoImage(file="images/true.png")
        self.correct=Button(image=self.r_img,highlightthickness=0,command=self.true_clicked,bd=0,activebackground=THEME_COLOR)
        self.correct.grid(row=2,column=0,padx=10,pady=10)
        self.w_img=PhotoImage(file="images/false.png")
        self.wrong=Button(image=self.w_img,highlightthickness=0,bd=0,command=self.false_clicked,activebackground=THEME_COLOR)
        self.wrong.grid(row=2,column=1,padx=10,pady=10)
        # self.right.grid(row=2,column=0,columnspan=2)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_text)
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text,
                                   text=f"You've completed the quiz\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_clicked(self):
        check=self.quiz.check_answer("True")
        self.give_feedback(check)


        # self.get_next_question()
    def false_clicked(self):
        check=self.quiz.check_answer("False")
        self.give_feedback(check)
        # self.get_next_question()
    def give_feedback(self,check):
        if check:
            feedback=self.canvas.config(bg="green")
            print("chill")
        else:
            feedback=self.canvas.config(bg="red")
            print("it's fine")
        # self.canvas.itemconfig(self.text,fill=THEME_COLOR)
        self.window.after(1000,self.get_next_question)
        if check==None:
            self.window.after_cancel(feedback)




