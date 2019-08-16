from bib_parser import *

request1=["Mirai","IoT"]    # MODIFY TO ADD NEW FILE NAME AS "r1 r2.bib"
request2=["botnet","malware"]

def main():
    r = GenRequest(request1,request2)
    print(str(r))
    ida = recupID(r)
    ShowBar(ida)
    GenGraph(ida,r)




if __name__ == '__main__':
    main()