import sys

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
solved = False
stack = []
currentPath = [1]
highest = 0
currentNode = 1
navigated = true
#traverse graph
while !solved:
    if !navigated:

    navigated = false
    stack.append(graph[currentNode]) #add current node's paths to stack
    for index, path in enumerate(stack[len(currentPath)-1]):
        #if the node the target points at only poits at the node we're leaving, or it's already been visited, we just don't for now
        if len(graph[path[0]]) == 1 or path[1] in currentPath:
            stack[len(currentPath)-1].pop(index)
        #TODO we need to figure out how to actually navigate the tree and double back if needed
        elif highest
