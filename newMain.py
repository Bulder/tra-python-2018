import sys
import bisect

def getLowestKeys(set = {}, count):
    keys = set.keys
    sorted(keys)
    return keys[:count]

def isRoutable(start, target)

#read file
with open(sys.argv[1]) as nodeFile:
    fileContent = nodeFile.read()

#split file by row
fileRows = fileContent.split('\n')
#they're surprise tools that will help us later
cityCount, roadCount = map(int, fileRows[0].split(' '))
targetCity = fileRows[len(fileRows)-2] #the file ends with an empty row so skip past that
#build graph object
routes = {}

for row in fileRows[1:roadCount+1]:
    rFrom, rTo, rHeight = map(int, row.split(' '))
    #add all roads leading out of nodes and setting them to untraversed
    routes[rHeight] = [rFrom, rTo]

print(routes)
print(str(routes).replace('],', ']\n'))

searchDirection = False #false means shrink, true means expand
while true:
