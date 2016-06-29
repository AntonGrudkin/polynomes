from file_writer import *
from os_module import *
from ScrolledText import *
# from Tkinter import Tk

__author__ = 'Anton Grudkin'


class MainGui(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        Label(self, text='Title:', justify=LEFT).grid(row=0, column=0, sticky=E)
        title_var = StringVar(self)
        title_var.set("Bring polynomes to standard form")
        title = Entry(self, textvariable=title_var, width=35)
        title.grid(row=0, column=1, sticky=W)

        Label(self, text='Count of tasks:', justify=LEFT).grid(row=1, column=0, sticky=E)
        count_var = StringVar(self)
        count_var.set("5")
        count = Spinbox(self, from_=0, to=10, textvariable=count_var, width=2)
        count.grid(row=1, column=1, sticky=W)

        Label(self, text='Count of summands in one task:', justify=LEFT).grid(row=2, column=0, sticky=E)
        sum_count_var = StringVar(self)
        sum_count_var.set("5")
        sum_cont = Spinbox(self, from_=0, to=10, textvariable=sum_count_var, width=2)
        sum_cont.grid(row=2, column=1, sticky=W)

        Label(self, text='Maximal degree:').grid(row=3, column=0, sticky=E)
        deg_var = StringVar(self)
        deg_var.set("5")
        deg = Spinbox(self, from_=0, to=10, textvariable=deg_var, width=2)
        deg.grid(row=3, column=1, sticky=W)

        Label(self, text='Coefficients dispersion:').grid(row=4, column=0, sticky=E)
        cof_var = StringVar(self)
        cof_var.set("5")
        cof = Spinbox(self, from_=0, to=10, textvariable=cof_var, width=2)
        cof.grid(row=4, column=1, sticky=W)

        open_files_flag = BooleanVar()
        flag = Checkbutton(self, text='Open files after closing', variable=open_files_flag)
        flag.grid(row=5, column=0, sticky=W)

        self.gui_console = ScrolledText(self, width=50, height=20)
        self.gui_console.grid(row=6, column=0, columnspan=2, sticky=W+E+N+S)

        self.menubar = Menu(self)

        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', underline=0, menu=file_menu)
        file_menu.add_command(label='Compile', underline=6, command=(lambda: self.compile(self, open_files_flag.get(),
                                                                                          False
                                                                                          )
                                                                     ),
                              accelerator="Ctrl+C")
        file_menu.add_command(label='Compile and close', underline=1,
                              command=(lambda: self.compile(self,
                                                            open_files_flag.get(),
                                                            True
                                                            )
                                       ),
                              accelerator="Alt+Q")
        file_menu.add_command(label='Close', underline=0, command=(lambda: self.quit()), accelerator="Ctrl+Q")

        edit_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', underline=0, menu=edit_menu)
        edit_menu.add_command(label='Add', underline=0, command=(lambda: self.add(title.get(),
                                                                                  int(count.get()),
                                                                                  int(sum_cont.get()),
                                                                                  int(deg.get()),
                                                                                  int(cof.get())
                                                                                  )
                                                                 ),
                              accelerator="Ctrl+A")
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(self, "config", "-menu", self.menubar)

        self.bind_all("<Control-q>", self.quit_event)
        self.bind_all("<Alt-q>", self.compile_and_quit_event)
        self.bind_all("<Control-a>", self.add_event)
        self.bind_all("<Control-c>", self.compile_event)

    def add(self, title=None, count=10, sum_count=5, deg=4, cof=20):
        polygen_writer(title, count, sum_count, deg, cof)
        # self.gui_console.insert(INSERT, 'Added!\n')
        print 'Added print'

    @staticmethod
    def compile(self, open_files_flag=False, close_flag=False):
        print "gen_close | current direction: " + str(os.getcwd())
        ground_writer()
        problems.close()
        answers.close()
        print 'Files closed'
        status = generate_pdf(answers_filename, open_files_flag)
        if status == 0:
            self.gui_console.insert(INSERT, 'File ' + answers_filename + '.tex compiled successfully...\n')
        else:
            self.gui_console.insert(INSERT, 'Error occurred while compiling file ' + answers_filename + '.tex...\n')
        status = generate_pdf(problems_filename, open_files_flag)
        if status == 0:
            self.gui_console.insert(INSERT, 'File ' + problems_filename + '.tex compiled successfully...\n')
        else:
            self.gui_console.insert(INSERT, 'Error occurred while compiling file ' + problems_filename + '.tex...\n')
        if close_flag:
            self.quit()

    def add_event(self, event):
        self.add()

    def compile_event(self, event):
        self.compile(self)

    def compile_and_quit_event(self, event):
        self.compile(self)
        self.quit()

    def quit_event(self, event):
        self.quit()


class IORedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert(INSERT, string)

head_writer()
print("Started")

top = Tk()
top.title('Polynomes')
top.wm_iconbitmap("ico\\icon2.ico")

if __name__ == '__main__':
    window = MainGui(top)
    sys.stdout = IORedirector(window.gui_console)
    sys.stderr = IORedirector(window.gui_console)
    print("Started")
    window.pack()
    window.mainloop()

sys.stdout = sys.__stdout__
print("Finished")
