class node:
    # direction: Right = 1, Left = 0
    def __init__(self, m, c, direction):
        self.m = m
        self.c = c
        self.direction = direction

'''
possible states of movement across the banks -> (0M,1C), (0M,2C), (1M,0C), (1M,1C), (2M,0C)
'''
possibleStates = [(0,1), (0,2), (1,0), (1,1), (2,0)]
visited = []
path = []

# generate child nodes as possible states of movement
def possibleState(leftParent, rightParent, parentBank, m, c):
        # have to go from left -> right
        if parentBank == 0:
            if leftParent.m >= m and leftParent.c >= c:  
                left = node(leftParent.m - m, leftParent.c - c, 0)
                right = node(rightParent.m + m, rightParent.c + c, 1)
            else: 
                left = right = None
        
        # have to go right -> left
        else:
            if rightParent.m >= m and rightParent.c >= c: 
                left = node(leftParent.m + m, leftParent.c + c, 0)
                right = node(rightParent.m - m, rightParent.c - c, 1)
            else: 
                left = right = None
        
        return left, right

# checks if a state is valid or not.
# for validity: cannibals should not outnumber missionaries on either bank
def isValid(left, right):
    if not left or not right:
        return False
    if (left.m > 0 and left.c > 0 and left.m < left.c) or (right.m > 0 and right.c > 0 and right.m < right.c):
        return False
    return True 
        

def display(left, right):
    print(left.m, left.c, "L", end="\t")
    print(right.m, right.c, "R")


def missionaryCannibals(left, right, parentbank, maxM, maxC):
    
    if left.m == 0 and left.c == 0 and right.m == maxM and right.c == maxC:
        print("**found**")
        for p in path:
            print(p)
        return

    visitedState = ((left.m, left.c, left.direction), (right.m, right.c, right.direction), parentbank)
    visited.append(visitedState)
    path.append(visitedState)

    for state in possibleStates:
        leftChild, rightChild = possibleState(left, right, parentbank, state[0], state[1])
        if isValid(leftChild, rightChild): 
            tempState = ((leftChild.m, leftChild.c, leftChild.direction), (rightChild.m, rightChild.c, rightChild.direction), not parentbank) 
            if tempState not in visited:
                missionaryCannibals(leftChild, rightChild, not parentbank, maxM, maxC)
                if path:
                    path.pop()
    pass

def main():
    maxM = 3
    maxC = 3
    starting_bank = 0
    
    left = node(maxM, maxC, 0)
    right = node(0, 0, 1)
    
    missionaryCannibals(left, right, 0, maxM, maxC)

if __name__ == "__main__":
    main()