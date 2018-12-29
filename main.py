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

#build graph object that can be parsed for minimum spanning tree
graph = []
for row in fileRows[1:roadCount+1]:
    rFrom, rTo, rHeight = map(int, row.split(' '))
    graph.append([rHeight, rFrom, rTo])

graph.sort(key=lambda x: x[0], reverse=True)

#
cities = []
for i in range(cityCount):
    cities.append([i+1])

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
    groupA += cities.pop(groupBindex)
    edges.append(edge)

#rebuild graph with spanning tree and create an empty height list
graph = {}
highests = []
for i in range(cityCount):
    graph[i+1] = []
    highests.append(0)
for edge in edges:
    graph[edge[1]].append([edge[0], edge[2]])
    graph[edge[2]].append([edge[0], edge[1]])


path = [1]
currentNode = 1
previousNode = 0
highest = 0

#build path
while targetCity not in path:
    if len(graph[currentNode]) > 0:
        step = graph[currentNode].pop(-1)
        if step[1] == previousNode:
            continue
        path.append(step[1])
        if step[0] > highest:
            highest = step[0]
        previousNode = currentNode
        currentNode = path[-1]
        highests[currentNode-1] = highest

    else:
        path.pop(-1)
        currentNode = path[-1]
        highest = highests[currentNode-1]


print(path, highest)
