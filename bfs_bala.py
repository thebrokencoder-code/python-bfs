graph_or_tree = {
"A" :["B","C","D"],
"B" :["D","E"],
"C" :["B","F"],
"D": [],
"E" : ["F"],
"F" :[],
"G" :["B","A","L","A","J","I"]
}

print(graph_or_tree["G"])
waiting_queue =[]
bfs_level={}
visited_nodes=[]
parent ={}
bfs_path=[]

for node in graph_or_tree.keys():
    bfs_level[node] = -1
    parent[node]= None

root = "A"
visited_nodes.append(root)
bfs_level[root]=0
waiting_queue.append(root)

while len(waiting_queue )>0:
    node = waiting_queue.pop(0)
    bfs_path.append(node)

    for n in graph_or_tree[node]:
        if n not in visited_nodes:
            visited_nodes.append(n)
            parent[n] = node
            bfs_level[n] =bfs_level[node]+1
            waiting_queue.append(n)
print("=============Breadth First Search Algorithm===========")
print("traversal using Breadth First Search =\t",*bfs_path,sep=" -> ")
print("levels to verify the traversal",bfs_level)
    
