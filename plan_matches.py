import sys
import math
import itertools
import collections 

input_file = "example_graph_3.txt"
part1 = []
part2 = []
k = 0

with open(input_file) as graph_input:
    for line in graph_input:
        nodes = [x for x in line.split()]
        #storing each match player in two lists
        part1[k] = nodes[0]
        part2[k] = nodes[1]
        k++

for i in range(k)
    #swap values, if for example a match is c,b this should turn into b,c
    if part2[k] < part1[k]:
        part1[k], part2[k] = part2[k], part1[k]

days = []
g = {}

for i in range(k)
    dict_keys= list(g.keys())
    length = len(dict_keys)
    days[k] = find_Matchday(g, length, part1[k], part2[k])
    
matchdays = {}
for i in range(k)
    tu = part1[k], part2[k]
    matchdays[tu] = [days[k]]
    
for i in range(k)
    print( ({0}, {1}) {2}.format('matchdays[k][0]', 'matchdays[k][1]', matchdays[k]))

def find_Matchday(dict, size, num1, num2)
    for i in range(size)
        if num1 not in dict[i] & num2 not in dict[i]:
            temp_list = []
            temp_list.append(dict[i])
            dict[i] = [temp_list, num1, num2]
            var = i
            break
        else:
            dict[size+1] = [num1, num2]
            var = size+1
            break
    return var
