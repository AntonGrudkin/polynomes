from tkinter import *
from tkinter.messagebox import showinfo
from polygen import *

__author__ = 'Anton Grudkin'

head_file = open("head.tex", 'r')
ground_file = open("ground.tex", 'r')

problems = open("problems.tex", 'w')
answers = open("answers.tex", 'w')


def head_writer():
    head = head_file.read()
    problems.write(head)
    answers.write(head)


def ground_writer():
    ground = ground_file.read()
    problems.write(ground)
    answers.write(ground)


def polygen_writer(count = 10, sum_count = 5, deg = 4, cof = 20):
    t = polygen(count, sum_count, deg, cof)
    problems.write(t[0])
    answers.write(t[1])

# parameters = [count, sum_count, degree]


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Label(self, text='Count of tasks:').grid(row=0, column=0)
        count = Entry(self)
        count.grid(row=0, column=1)
        Label(self, text='Count of summands in one task:').grid(row=1, column=0)
        sum_cont = Entry(self)
        sum_cont.grid(row=1, column=1)
        Label(self, text='Maximal degree:').grid(row=2, column=0)
        deg = Entry(self)
        deg.grid(row=2, column=1)
        Label(self, text='Coefficients dispersion:').grid(row=3, column=0)
        cof = Entry(self)
        cof.grid(row=3, column=1)

        Button(self, text='Add',
               command=(lambda: self.add(int(count.get()),
                                         int(sum_cont.get()),
                                         int(deg.get()),
                                         int(cof.get())
                                         )
                        )
               ).grid(row=10, column=0)
        Button(self, text='Close', command=self.quit).grid(row=10, column=1)
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)

    @staticmethod
    def add(count=10, sum_count=5, deg=4, cof=20):
        showinfo(title='popup', message='Ready!')
        polygen_writer(count, sum_count, deg, cof)


# noinspection PyRedeclaration
problems = open("problems.tex", 'w')
# noinspection PyRedeclaration
answers = open("answers.tex", 'w')
head_writer()
print("Started")

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()

ground_writer()
problems.close()
answers.close()
print("Finished")