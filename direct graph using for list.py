graph = {
    'A': ['B'],
    'B': ['C', 'D', 'E'],
    'C': ['E', 'D'],
    'D': ['A', 'E'],
    'E': ['F'],
    'G': ['D']
}

for key,val in graph.items():
    print(key,'-->',val)