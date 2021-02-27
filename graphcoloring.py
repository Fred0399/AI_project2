
# path for input file
filepath = 'test1.txt'

# our arr of vertices
arrVertex = []

# graph edges (unmapped)
edges = []

# by default we have 0 color
colorCount = 0

# our graph, adjacency matrix
graphMatrix = []

# read vertices array from file
def readInput():
    global colorCount
    global arrVertex, edges, graphMatrix
    
    with open(filepath) as fp:
       line = fp.readline()
       while line:
           line = line.rstrip('\n')
           
           # make f = True, and f_find false
           if(len(line)>0 and '#' in line):
               line = fp.readline()
               continue
            
           # read the number of colors
           if(len(line)>0 and ('Colors = ' in line or 'colors = ' in line)):
               
               # get the number of colors
               
               colorCount = int(line.split(' = ')[1])
               
               line = fp.readline()
               continue
            
           splittedArr = line.split(',')
           
           if(len(splittedArr)==2):
               
               if(int(splittedArr[0]) not in arrVertex):
                   arrVertex.append(int(splittedArr[0]))
               
               if(int(splittedArr[1]) not in arrVertex):
                   arrVertex.append(int(splittedArr[1]))

           edges.append([int(splittedArr[0]),int(splittedArr[1])])
           
           
           line = fp.readline()
    
    # fill the default matrix with 0's
    graphMatrix = [[0 for i in range(len(arrVertex))] for j in range(len(arrVertex))]

    # map the edges to 0,1,2,3,4...
    for i in range(len(edges)):
        for vInd in range(len(arrVertex)):
            if(edges[i][0] == arrVertex[vInd]):
                edges[i][0] = vInd
                break
        
        for vInd in range(len(arrVertex)):
            if(edges[i][1] == arrVertex[vInd]):
                edges[i][1] = vInd
                break
                
    
    # build adjacency matrix from edge infos
    for path in edges:
        graphMatrix[path[0]][path[1]] = graphMatrix[path[1]][path[0]] = 1

# reading input and parsing to normalized data
readInput()

# minimum remaining values, picks the value with less possible options
def MRVheur(colors, v, c):
    global vertexCount, graphMatrix
    
    for i in range(vertexCount):
        # check if vertex is colored
        if graphMatrix[v][i] == 1 and colors[i] == c:
            return False
    return True
	
# A recursive utility function to solve coloring problem
def recursiveBackTrack(colors, colCount, v):
    global vertexCount
    # check if we reached at the end of tree
    if v == vertexCount:
        return True
    
    # search vertices of graph one by one and 
    for c in range(1, colCount + 1):
        # find minimal remaining domains of vertex
        if MRVheur(colors, v, c) == True:
            # append color to vertex 
            colors[v] = c
            # search recursively among vertices and get True or False
            # if possible to append color approve or not
            if recursiveBackTrack(colors, colCount, v + 1) == True:
                return True
            # if it is not possible to append
            # color then reset it
            colors[v] = 0

def backtracking(colCount):
    global vertexCount,colorsArr
    # start recursive function to search
    if recursiveBackTrack(colorsArr, colCount, 0) == None:
        print("Not possible to color graph with input data")
        return False
    
    for c in range(len(colorsArr)):
        print("Vertex: {0} Color: {1}".format(arrVertex[c],colorsArr[c]))
    


vertexCount = len(arrVertex)
colorsArr = [0] * vertexCount
# 
backtracking(colorCount)
