import os
import bibtexparser
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import GraphToDot as Gtd


def autolabel(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width(), height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def GenRequest(request1,request2):
    requests=[]
    for r1 in request1:
        for r2 in request2:
            request=r1+" "+r2
            requests.append(request)
    return requests

def recupID(requests):
    ida={}
    for r in requests:
        file=r+".bib"
        with open(file) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            for ref in bib_database.entries:
                if ref['ID'] not in ida:
                    ida[ref['ID']]=[r]
                else :
                    ida[ref['ID']].append(r)
    print("nombre d'articles différents = "+str(len(ida)))
    return ida

def GenGraph(ida,requests):
    name="Relation articles - requetes"
    G={'name':name}
    nodes=[]
    edges=[]
    for r in requests:
        n={'name':r,'fontsize':12,'size':15}
        nodes.append(n)
    print(str(nodes))
    for i,v in ida.items():
        n={'name':i,'fontsize':8*len(v),'size':len(v)*4}
        nodes.append(n)
        for r in v:
            edges.append([i,r])
    Gtd.GraphToDot(G,"test.dot",nodes,edges)
    # nx.draw(G, pos=nx.circular_layout(G), with_labels=True, font_weight='bold',node_size =[500 * v for v in nodeSize])
    # nx.drawing.nx_pydot.write_dot(G,"test.dot")
    # plt.show()

def ShowBar(ida):
    labels=[]
    values=[]
    width=0.35
    fig, ax = plt.subplots()
    for i,v in ida.items():
        labels.append(i)
        values.append(len(v))
    x=np.arange(len(labels))
    rects=ax.bar(x, values)
    ax.set_ylabel("nombre d'apparitions")
    ax.set_title("nombre d'apparitions par article")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    autolabel(rects,ax)
    fig.autofmt_xdate()
    plt.show()



