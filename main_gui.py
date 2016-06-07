from file_writer import *
from os_module import *
import os
import subprocess
from error_codes import *
from Tkinter import *
from tkinter.messagebox import showinfo
import Tkinter as tk

__author__ = 'Anton Grudkin'

flag = False


class MainGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        Label(self, text='Count of tasks:').grid(row=0, column=0)
        count = Entry(self)
        count.grid(row=0, column=1)
        count.insert(0, '5')

        Label(self, text='Count of summands in one task:').grid(row=1, column=0)
        sum_cont = Entry(self)
        sum_cont.grid(row=1, column=1)
        sum_cont.insert(0, '5')

        Label(self, text='Maximal degree:').grid(row=2, column=0)
        deg = Entry(self)
        deg.grid(row=2, column=1)
        deg.insert(0, '5')

        Label(self, text='Coefficients dispersion:').grid(row=3, column=0)
        cof = Entry(self)
        cof.grid(row=3, column=1)
        cof.insert(0, '5')

        self.open_files = BooleanVar(master=self)
        Checkbutton(self, text='Open files after closing', variable=self.open_files).grid(row=4, column=0)

        Button(self, text='Add',
               command=(lambda: self.add(int(count.get()),
                                         int(sum_cont.get()),
                                         int(deg.get()),
                                         int(cof.get())
                                         )
                        )
               ).grid(row=10, column=0)
        Button(self, text='Close', command=(lambda: self.finish())).grid(row=10, column=1)

    @staticmethod
    def add(count=10, sum_count=5, deg=4, cof=20):
        showinfo(title='popup', message='Ready!')
        polygen_writer(count, sum_count, deg, cof)

    def finish(self):
        print 'quit'
        print str(self.open_files.get())
        ground_writer()
        generate_pdf(answers_filename, self.open_files.get())
        generate_pdf(problems_filename, self.open_files.get())
        self.quit()

print("Started")

head_writer()

if __name__ == '__main__':
    window = MainGui()
    window.pack()
    window.mainloop()

problems.close()
answers.close()

print("Finished")
