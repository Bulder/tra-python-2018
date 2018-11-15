import sys
import copy
import time

#prune graph of nodes with only one route
def pruneDeadEnds(graph, target):
    for key in graph:
        if len(graph[key]) < 2 and key != target:
            #remove paths to the node too

            del graph[key]
            print("key %d removed as dead end" % key)


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

print(graph)
#print(str(graph).replace(']],', ']]\n'))

absolutePath = [1]
path = [[1], 0]
previousPath = [-1]
availableSteps = []
previousNode = None
currentNode = 1
backtrack = []

while currentNode != targetCity:
    shortestStep = None

    nextSteps = graph[currentNode].copy()

    #remove new steps going into dead ends or visited nodes
    for step in nextSteps:
        if len(graph[step[0]]) <= 1 or step[0] in path[0] or step[0] == previousNode:
            nextSteps.remove(step)

    #if one of the next steps is shorter or equal to the current highest
    shortestStep = min(nextSteps, key=lambda x: x[1])
    if shortestStep[0] == previousNode: #or shortestStep[0] == previousPath[-1]
        print(nextSteps)
        nextSteps.remove(shortestStep)
        shortestStep = min(nextSteps, key=lambda x: x[1])

    for step in nextSteps:
        if step in availableSteps:
            continue
        availableSteps += nextSteps


    if shortestStep[1] <= path[1]:
        backtrack = []
        availableSteps.remove(shortestStep)
        path[0].append(shortestStep[0])
        print("hop %d" % shortestStep[0])
    else:
        #pick the second best
        shortestStep = availableSteps.pop(availableSteps.index(min(availableSteps, key=lambda x: x[1])))
        print(previousNode, currentNode, shortestStep)
        currentNode = shortestStep[0]
        previousPath = path[0]
        path[0] = path[0][:path[0].index(shortestStep[2])+1]
        path[0].append(shortestStep[0])
        path[1] = shortestStep[1]
        print("hop back to %d then hop to %d" % (shortestStep[2], shortestStep[0]))

    previousNode = currentNode
    currentNode = shortestStep[0]
    absolutePath.append(currentNode)
    print(path[0])
    print(absolutePath, "\n")
    time.sleep(0.5)
print(path)
