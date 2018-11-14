import sys

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
    graph[rFrom].append([rTo, rHeight, False])
    graph[rTo].append([rFrom, rHeight, False])

print(graph)
print(str(graph).replace(']],', ']]\n'))

pruneDeadEnds(graph, targetCity)
