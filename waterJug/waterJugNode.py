'''
class: water jug
objective: defining methods for different actions possible with water jug
'''
import time
class waterJug:
    def __init__(self, x, y, xCapacity, yCapacity):
        self.x = x
        self.y = y
        self.xCapacity = xCapacity
        self.yCapacity = yCapacity
    
    # completely fill Jug A
    def fillA(self):
        if (self.x < self.xCapacity):
            childNode = waterJug(self.xCapacity, self.y, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None
        
    # completely fill Jug B
    def fillB(self):
        if (self.y < self.yCapacity):
            childNode = waterJug(self.x, self.yCapacity, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None

    # completely empty jug A
    def emptyA(self):
        if(self.x > 0):
            childNode = waterJug(0, self.y, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None

    # completely empty Jug B
    def emptyB(self):
        if(self.y > 0):
            childNode = waterJug(self.x, 0, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None

    # transfer Jug A to Jug B according to capacity
    def AtoB(self):
        if (0 < self.x <= self.xCapacity) and (0 <= self.y < self.yCapacity):
            BCapacity = self.yCapacity - self.y
            amount = self.x if (self.x <= BCapacity) else BCapacity
            x2 = self.x - amount
            y2 = self.y + amount
            childNode = waterJug(x2, y2, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None

    # transfer Jug B to Jug A according to capacity
    def BtoA(self):
        if (0 <= self.x < self.xCapacity) and (0 < self.y <= self.yCapacity):
            ACapacity = self.xCapacity - self.x
            amount = self.y if (self.y <= ACapacity) else ACapacity
            x2 = self.x + amount
            y2 = self.y - amount
            childNode = waterJug(x2, y2, self.xCapacity, self.yCapacity)
            return childNode
        else:
            return None


# import waterJugNode

# '''
# class: graph
# objective: contains methods to create graph and perform dfs to find goal state
# '''           
# class graph:
#     visited = []
#     path = []
#     finalPath = []
#     count = 0
#     def __init__(self, xCapacity, yCapacity, xGoal, yGoal):
#         self.xCap = xCapacity
#         self.yCap = yCapacity
#         self.xGoal = xGoal
#         self.yGoal = yGoal
#         self.graphDict = {}

#         # initialising visited matrix with false
#         for i in range(self.xCap+1):
#             temp=[]
#             for j in range(self.yCap+1):
#                 temp.append(False)
#             self.visited.append(temp)

#     ''' 
#     Objective: To check if the state of a node is present in one of the paths to goal state
#     '''
#     def inFinalPath(self, state):
#         for path in self.finalPath:
#             if state in path:
#                 i = path.index(state)
#                 newPath = self.path + path[i:]
#                 return path[i:]
#         return False

#     ''' 
#     Objective: Driver function for dfs create graph method
#     '''
#     def createGraphUtil_BFS(self):
#         root = waterJug(0, 0, self.xCap, self.yCap)
#         start = time.time()
#         self.createGraphBFS(root)
#         stop = time.time()
#         print(f"Time in BFS: {(stop-start)*1000} ms" )
#         print("Total ways:", self.count)

#     def createGraphUtil_DFS(self):
#         dfsroot = waterJug(0, 0, self.xCap, self.yCap)
#         start = time.time()
#         self.createGraphDFS(dfsroot)
#         stop = time.time()
#         print(f"Time in DFS: {(stop-start)*1000} ms" )
#         print("Total ways:", self.count)
        

#     ''' 
#     Objective: Checking necessary conditions to call recursive functions
#     '''
#     def checkNode(self, node):
#         if not node:
#             return
        
#         state = (node.x, node.y)
#         if self.visited[node.x][node.y] == False:
#             # recursive call
#             self.createGraphDFS(node)
#             # remove the node from path while backtracking
#             self.path.pop()

#         # if the state has already visited but it leads to goal state
#         elif self.inFinalPath(state) and state not in self.path:
#             self.count += 1
#             print(self.path + self.inFinalPath(state))
 
#     ''' 
#     Objective: Graph creation using DFS 
#     '''
#     def createGraphDFS(self, node):
#         self.path.append((node.x, node.y))
        
#         if (node.x == self.xGoal) and (node.y == self.yGoal):
#             self.count += 1
#             print(self.path)
#             self.finalPath.append(list(self.path))
#             return

#         self.visited[node.x][node.y] = True
        
#         fillA = node.fillA()
#         self.checkNode(fillA)
        
#         fillB = node.fillB()
#         self.checkNode(fillB)
        
#         emptyA = node.emptyA()
#         self.checkNode(emptyA)
        
#         emptyB = node.emptyB()
#         self.checkNode(emptyB)
        
#         AtoB = node.AtoB()
#         self.checkNode(AtoB)
        
#         BtoA = node.BtoA()
#         self.checkNode(BtoA)

#         self.graphDict[node] = [fillA, fillB, emptyA, emptyB, AtoB, BtoA]

#     def createGraphBFS(self, node):
#         self.path.append((node.x, node.y))
        
#         if (node.x == self.xGoal) and (node.y == self.yGoal):
#             self.count += 1
#             print(self.path)
#             self.finalPath.append(list(self.path))
#             return

#         self.visited[node.x][node.y] = True

#         fillA = node.fillA()
#         fillB = node.fillB()
#         emptyA = node.emptyA()
#         emptyB = node.emptyB()
#         AtoB = node.AtoB()
#         BtoA = node.BtoA()
        
#         self.graphDict[node] = [fillA, fillB, emptyA, emptyB, AtoB, BtoA]

#         for state in self.graphDict[node]:
#             self.checkNode(state)



        
#     def displayGraph(self):
#         print("Graph:")
#         for key, value in self.graphDict.items():
#             if key!=None:
#                 print(key.x, key.y, end=" -> ")
#             for child in value:
#                 if child != None:
#                     print(child.x, child.y, end=" , ")
#             print()

    
# def main():
#     xCap = 3
#     yCap = 4
#     xGoal = 0
#     yGoal = 2
    
#     # print("Total ways:", ob.count)
    
#     ob2 = graph(xCap, yCap, xGoal, yGoal)
#     graph.createGraphUtil_DFS(ob2)
#     # print("Total ways:", ob2.count)

#     ob = graph(xCap, yCap, xGoal, yGoal)
#     graph.createGraphUtil_BFS(ob)
    
    

# if __name__ == "__main__":
#     main()





    
