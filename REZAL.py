print("Demarrage 'REZAL.py'")
def REZAL_ping(IP):
    try:
        return int(os.system("ping -a -c 1 -W 1 "+str(IP))==0)
    except:
        return False
def REZAL_pingAndSetState(IP):
    return SQL_EXECUTE(QUERRY_setOnline(IP,int(REZAL_ping(IP))))
def REZAL_pingServeur():
    try:
        return REZAL_ping(setting.connection["host"])
    except:
        return False
def REZAL_pingInternet():
    try:
        return REZAL_ping(setting.serveurNet)
    except:
        return False
def REZAL_getIP():
    try:
        a = str(subprocess.check_output("hostname -I",shell=True).decode('utf-8')).split(" ")[0]
        if a == "\n":
            raise ValueError
        return a
    except:
        return '0.0.0.0'
def REZAL_connect(IP):
    env.host_string=IP
    env.user=setting.connection['user']
    env.password=setting.connection['password']
    env.sudo_user=setting.connection['user']
    env.sudo_password=setting.connection['password']
def REZAL_disconnect():
    disconnect_all()
def REZAL_download(chemin):
    get(chemin,chemin)
def REZAL_getMAC():
    for root,dirs,files in os.walk('/sys/class/net'):
        for dir in dirs:
            if dir[:3]=='enx' or dir[:3]=='eth':
                MAC=open('/sys/class/net/%s/address' %dir).read()[0:17]
    return MAC
def REZAL_getVersion():
    seed(str(CRYPT_HashDossier("/home/pi/PICONFLEX2000-FONCTIONS",["setting.py",".git"]))+str(CRYPT_HashDossier("/home/pi/PICONFLEX2000-CLIENT",["setting.py",".git"])))
    return str(random()).replace("0.","")[:3]
def REZAL_restart():
    hint("REDEMARRAGE",1)
    hint("DU",2)
    hint("SCRIPT",3)
    os.system("sudo python3 /home/pi/PICONFLEX2000-CLIENT/boot.py")
    sys.exit()
def REZAL_reboot():
    hint("REDEMARRAGE",1)
    hint("DU",2)
    hint("RASPBERRY",3)
    os.system("sudo reboot")
    sys.exit()
def REZAL_exit():
    hint("ARRET",1)
    hint("DU",2)
    hint("SCRIPT",3)
    sys.exit()
def REZAL_synchQUERRYToSQL():
    _SQLQUERRY=DATA_get("/home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt")
    if _SQLQUERRY!="":
        SQL_UPDATE(_SQLQUERRY)
        os.system("sudo rm "+"/home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt")
