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

for row in fileRows[1:len(fileRows)-3]: #skip first row and two last rows
    rFrom, rTo, rHeight = map(int, row.split(' '))
    graph[rFrom].append([rTo, rHeight])

print(graph)
