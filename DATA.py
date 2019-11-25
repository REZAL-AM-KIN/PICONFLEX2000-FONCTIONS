print("Demarrage 'DATA.py'")
def DATA_setVariable(variableName,contenu):
    fichierName="/home/pi/PICONFLEX2000-CLIENT/setting.py"
    if type(contenu)==str:
        exec("setting."+variableName+"="+"'"+str(contenu)+"'")
    else:
        exec("setting."+variableName+"="+str(contenu))
    _tmp=open(fichierName,"r")
    _ligne=_tmp.readline()
    while _ligne!="":
        _ligne=_tmp.readline()
        if _ligne[:len(variableName)+4]==" "*4+variableName:
            _tmp.close()
            _lineToWrite=" "*4+variableName+"="
            if type(contenu)==str:
                _lineToWrite+="'"+contenu+"'"
            else:
                _lineToWrite+=str(contenu)
            _lineToWrite+="\n"
            _file=DATA_get(fichierName).replace(_ligne,_lineToWrite)
            DATA_set(fichierName,_file)
            return
    _tmp.close()
    print("Variable "+variableName+" non-trouvee")
    REZAL_exit()
    return
def DATA_set(fichierName,contenu):
    DATA_check(fichierName)
    _tmp=open(fichierName,"w")
    _tmp.write(str(contenu))
    _tmp.close()
def DATA_get(fichierName):
    DATA_check(fichierName)
    _tmp=open(fichierName,"r")
    _contenu=_tmp.read()
    _tmp.close()
    return _contenu
def DATA_add(fichierName,contenu):
    DATA_check(fichierName)
    _tmp=open(fichierName,"a")
    _tmp.write(str(contenu))
    _tmp.close()
def DATA_check(fichierName):
    try:
        _tmp=open(fichierName,"r")
        _contenu=_tmp.read()
        _tmp.close()
        return
    except:
        os.system("sudo mkdir "+STRING_getPath(fichierName))
        os.system("sudo touch "+fichierName)
        DATA_check(fichierName)
