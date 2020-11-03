# Graph traversal




def view_adjacencyMatrix(mat):
    print("Adjacency Matrix: ")
    for i in mat:
        print(i)


def graph(mat):
    vertices = []
    edges = []
    weights = {}
    for i in range(len(mat)):
        vertices.append(mat[0][i])
        for j in range(i, len(mat)):
            if type(mat[j][i]) == int:
                if mat[j][i] > 0:
                    edges.append((mat[0][i],mat[0][j]))
                    weights[(mat[0][i],mat[0][j])] = mat[j][i]
                
    print("Vertices: ", end = "")
    for v in vertices:
        print(v, ' ', end = "")
        
    print("\nEdges: ", end = "")
    for e in edges:
        print(e, ' ' , end = "")

    print("\nWeights: ")
    for i in weights:
        print(i, weights[i])
    
    return vertices, edges
    
        


def main():
    adjMat = [[' ','A','B','C','D','E'],['A',0,3,4,5,0],['B',3,0,0,0,7],['C',4,0,0,3,0],['D',5,0,3,0,2],['E',0,7,0,2,0]]
    view_adjacencyMatrix(adjMat)
    graph(adjMat)

main()
