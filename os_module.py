import os
import subprocess
import tempfile
import shutil
from subprocess import call
from error_codes import *
from Tkinter import *
# from main_gui import *
from tkinter.messagebox import showinfo

__author__ = 'Anton Grudkin'

open_files_flag = False


def execute_os(cmd):
    """int"""
    # os.system(' '.join(cmd))
    process = subprocess.Popen(cmd)
    process.communicate()
    return process.returncode, process.stdout


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


def generate_pdf(filename_long, open_files = False):

    path = get_path(filename_long)[0]
    filename = get_path(filename_long)[1]

    current = os.getcwd()
    temp = tempfile.mkdtemp()
    os.chdir(temp)

    if path != '':
        os.chdir(path)

    cmd = ['pdflatex', '-interaction', '=nonstopmode', filename+'.tex']
    return_code = execute_os(cmd)

    # os.unlink(filename+'.aux')
    # os.unlink(filename+'.log')

    if not return_code[0] == 0:
        try:
            os.unlink(filename+'.pdf')
        except:
            showinfo(title='Error', message='Error ' + str(return_code[0]) + ' executing command ' +
                                            ' '.join(cmd) + '. PDF file was not generated. ')
            # exit()
        # raise ValueError('Error {} executing command: {}'.format(return_code, ' '.join(cmd)))
    else:
        if open_files:
            os.startfile(filename+'.pdf')

    for i in range(0, len(path.split('/'))):
        os.chdir('../')
