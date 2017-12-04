__author__ = 'Anton Grudkin'


class Polynome:
    def __init__(self, list, rep):
        self.list = list
        self.rep = rep

    def plus(self, a, d):
        try:
            self.list[d] += a
        except:
            self.list = self.list + [0]*(d - len(self.list) + 1)
            self.list[d] += a
        aa = a
        if self.rep != '' and aa != 0:
            if aa < 0:
                aa = abs(aa)
                self.rep += ' - '
            else:
                self.rep += ' + '
        else:
            if aa < 0:
                aa = abs(aa)
                self.rep += '-'
        if aa != 0 and (aa != 1 or d == 0):
            self.rep += str(aa)
        if d == 1 and aa != 0:
            self.rep += 'x'
        elif d > 1 and aa != 0:
            self.rep += 'x^{' + str(d) + '}'

    # def max_deg(self):

    def print_out(self):
        # return str(self.list[d])
        s = ''
        for i in range(len(self.list)):
            if self.list[i] != 0:
                if self.list[i] > 0 and s != '':
                    s += ' + '
                if self.list[i] != 1 and self.list[i] != -1 or i == 0:
                    s += str(self.list[i])
                elif i == -1:
                    s += ' - '
                if i > 0:
                    s += 'x'
                if i > 1:
                    s += '^{' + str(i) + '}'
        return s

    def reset(self):
        self.rep = ''
        self.list = [0]

    def mult(self, pol):
        l = self.list
        self.list = [0]*(len(self.list) + len(pol.list) - 1)
        for i in range(len(l)):
            for j in range(len(pol.list)):
                self.list[i+j] += l[i]*pol.list[j]
        self.rep = self.print_out()

    def plus_pol(self, pol):
        for i in range(len(pol.list)):
            if pol.list[i] != 0:
                self.plus(pol.list[i],i)

    @property
    def length(self):
        result = 0
        for i in range(len(self.list)):
            if self.list[i] != 0:
                result += 1
        return result

    def dev(self, deg=1):
        for j in range(deg):
            for i in range(len(self.list)):
                if i != 0:
                    self.list[i-1] = self.list[i]*i
            self.list = self.list[:-1]
