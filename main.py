import sys
import copy
import time
import math

#read file
with open(sys.argv[1]) as nodeFile:
    fileContent = nodeFile.read()

#split file by row
fileRows = fileContent.split('\n')
#they're surprise tools that will help us later
cityCount, roadCount = map(int, fileRows[0].split(' '))
targetCity = int(fileRows[len(fileRows)-2]) #the file ends with an empty row so skip past that
#build graph object
graph = {}
for i in range(cityCount):
    graph[i+1] = []

for row in fileRows[1:roadCount+1]:
    rFrom, rTo, rHeight = map(int, row.split(' '))
    #add all roads leading out of nodes and setting them to untraversed
    graph[rFrom].append([rTo, rHeight, rFrom])
    graph[rTo].append([rFrom, rHeight, rTo])

#print(graph)
#print(str(graph).replace(']],', ']]\n'))

lowest = [math.inf] * cityCount
previous = [None] * cityCount
unvisited = graph.copy()

index = 1

while len(unvisited) != 0:
    node = unvisited.pop(index)
    print(index)
    for path in node:
        if path[1] < lowest[path[0]-1]:
            lowest[path[0]-1] = path[1]
            previous[index-1] = path[0]

    index = None
    minimum = math.inf
    i = 0
    while i < cityCount:
        if i+1 in unvisited and lowest[i] < minimum:
            index = i+1
        i += 1
traceBackCursor = targetCity-1
path = []
print(unvisited)
print(previous)
print(lowest)


print(path)
