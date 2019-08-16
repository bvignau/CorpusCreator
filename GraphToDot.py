def NodeToDot(node,file):
    line=node['name']+"      [fixedsize=True,fontsize="+str(node['fontsize'])+", height="+str(node['size'])+", width="+str(node['size'])+"];\n"
    file.write(line)


def EdgdeToDot(edge,file):
    line=edge[0]+" -> "+edge[1]+";\n"
    file.write(line)

def GraphToDot(graph,file,nodes,edges):
    with open(file,'w') as output:
        line="digraph \""+graph['name']+"\"{ graph [fontsize=80, nodesep=1.5, size=\"100,100\"];\n"
        output.write(line)
        for n in nodes : 
            NodeToDot(n,output)
        for e in edges :
            EdgdeToDot(e,output)
        output.write("}")
