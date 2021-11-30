# Online Python compiler (interpreter) to run Python online.
#Fatmata Alice Koroma
#Variable declaration
#Initilize an integer that is larger than the starting node 6 and assign it to the float(INF) as it present infinity
INF = 50

# Initailize a vertices variable to hold the number of vertex in the graph
Vertices = 7

# Initialize a variable that holds the weight of graph in a form of an adjacency matrix, where the first indeices contain the individual vertices on the graph. With every element represented as a list
Graph = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 22, 0, 0, 18],
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 8, 24, 0, 0]]

#Declare a list that has 7 elements indicating the number of vertices 
selected = [0, 0, 0, 0, 0, 0, 0]

# Initializing values that holds the number of edges left in the graph
no_edge = 0
selected[5] = True


# Print the spanning tree 
print("Edge : Weight\n")
while (no_edge < Vertices - 1):
   
    minimum = INF
    x = 0
    y = 0
    for i in range(Vertices):
        if selected[i]:
            for j in range(Vertices):
                if ((not selected[j]) and Graph[i][j]):  
                    if minimum > Graph[i][j]:
                        minimum = Graph[i][j]
                        x = i
                        y = j
    # print sequence of movement and the weight of the edge
    print(str(x+1) + "->" + str(y+1) + ":" + str(Graph[x][y]))
     #update select value with the next vertex
    selected[y] = True
     #Increment number of edges by 1
    no_edge += 1