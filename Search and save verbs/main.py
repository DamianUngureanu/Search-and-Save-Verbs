import random
import shutil
import urllib.request
from clase_verbe import *
# -*- coding: utf-8 -*-

    



def cautaConjugarea(verb):

    verb=verb.replace("ă","a"); verb=verb.replace("â","a"); verb=verb.replace("î","i"); verb=verb.replace("ș","s"); verb=verb.replace("ț","t")
    verb=verb.replace("Ă","A"); verb=verb.replace("â","A"); verb=verb.replace("Î","I"); verb=verb.replace("Ș","S"); verb=verb.replace("Ț","T")
    page = urllib.request.urlopen(f'https://www.conjugare.ro/romana.php?conjugare={verb}')
    #print(page.read())
    htmlDocument=str(page.read())
    cauta=''
    intre=''
    ceCaut=''
    rezultate=[['Infinitiv',0,0],['Infinitiv Lung',49,-77],['Participiu',54,-96],['Gerunziu',50,-63],['singular',48,-146],['plural',12,-53],['singular negativ',10,-48],['plural negativ',20,-53],
               ['eu',18,-148],['tu',6,-53],['el/ea',6,-48],['noi',9,-54],['voi',7,-48],['ei/ele',7,-54],['eu',10,-126],['tu',18,-53],['el/ea',18,-48],['noi',21,-54],['voi',19,-48],['ei/ele',19,-54],
               ['eu',22,-131],['tu',6,-53],['el/ea',6,-48],['noi',9,-54],['voi',7,-48],['ei/ele',7,-54],['eu',10,-556],['tu',6,-53],['el/ea',6,-47],['noi',9,-53],['voi',7,-47],['ei/ele',7,-53],
               ['eu',10,-128],['tu',6,-53],['el/ea',6,-48],['noi',9,-54],['voi',7,-48],['ei/ele',7,-54],['eu',10,-140],['tu',19,-53],['el/ea',19,-48],['noi',22,-54],['voi',20,-48],['ei/ele',20,-54],
               ['eu',23,-167],['tu',16,-53],['el/ea',9,-48],['noi',12,-54],['voi',10,-48],['ei/ele',18,-54],['eu',13,-134],['tu',19,-53],['el/ea',12,-48],['noi',15,-54],['voi',13,-48],['ei/ele',21,-54],
               ['eu',16,-138],['tu',9,-53],['el/ea',9,-48],['noi',11,-54],['voi',10,-48],['ei/ele',18,-54],['eu',13,-147],['tu',10,-53],['el/ea',10,-48],['noi',12,-54],['voi',11,-48],['ei/ele',19,-54],
               ['eu',14,-123],['tu',13,-53],['el/ea',13,-48],['noi',15,-54],['voi',14,-48],['ei/ele',22,-54],['Verbele anterioare',17,-64]]
    deAflat=[]
    i=r'\xc3\xae'
    a1=r'\xc4\x83'
    a2=r'\xc3\xa2'
    s=r'\xc8\x99'
    t=r'\xc8\x9b'

    y=0
    ok=0
    for rezultat,start,stop in rezultate:

        intre=''
        x=len(rezultat)+y
        cauta=htmlDocument[y:x]
        taiere= slice(start,stop)
        while cauta!=rezultat:
            cauta=htmlDocument[y+1:x+1]
            if ok!=0:
                intre=intre+htmlDocument[y+1]
            y+=1
            x+=1
        if ok!=0:
            ceCaut=intre[taiere]
            dr=8
            st=0
            modificareDiacritice=ceCaut[st:dr]
            while dr<=len(ceCaut):
                if(modificareDiacritice==i):
                    ceCaut2=ceCaut[:st]+'î'+ceCaut[dr:]
                    ceCaut=ceCaut2
                elif(modificareDiacritice==a1):
                    ceCaut2=ceCaut[:st]+'ă'+ceCaut[dr:]
                    ceCaut=ceCaut2
                elif(modificareDiacritice==a2):
                    ceCaut2=ceCaut[:st]+'â'+ceCaut[dr:]
                    ceCaut=ceCaut2
                elif(modificareDiacritice==s):
                    ceCaut2=ceCaut[:st]+'ș'+ceCaut[dr:]
                    ceCaut=ceCaut2
                elif(modificareDiacritice==t):
                    ceCaut2=ceCaut[:st]+'ț'+ceCaut[dr:]
                    ceCaut=ceCaut2
                modificareDiacritice=ceCaut[st+1:dr+1]
                st+=1
                dr+=1
        deAflat.append(ceCaut)
        ok+=1
    with open('clase_verbe.py','a',encoding='utf-8') as memorie:
        memorie.write(f'class {deAflat[1]}:\n  infinitiv="{deAflat[1]}";infinitiv_lung="{deAflat[2]}";participiu="{deAflat[3]}";gerunziu="{deAflat[4]}"\n  class imperativ:\n\
        singular="{deAflat[5]}";plural="{deAflat[6]}";singular_negativ="{deAflat[7]}";plural_negativ="{deAflat[8]}"\n  class prezent:\n\
        eu="{deAflat[9]}";tu="{deAflat[10]}";el_ea="{deAflat[11]}";noi="{deAflat[12]}";voi="{deAflat[13]}";ei_ele="{deAflat[14]}"\n  class conjunctiv_prezent:\n\
        eu="{deAflat[15]}";tu="{deAflat[16]}";el_ea="{deAflat[17]}";noi="{deAflat[18]}";voi="{deAflat[19]}";ei_ele="{deAflat[20]}"\n  class imperfect:\n\
        eu="{deAflat[21]}";tu="{deAflat[22]}";el_ea="{deAflat[23]}";noi="{deAflat[24]}";voi="{deAflat[25]}";ei_ele="{deAflat[26]}"\n  class perfect_simplu:\n\
        eu="{deAflat[27]}";tu="{deAflat[28]}";el_ea="{deAflat[29]}";noi="{deAflat[30]}";voi="{deAflat[31]}";ei_ele="{deAflat[32]}"\n  class mai_mult_ca_perfect:\n\
        eu="{deAflat[33]}";tu="{deAflat[34]}";el_ea="{deAflat[35]}";noi="{deAflat[36]}";voi="{deAflat[37]}";ei_ele="{deAflat[38]}"\n  class conjunctiv_perfect:\n\
        eu="{deAflat[39]}";tu="{deAflat[40]}";el_ea="{deAflat[41]}";noi="{deAflat[42]}";voi="{deAflat[43]}";ei_ele="{deAflat[44]}"\n  class conditional_prezent:\n\
        eu="{deAflat[45]}";tu="{deAflat[46]}";el_ea="{deAflat[47]}";noi="{deAflat[48]}";voi="{deAflat[49]}";ei_ele="{deAflat[50]}"\n  class conditional_perfect:\n\
        eu="{deAflat[51]}";tu="{deAflat[52]}";el_ea="{deAflat[53]}";noi="{deAflat[54]}";voi="{deAflat[55]}";ei_ele="{deAflat[56]}"\n  class perfect_compus:\n\
        eu="{deAflat[57]}";tu="{deAflat[58]}";el_ea="{deAflat[59]}";noi="{deAflat[60]}";voi="{deAflat[61]}";ei_ele="{deAflat[62]}"\n  class viitor:\n\
        eu="{deAflat[63]}";tu="{deAflat[64]}";el_ea="{deAflat[65]}";noi="{deAflat[66]}";voi="{deAflat[67]}";ei_ele="{deAflat[68]}"\n  class viitor_anterior:\n\
        eu="{deAflat[69]}";tu="{deAflat[70]}";el_ea="{deAflat[71]}";noi="{deAflat[72]}";voi="{deAflat[73]}";ei_ele="{deAflat[74]}"\n')


        
cuvantInput=input("cuvant: ")
while(cuvantInput!=0):
    cautaConjugarea(cuvantInput)
    cuvantInput=input("cuvant: ")




    