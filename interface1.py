from tkinter import *
from tkinter.messagebox import showinfo
from polygen import *
import os
import subprocess
from error_codes import *

__author__ = 'Anton Grudkin'

head_file = open("tex\head.tex", 'r')
ground_file = open("tex\ground.tex", 'r')


def check_output_filename(filename_input):
    """string"""
    filename = filename_input
    copy = 0
    while True:
        try:
            os.unlink(filename + '.pdf')
            break
        except BaseException as err:
            error_code = int(format(err).split(']')[0].split(' ')[1])
            if error_code != 2:
                showinfo(title='popup', message=error_code_message(error_code, filename + ".pdf"))
            copy += 1
            if copy == 1:
                filename += '(' + format(copy) + ')'
            else:
                filename.replace('(' + format(copy - 1) + ')', '(' + format(copy) + ')')
            if error_code == 2:
                break
            print(error_code)
    # print (filename)
    return filename

answers_filename = check_output_filename('answers')
problems_filename = check_output_filename('problems')

answers = open(answers_filename + '.tex', 'w')
problems = open(problems_filename + '.tex', 'w')

open_files_flag = BooleanVar


def head_writer():
    head = head_file.read()
    problems.write(head)
    answers.write(head)


def ground_writer():
    ground = ground_file.read()
    problems.write(ground)
    answers.write(ground)


def polygen_writer(count=10, sum_count=5, deg=4, cof=20):
    t = polygen(count, sum_count, deg, cof)
    problems.write(t[0])
    answers.write(t[1])

# parameters = [count, sum_count, degree]


def generate_pdf(filename):

    # print(filename)
    cmd = ['pdflatex', '-interaction', 'nonstopmode', filename+'.tex']
    process = subprocess.Popen(cmd)
    process.communicate()

    os.unlink(filename+'.aux')
    os.unlink(filename+'.log')

    return_code = process.returncode

    if not return_code == 0:
        os.unlink(filename+'.pdf')
        raise ValueError('Error {} executing command: {}'.format(return_code, ' '.join(cmd)))

    else:
        if open_files_flag:
            os.startfile(filename+'.pdf')


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

        flag = Checkbutton(self, text='Open files after closing', variable=open_files_flag)
        flag.grid(row=4, column=0)
        # flag.edit_modified()
        # open_files_flag = flag.getboolean(1)
        # Label(self, text='Coefficients dispersion:').grid(row=4, column=1)

        Button(self, text='Add',
               command=(lambda: self.add(int(count.get()),
                                         int(sum_cont.get()),
                                         int(deg.get()),
                                         int(cof.get())
                                         )
                        )
               ).grid(row=10, column=0)
        Button(self, text='Close', command=self.quit).grid(row=10, column=1)

    @staticmethod
    def add(count=10, sum_count=5, deg=4, cof=20):
        showinfo(title='popup', message='Ready!')
        polygen_writer(count, sum_count, deg, cof)


print("Started")

head_writer()

if __name__ == '__main__':
    window = MainGui()
    window.pack()
    window.mainloop()

ground_writer()
problems.close()
answers.close()

generate_pdf(answers_filename)
generate_pdf(problems_filename)

print("Finished")
