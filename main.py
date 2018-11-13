import sys
import bisect

#read file
with open(sys.argv[1]) as nodeFile:
    fileContent = nodeFile.read()

#split file by row
fileRows = fileContent.split('\n')
#they're surprise tools that will help us later
cityCount, roadCount = map(int, fileRows[0].split(' '))
targetCity = fileRows[len(fileRows)-2] #the file ends with an empty row so skip past that
#build graph object
graph = {}
for i in range(cityCount):
    graph[i+1] = []

for row in fileRows[1:roadCount+1]:
    rFrom, rTo, rHeight = map(int, row.split(' '))
    #add all roads leading out of nodes and setting them to untraversed
    graph[rFrom].append([rTo, rHeight, False])
    graph[rTo].append([rFrom, rHeight, False])

print(graph)
print(str(graph).replace(']],', ']]\n'))

#Beginning of solver
path = [1]
#index is city number -1, format should be [[unnavigated path], highest at time]
unfollowedPaths = [[] for _ in range(cityCount)]

depth = 0
currentNode = 1
highest = 0
lowestPotential = None
while True:
    nextSteps = graph[currentNode]
    nextNode = None
    unfollowedPaths[]
    for step in nextSteps:
        #if the next step is a dead end or if we've already been there we don't navigate
        if len(graph[step[0]]) == 1 or step[0] in path:
            print("No")
        #if the next step is lower than the highest then sure let's go for it
        elif path[1] < highest:
            nextNode = step[0]
            newPath = path
            newPath.append(nextNode)
        else:
            unfollowedPaths[currentNode-1].append([step, highest])
            if step[1] <
            lowestPotential = [currentNode, step]

    if nextNode == None:
        if depth > 0:
            depth = depth-1
            path.pop()


#bisect.insort_left
