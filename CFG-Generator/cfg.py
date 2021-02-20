from staticfg import CFGBuilder
import re
count = 0
cfg = CFGBuilder().build_from_file('control flow graph', 'qsort.py')
cfg.build_visual('qsort', 'pdf')
f = open("qsort", "r")
f=f.read()
#find edges
freq = f.count("->")
calls = f.count("_calls") 
edges = freq - (calls/2 ) 
edges = int(edges)
print("Edges:",int(edges))
# node
with open("qsort") as file_in:
    lines = []
    for line in file_in:
        temps = line.replace("\t","").replace(' ',"")
        if (temps[0].isdigit()):
            temp = int(temps[0])
            lines.append(temp)
            # print(temps[0])
            if (temps[0].isdigit() and temps[1].isdigit()):
                temp = int(temps[0]+temps[1])
                lines.append(temp)
                # print(temp)
    lines = list(dict.fromkeys(lines))
    node = len(lines)
    print("Node: ",node)
print("V(G) = E - N + 2")
print("V(G) = "+ str(edges) + " - "+ str(node) +" + 2")
vg = int(edges)-node + 2
print("V(G) =", str(vg))

  
