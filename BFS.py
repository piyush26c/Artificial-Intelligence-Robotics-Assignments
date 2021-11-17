# -*- coding: utf-8 -*-
"""
Authors: Piyush Rajendra Chaudhari

Topic  : Best First Search Algorithm (Best solution but not always optimal)
"""
import sys
INT_MAX = sys.maxsize

class Node:
    def __init__(self, f = 0, h = 0, name = 0):
        self.f = f
        self.h = h
        self.name = name
        
    def setNeighbours(self, neighbours = {}):
        self.neighbours = neighbours


class BestFirstSearchAlgorithm(Node):
    def __init__(self):
        self.adjacencyMatrix = []
        self.nameIndexMapping = {}
        self.listOfNodes = []
        self.openList = []
        self.closeList = []
        self.startNode = None
        self.goalNode = None
        self.numberOfNodes = None

    def getInput(self):
        self.numberOfNodes = int(input('Enter number of nodes in graph : '))
        self.adjacencyMatrix = [[-1 for i in range(self.numberOfNodes)] for j in range(self.numberOfNodes)]
        for i in range(self.numberOfNodes):
            self.nameOfNode = str(input('Enter the name of node : '))
            self.heuristicValue = int(input('Enter the heuristic value of node ' + self.nameOfNode + ' : '))
            self.listOfNodes.append(Node(name=i, h=self.heuristicValue))
            self.nameIndexMapping[self.nameOfNode] = i  # a : 1

        while (True):
            inputNodes = str(input('Input in for [fromNode toNode edgeCost] (else input # to stop) : '))

            if (inputNodes == '#'):
                break
            inputNodes = inputNodes.split(' ')
            fromNode = self.nameIndexMapping[inputNodes[0]]
            toNode = self.nameIndexMapping[inputNodes[1]]
            edgeCost = int(inputNodes[2])
            self.adjacencyMatrix[fromNode][toNode] = edgeCost
            print("Insertion successfull!!!")

        self.startNode = self.listOfNodes[self.nameIndexMapping[str(input('Input start node name : '))]]
        self.goalNode = self.listOfNodes[self.nameIndexMapping[str(input('Input goal node name : '))]]

        for x in range(self.numberOfNodes):
            tempL = []
            for y in range(self.numberOfNodes):
                if (self.adjacencyMatrix[x][y] != -1):
                    tempL.append(self.listOfNodes[y])
            self.listOfNodes[x].setNeighbours(tempL)

    def bestFirstSearchAlgorithm(self):

        self.startNode.f = self.startNode.h
        self.openList.append(self.startNode)
        currentNode_ = self.startNode

        while len(self.openList) != 0:
            if currentNode_ == self.goalNode:
                self.closeList.append(currentNode_)
                return 1
            self.openList.remove(currentNode_)
            self.closeList.append(currentNode_)

            for neighbourNode in currentNode_.neighbours:
                if self.adjacencyMatrix[currentNode_.name][neighbourNode.name] != -1:
                    if neighbourNode in self.closeList:
                        continue
                    if neighbourNode not in self.openList:
                        self.openList.append(neighbourNode)
                    
                    neighbourNode.f = neighbourNode.h

            currentNode_ = self.findNodeWithLowestFScore(self.openList, currentNode_)

        return -1

    def findNodeWithLowestFScore(self, openList_, currentNode_):
        fScore = INT_MAX
        node = None

        for eachNode in openList_:
            if eachNode.f < fScore and self.adjacencyMatrix[currentNode_.name][eachNode.name] != -1:
                fScore = eachNode.f
                node = eachNode
        return node

    def getKeyFromNameIndexMappingDictionary(self, value):
        for k, v in self.nameIndexMapping.items():
            if v == value:
                return k

    def printOutput(self):
        print("Path : ", end=' ')
        for x in range(0, len(self.closeList) - 1):
            print(self.getKeyFromNameIndexMappingDictionary(int(self.closeList[x].name)), '--> ', end='')
        print(self.getKeyFromNameIndexMappingDictionary(int(self.closeList[len(self.closeList) - 1].name)), end='')
        #print("\nCost : " + str(self.goalNode.g))



if __name__ == "__main__":
    obj = BestFirstSearchAlgorithm()
    obj.getInput()
    successOfExecution = obj.bestFirstSearchAlgorithm()
    obj.printOutput()



"""
Input - 1 : 
Enter number of nodes in graph : 10
Enter the name of node : a
Enter the heuristic value of node a : 12
Enter the name of node : b
Enter the heuristic value of node b : 4
Enter the name of node : c
Enter the heuristic value of node c : 7
Enter the name of node : d
Enter the heuristic value of node d : 3
Enter the name of node : e
Enter the heuristic value of node e : 8
Enter the name of node : f
Enter the heuristic value of node f : 2
Enter the name of node : h
Enter the heuristic value of node h : 4
Enter the name of node : i
Enter the heuristic value of node i : 9
Enter the name of node : s
Enter the heuristic value of node s : 13
Enter the name of node : g
Enter the heuristic value of node g : 0
Input in for [fromNode toNode edgeCost] (else input # to stop) : s a 3
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : s b 2
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : a c 4
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : a d 1
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : b e 3
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : b f 1
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : e h 5
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : f i 2
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : f g 3
Insertion successfull!!!
Input in for [fromNode toNode edgeCost] (else input # to stop) : #
Input start node name : s
Input goal node name : g

Output - 1 : 
Path :  s --> b --> f --> g
Cost : 6
"""