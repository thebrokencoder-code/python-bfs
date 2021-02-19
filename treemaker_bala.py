
class graphCreate(dict):
    def __init__(self):
        self = dict()
    def add(self,key,value):
        self[key] = value
while True:
    ans = int(input("enter 1 to create a graph =\t"))
    if ans == 1:
        graph = graphCreate()
        print(graph)
    else:
        print("please enter a valid option")
    ans = int(input("enter 1 to add a node \t0 to end graph=\t"))
    if ans == 1:
        while True:
            key = str(input("enter the parent = \t"))
            value = list(input("enter the child node =\t"))
            if key and value:
                graph.add(key,value)
                print(graph)
                ans=int(input("enter \n1. to add a new child node to same root \t 0 to end graph \t 2. to add a new parent node = \t"))
                if ans == 1:
                    value = list(input("enter the child node =\t"))
                    if value:
                        graph[key] = graph.get(key,[]) + value
                        print("Updated graph = ", graph)
                elif ans == 2:
                    continue
                elif ans == 0:
                    break
    elif ans == 0:
        break
