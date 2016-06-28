from polygen import *
from os_module import *

__author__ = 'Anton Grudkin'

head_file = open("tex/head.tex", 'r')
ground_file = open("tex/ground.tex", 'r')

answers_filename = check_output_filename('output/answers')
problems_filename = check_output_filename('output/problems')

answers = open(answers_filename + '.tex', 'w')
problems = open(problems_filename + '.tex', 'w')


def head_writer():
    head = head_file.read()
    problems.write(head)
    answers.write(head)


def ground_writer():
    ground = ground_file.read()
    problems.write(ground)
    answers.write(ground)


def polygen_writer(title=None, count=10, sum_count=5, deg=4, cof=20):
    t = polygen(count, sum_count, deg, cof)
    if title is not None:
        problems.write('\section{' + title + '}')
        answers.write('\section{' + title + '}')
    problems.write(t[0])
    answers.write(t[1])



