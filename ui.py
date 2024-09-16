from tkinter import *
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: quiz_brain.QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quiz app")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question = self.canvas.create_text(150, 125, text="question", width=250, font=("Arial", 15, "italic"))

        self.score = Label(text="score: 0",
                           bg=THEME_COLOR, highlightthickness=0,
                           font=("Arial", 15, "normal"),
                           fg="white")
        self.score.grid(row=0, column=1)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true = Button(image=self.true_image, highlightthickness=0, command=self.say_true)
        self.true.grid(row=3, column=1)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false = Button(image=self.false_image, highlightthickness=0, command=self.say_false)
        self.false.grid(row=3, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="Quiz end")
            self.true.config(command=self.do_nothing)
            self.false.config(command=self.do_nothing)

    def say_true(self):
        checking = self.quiz.check_answer("true")
        self.interact(checking)

    def say_false(self):
        checking = self.quiz.check_answer("false")
        self.interact(checking)

    def interact(self, answer: bool):
        if answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)

    def do_nothing(self):
        pass
