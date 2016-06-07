import os
import subprocess
from error_codes import *
from tkinter import *
from tkinter.messagebox import showinfo

__author__ = 'Anton Grudkin'

open_files_flag = BooleanVar


def execute_os(cmd):
    """int"""
    process = subprocess.Popen(cmd)
    process.communicate()
    return process.returncode


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


def generate_pdf(filename_long):

    path = get_path(filename_long)[0]
    filename = get_path(filename_long)[1]
    os.chdir(path)

    cmd = ['pdflatex', '-interaction', 'nonstopmode', filename+'.tex']
    return_code = execute_os(cmd)

    os.unlink(filename+'.aux')
    os.unlink(filename+'.log')

    if not return_code == 0:
        os.unlink(filename+'.pdf')
        raise ValueError('Error {} executing command: {}'.format(return_code, ' '.join(cmd)))

    else:
        if open_files_flag:
            os.startfile(filename+'.pdf')

    os.chdir('../')