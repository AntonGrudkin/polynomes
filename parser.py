__author__ = 'Anton'

import re

# noinspection PyBroadException
try:
    inputFile = open('input.txt', 'r')
except:
    print('File "input.txt" does not exist...')
    inputFile = open('input.txt', 'w')
    print('File "input.txt" has been successfully created...')

output = open('output.txt', 'w')

s = None
border = '-' * 25

print('Reading text from input file...\n' + border)
# noinspection PyBroadException
try:
    s = inputFile.read()
    print(s)
except:
    print('File has not been successfully reade...')
print(border)

s = s.lower()
#s = s.replace(" ", '')
s = s.replace("\t", ' ')
s = s.replace("\n", ' ')
print(s)
print(s.split()[1:-1])
aux = s.split()[1:-1]
flag = True


#while s.find('  ') > -1:
 #   s = s.replace('  ', ' ')
#print(s)
#s = s.replace(" ", ' ')
#s = s.replace("\t", ' ')
#s = s.replace("\n", ' ')

cont = s.split()
check_flag = True

if len(cont) < 2:
    print('Input file does not informative...')
    check_flag = False
elif cont[0] != 'digraph{':
    print('Error1: "digraph{" was not found...')
    check_flag = False
elif cont[len(cont) - 1] != '}':
    print('Error2: "}" was not found...')
    check_flag = False

if check_flag:
    cont.pop(0)
    cont.pop(len(cont) - 1)

nodes_dict = {}
for i in range(len(cont)):
    match = re.match('([0-9]*)->([0-9]*)', cont[i])
    if match.group(1) in nodes_dict.keys():
        nodes_dict[match.group(1)].append(match.group(2))
    else:
        nodes_dict[match.group(1)] = [match.group(2)]
    if match.group(2) not in nodes_dict.keys():
        nodes_dict[match.group(2)] = []
    cont[i] = cont[i].replace(match.group(1) + '->' + match.group(2), '')
    # noinspection PyRedeclaration
    aux = match.group(2)
    while len(cont[i]) > 0:
        match = re.match('->([0-9]*)', cont[i])
        nodes_dict[aux].append(match.group(1))
        if match.group(1) not in nodes_dict.keys():
            nodes_dict[match.group(1)] = []
        aux = match.group(1)
        cont[i] = cont[i].replace('->' + match.group(1), '')

#print('Edge from node', match.group(1), 'to node', match.group(2), 'was found...')

nodes_set = set(nodes_dict.keys())
# noinspection PyRedeclaration
aux = {int(s): s for s in nodes_set}
aux = [aux[i] for i in sorted(aux.keys())]
nodes_set = aux[:]
nodes_list = list(nodes_set)

nodes = []
aux = [0]*len(nodes_set)
for n in nodes_set:
    for i in range(len(nodes_dict[n])):
        aux[list(nodes_set).index((nodes_dict[n][i]))] = 1
    nodes.append(aux[:])
    aux = [0]*len(nodes_set)

# noinspection PyRedeclaration
aux = '   '
for i in range(len(nodes)-1):
    aux += nodes_list[i] + '  '
aux += nodes_list[len(nodes_list)-1]
print(aux)
for n in range(len(nodes)):
    print(nodes_list[n], nodes[n])
#input()
