import sys
import bisect

#prune graph of nodes with only one route
def pruneDeadEnds(graph):
    for key in graph:
        print(key)
        for path in graph[key]:
            if len(graph[path[0]]) < 2:
                print(key, graph[path[0]])


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

pruneDeadEnds(graph)



#Beginning of solver
