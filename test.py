from polygen import *

head_file = open("head.tex", 'r')
ground_file = open("ground.tex", 'r')

problems = open("problems.tex", 'w')
answers = open("answers.tex", 'w')

head = head_file.read()
problems.write(head)
answers.write(head)

t = polymult(5, 1, 4, 2, 3, 1)

problems.write(t[0])
answers.write(t[1])

ground = ground_file.read()
problems.write(ground)
answers.write(ground)

problems.close()
answers.close()

#p = genpoly()
#print(p.print_out())
#for i in range(5):
 #   p.dev()
  #  print(p.print_out())

p1 = Polynome([0], '')
p1.plus(-1, 1)
p1.plus(2, 2)
p1.plus(1, 0)
print(p1.rep)

p2 = Polynome([0], '')
p2.plus(1, 1)
p2.plus(-1, 2)
p2.plus(-2, 0)
print(p2.rep)

p1.mult(p2)
print(p1.print_out())

#p2 = polymone([0], '')
#p2.plus()




