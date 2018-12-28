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
graph = []

cities = []

for i in range(cityCount):
    cities.append([i+1])


for row in fileRows[1:roadCount+1]:
    rFrom, rTo, rHeight = map(int, row.split(' '))
    graph.append([rHeight, rFrom, rTo])

graph.sort(key=lambda x: x[0], reverse=True)

print(graph)

#build minimum spanning tree
edges = []
while len(edges) < cityCount-1:
    edge = graph.pop()
    groupA, groupB = [], []
    groupAindex, groupBindex = -1, -1
    for index, group in enumerate(cities):
        if edge[1] in group:
            groupAindex = index
            groupA = group
        if edge[2] in group:
            groupBindex = index
            groupB = group
    if groupAindex == groupBindex:
        continue
    print(groupAindex, groupBindex)
    groupA += cities.pop(groupBindex)
    print(groupA)

    print(cities)
    edges.append(edge)

print(edges, cities)
