from bib_parser import *
import configparser

request1=["Mirai","IoT", "Aidra", "amnesia","bashlite","carna","Darlloz","elknot","hajime","hydra","iotreaper","luabot","nyadrop","persirai","psyb0t","qbot","remaiten","satori","soho pharming","spike","themoon","tsunami","vpnfilter","wifatch","xorddos"]    # MODIFY TO ADD NEW FILE NAME AS "r1 r2.bib"
request2=["botnet","malware"]

def ConfigParse():
    config = configparser.ConfigParser()
    config.read('config.conf')
    requests=[]
    for i in range(len(config['Request'])):
        r="r"+str(i)
        requests.append(config['Request'][r].split(','))
    CSV=config['RQ']['CSV'].split(',')
    TEXTE=config['RQ']['Text'].split(',')
    print("Requests = "+str(requests))
    print("CSV = "+str(CSV))
    print("Texte = "+str(TEXTE))
    return requests,CSV,TEXTE



def main():
    requests,CSV,TEXTE = ConfigParse()
    r = GenRequest(requests)
    print(str(r))
    path=os.path.abspath(os.path.split(__file__)[0])
    ida = recupID(r,path)
    idt=sort(ida)
    ShowBar(idt)
    #GenGraph(ida,r)
    GenDirectories(ida,request1,idt,path,CSV,TEXTE)




if __name__ == '__main__':
    main()