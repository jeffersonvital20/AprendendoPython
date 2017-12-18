import numpy as np
from collections import deque
from sortedcontainers import SortedSet

class buscas:
    objetivo = []
    def __init__(self):
        print("criou")
    def profundidade(self,inicio,objtivo):
        estados = []

        if estados.__contains__(inicio) or len(objtivo) == 0:
            return None

        fia =[]
        fia.append(inicio,inicio)

        while len(fia) != 0:
            n =fia.pop()


'''class testes:
    def DFS_Stack(self, exploreObj=None):
        self.setVertexListAsUnexplored()

        self.__time = 0

        for vertex in self.__V:
            if (not vertex.wasExplored()):
                self.__DFS_VISIT_STACK(vertex, exploreObj)

        return exploreObj

    def BFS(self, source=0, exploreObj=None):
        self.setVertexListAsUnexplored()

        if ((exploreObj is not None) and (source != exploreObj.getInitialVertexIndex())):
            source = exploreObj.getInitialVertexIndex()

        self[source].d = 0
        self[source].explore(exploreObj)

        queue = deque([self[source]])

        while len(queue) != 0:
            v = queue.popleft()

            for adjacentVertex in v.getAdjacentVertexSet():
                if (not adjacentVertex.wasExplored()):
                    adjacentVertex.predecessor = v
                    adjacentVertex.d = v.d + 1
                    adjacentVertex.explore(exploreObj)

                    queue.append(adjacentVertex)

        return exploreObj
'''