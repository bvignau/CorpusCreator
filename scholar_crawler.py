import os
import scholarly

def GenId(author,title):
    id=""
    for a in author.split(' '):
        if len(a) > 1:
            id+=a
            break
    
    id+=title.split(' ')[0]
search_query=scholarly.search_pubs_query('iot botnet')
with open("res.bib",'w') as fichier:
    for i in range (2):
        
        res=next(search_query,None)
        if res is None:
            print("erreur !!")
        else :
            res.fill()
            print(res)
            line="@article{"+res.bib['id']+","
            fichier.write(line)
            for key, value in res.bib.items():
                if key != 'id':
                    line=key+"={"+value+"},"
                    fichier.write(line)
            fichier.write("}")
