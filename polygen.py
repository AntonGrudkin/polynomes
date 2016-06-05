__author__ = 'Anton Grudkin'

from random import randrange
from polynome import *

enumi_beg = "\\begin{enumerate}\n"
enumi_end = "\\end{enumerate}\n"
item_beg = "\\item $"
item_end = "$;\n"


def genpoly(sum_count=10, deg=5, cof=10, min_count=1):
    """Generation of simple polynome with sum_count summands, maximal degree of variate of deg, radius of
    coefficients of cof, and minimal count of summands of min_count"""

    p = Polynome([0], '')
    d_prev = -1
    while p.length < min_count:
        p.reset()
        for j in range(sum_count):
            d = randrange(deg)
            c = randrange(-cof, cof)
            while d == d_prev and c != 0:
                d = randrange(deg)
                c = randrange(-cof, cof)
            d_prev = d
            p.plus(c, d)
    return p


def polygen(count=10, sum_count=10, deg=5, cof=10):
    """Generation of list of count polynomes"""

    s = enumi_beg
    ans = enumi_beg

    for i in range(count):
        s += item_beg
        ans += item_beg
        p = genpoly(sum_count, deg, cof)
        ans += p.print_out()
        s += p.rep + item_end
        ans += item_end
    s += enumi_end
    ans += enumi_end
    return s, ans


def polymult(count=10, mult_sum_count=3, mult_count=2, sum_count=2, deg=3, cof=10):

    s = enumi_beg
    ans = enumi_beg
    result = Polynome([0], '')

    for i in range(count):
        s += item_beg
        ans += item_beg
        result.reset()
        mult = Polynome([1], '')
        for j in range(mult_sum_count):
            mult.reset()
            mult.plus(1, 0)
            chance = mult_count # int(randrange(mult_count*100)/100) + 1
            for k in range(chance):
                if k > 0:
                    p = genpoly(sum_count, deg, cof, 2)
                else:
                    p = genpoly(sum_count, deg, cof)
                if p.length > 1:
                    if k == 0 and j != 0:
                        s += " + "
                    if chance > 1:
                        s += "(" + p.rep + ")"
                    else:
                        s += p.rep
                else:
                    if k == 0 and j != 0 and p.rep[0] != "-":
                        s += " + "
                    s += p.rep
                mult.mult(p)
            result.plus_pol(mult)
        ans += result.print_out()
        s += item_end
        ans += item_end

    s += enumi_end
    ans += enumi_end

    return s, ans