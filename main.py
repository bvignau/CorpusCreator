from bib_parser import *

request1=["Mirai","IoT", "Aidra", "amnesia","bashlite","carna","Darlloz","elknot","hajime","hydra","iotreaper","luabot","nyadrop","persirai","psyb0t","qbot","remaiten","satori","soho pharming","spike","themoon","tsunami","vpnfilter","wifatch","xorddos"]    # MODIFY TO ADD NEW FILE NAME AS "r1 r2.bib"
request2=["botnet","malware"]

def main():
    r = GenRequest(request1,request2)
    print(str(r))
    ida = recupID(r)
    idt=sort(ida)
    ShowBar(idt)
    #GenGraph(ida,r)
    GenDirectories(ida,request1,idt)




if __name__ == '__main__':
    main()