from file_writer import *
from os_module import *
from ScrolledText import *

__author__ = 'Anton Grudkin'


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

        open_files_flag = BooleanVar()
        flag = Checkbutton(self, text='Open files after closing', variable=open_files_flag)
        flag.grid(row=4, column=0)

        self.gui_console = ScrolledText(self, width=40, height=4)
        self.gui_console.grid(row=5, column=0, columnspan=2, sticky=W+E+N+S)

        Button(self, text='Add',
               command=(lambda: self.add(int(count.get()),
                                         int(sum_cont.get()),
                                         int(deg.get()),
                                         int(cof.get())
                                         )
                        )
               ).grid(row=10, column=0)
        Button(self, text='Compile', command=(lambda: self.compile(self, open_files_flag.get(), False))
               ).grid(row=10, column=1)

        Button(self, text='Compile and close', command=(lambda: self.compile(self, open_files_flag.get(), True))
               ).grid(row=11, column=1)

        Button(self, text='Close without compiling', command=(lambda: self.quit())
               ).grid(row=12, column=1)


    def add(self, count=10, sum_count=5, deg=4, cof=20):
        polygen_writer(count, sum_count, deg, cof)
        self.gui_console.insert(INSERT, 'Added!\n')
        print 'Added print'


    @staticmethod
    def compile(self, open_files_flag=False, close_flag=False):
        print "gen_close | current direction: " + str(os.getcwd())
        ground_writer()
        problems.close()
        answers.close()
        generate_pdf(answers_filename, open_files_flag)
        generate_pdf(problems_filename, open_files_flag)
        if close_flag:
            self.quit()


class IORedirect(MainGui):
    def write(self, text):
        self.gui_console.insert(INSERT, text)


head_writer()
print("Started")

if __name__ == '__main__':
    window = MainGui()
    window.pack()
    window.mainloop()
    # sys.stdout = IORedirect()

# sys.stdout = sys.__stdout__
print("Finished")
