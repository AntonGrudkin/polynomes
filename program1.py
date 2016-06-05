__author__ = 'Антон'
import re
match = re.match('(.*)@(.*)[.](.*)', "antongrudkin8@gmail.com")
print(match.group(2))
match2 = re.match('digraph[ \t]*[{][ \t]*([0-9]*)[ \t]*->[ \t]*([0-9]*)[ \t]*[}]')
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
col0 = []
for i in range(3):
    col0.append(M[i][0] + M[i][1] + M[i][2])
col2 = [M[0][i] + M[1][i] + M[2][i] for i in [0,1,2]]
G = (sum(row) for row in M)
V = 0
for i in range(3):
    for j in range(3):
        V += M[i][j]
print(str(V))
dic = {i : sum(M[i]) for i in range(3)}
if 2 != 1: print('yes')
s = ''

print(': ', s)
#print(dic)
#print(next(G))
#print(next(G))
#print(next(G))
#col1 = [row[1] for row in M] #list generator
#col01 =
#print(col0)
#print(col2)
D = {'a' : 1, 'c' : 3, 'b' : 2}
#print(D['b'])
k = list(D.keys())
k.sort()
#for key in k:
 #   print(key, '=>', D[key])]
f = open('result.txt', 'w')

#for key in sorted(D):
 #   f.write(str(key))
  #  f.write('=>')
  #  f.write(str(D[key]))
   # f.write('\n')
#f.close()
#r = open('result.txt', 'r')
#print('File ', r.name, ' has been opened...')
#text = r.read()
#print('There is a text in file:')
#print(text)

#print('Begin...')
#f.write(str(2 ** 1000))
#print('Done!')
#f.close()

map(sum(row), M)
M.insert(2, 3)
print(M)

