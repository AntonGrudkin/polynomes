from file_writer import *
from os_module import *
from ScrolledText import *
# from Tkinter import Tk

__author__ = 'Anton Grudkin'


class MainGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        Label(self, text='Count of tasks:', justify=LEFT).grid(row=0, column=0, sticky=E)
        count_var = StringVar(self)
        count_var.set("5")
        count = Spinbox(self, from_=0, to=10, textvariable=count_var)
        count.grid(row=0, column=1)

        Label(self, text='Count of summands in one task:', justify=LEFT).grid(row=1, column=0, sticky=E)
        sum_count_var = StringVar(self)
        sum_count_var.set("5")
        sum_cont = Spinbox(self, from_=0, to=10, textvariable=sum_count_var)
        sum_cont.grid(row=1, column=1)

        Label(self, text='Maximal degree:').grid(row=2, column=0, sticky=E)
        deg_var = StringVar(self)
        deg_var.set("5")
        deg = Spinbox(self, from_=0, to=10, textvariable=deg_var)
        deg.grid(row=2, column=1)

        Label(self, text='Coefficients dispersion:').grid(row=3, column=0, sticky=E)
        cof_var = StringVar(self)
        cof_var.set("5")
        cof = Spinbox(self, from_=0, to=10, textvariable=cof_var)
        cof.grid(row=3, column=1)

        open_files_flag = BooleanVar()
        flag = Checkbutton(self, text='Open files after closing', variable=open_files_flag)
        flag.grid(row=4, column=0)

        self.gui_console = ScrolledText(self, width=40, height=4)
        self.gui_console.grid(row=5, column=0, columnspan=2, sticky=W+E+N+S)

        self.menubar = Menu(self)

        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', underline=0, menu=file_menu)
        file_menu.add_command(label='Compile', underline=6, command=(lambda: self.compile(self, open_files_flag.get(),
                                                                                          False
                                                                                          )
                                                                     )
                              )
        file_menu.add_command(label='Compile and close', underline=1,
                              command=(lambda: self.compile(self,
                                                            open_files_flag.get(),
                                                            True
                                                            )
                                       )
                              )
        file_menu.add_command(label='Close', underline=0, command=(lambda: self.quit()), accelerator="Ctrl+Q")

        edit_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', underline=0, menu=edit_menu)
        edit_menu.add_command(label='Add', underline=0, command=(lambda: self.add(int(count.get()),
                                                                                  int(sum_cont.get()),
                                                                                  int(deg.get()),
                                                                                  int(cof.get())
                                                                                  )
                                                                 )
                              )
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(self, "config", "-menu", self.menubar)

        self.bind_all("<Control-q>", self.quit_event)
        self.bind_all("<Control-Shift-q>", self.quit)

    def quit_event(self, event):
        sys.exit(0)

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
        print 'Files closed'
        generate_pdf(answers_filename, open_files_flag)
        generate_pdf(problems_filename, open_files_flag)
        if close_flag:
            self.quit()


class IORedirect(MainGui):
    def write(self, text):
        self.gui_console.insert(INSERT, text)


head_writer()
print("Started")

top = Tk()
top.title('Polynomes')
top.wm_iconbitmap("ico\\icon2.ico")

if __name__ == '__main__':
    window = MainGui(top)
    window.pack()
    window.mainloop()
    # sys.stdout = IORedirect()

# sys.stdout = sys.__stdout__
print("Finished")
