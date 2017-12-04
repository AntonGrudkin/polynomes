import os
import subprocess
from error_codes import *
from tkinter import *
from tkinter.messagebox import showinfo
# import _tr

__author__ = 'Anton Grudkin'

# open_files_flag = BooleanVar


def execute_os(cmd):
    """int"""
    print "execute_os | STARTED"
    print "execute_os | system output is in the lines"
    print "=========================================="
    returncode = subprocess.call(cmd, shell=True)
    print "=========================================="
    print "execute_os | process finished with exit code " + str(returncode)
    print "execute_os | ENDED"
    return returncode


def get_path(filename):
    """[path: str, filename: str]"""
    aux = filename.split('/')
    return ['/'.join(aux[:-1]), aux[-1]]


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
            if error_code == 2:
                break
            else:
                showinfo(title='Error', message=error_code_message(error_code, filename + ".pdf"))
            copy += 1
            # print copy
            if copy == 1:
                filename += '(' + format(copy) + ')'
            else:
                filename = filename.replace('(' + format(copy - 1) + ')', '(' + format(copy) + ')')
                # print filename
            # print(error_code)
    # print (filename)
    return filename


def generate_pdf(filename_long, open_files_flag=False):

    status = 0
    print "generate_pdf | open_files_flag = " + str(open_files_flag)
    path = get_path(filename_long)[0]
    filename = get_path(filename_long)[1]
    print "generate_pdf | going to change directory to " + str(path)
    try:
        os.chdir(path)
        print "generate_pdf | SUCCESS, current directory is " + str(os.getcwd())
    except:
        print "generate_pdf | FAILED, current directory is " + str(os.getcwd())
        status = 1

    cmd = ['pdflatex', '-interaction', 'nonstopmode', filename+'.tex']
    # cmd = ['dir']
    print "generate_pdf | going to execute following command in shell=TRUE regime : \n " + str(' '.join(cmd))

    return_code = execute_os(cmd)

    if return_code == 0:
        try:
            os.unlink(filename+'.aux')
            os.unlink(filename+'.log')
            print "generate_pdf | SUCCESS : .aux and .log files deleted successfully"
        except:
            print "generate_pdf | FAILED : .aux and .log files deleting failed"
            status = 1

        if open_files_flag:
            os.startfile(filename + '.pdf')
    else:
        # os.unlink(filename+'.pdf')
        # raise ValueError('Error {} executing command: {}'.format(return_code, ' '.join(cmd)))
        print "Error occurred while compiling file"
        status = 1

    os.chdir('../')
    print "generate_pdf | SUCCESS, current directory is " + str(os.getcwd())
    print "generate_pdf | ENDED"
    return status
