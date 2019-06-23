print("Demarrage 'STRING.py'")
def STRING_montant(montant):
    STRING=str(abs(int(montant)))
    if (len(STRING)==0):
        return ("0,00e")
    elif (len(STRING)==1):
        return ("0,0"+STRING+"e")
    elif (len(STRING)==2):
        return ("0,"+STRING+"e")
    elif (len(STRING)==3):
        return (STRING[0]+","+STRING[1]+STRING[2]+"e")
    else:
        return (STRING[0:-2]+","+STRING[-2]+STRING[-1]+"e")
def STRING_List(tag):
    tag=(8*"0"+str(int(tag)))[-8:]
    LIST=[]
    for i in range(4):
        LIST.append(int(tag[2*i]+tag[2*i+1]))
    return LIST*4
def STRING_Tag(list):
    tag=""
    for i in range(4):
        tag+=(2*"0"+str(list[i]))[-2:]
    return str((8*"0"+str(tag))[-8:])
def STRING_getPath(chemin):
    List=chemin.split("/")
    chemin=""
    for i in range(len(List)-1):
        chemin=chemin+List[i]+"/"
    chemin=chemin[:-1]
    return chemin