print("Demarrage 'QUERRY.py'")
def QUERRY_addArgent(UID,montant):
    return ("UPDATE cartes SET ArgentCarte = ((SELECT ArgentCarte WHERE UID='{}')+'{}') WHERE UID='{}';".format(UID,montant,UID))
def QUERRY_setMontant(UID,montant):
    return ("UPDATE cartes SET ArgentCarte = '{}' WHERE UID='{}';".format(montant,UID))
def QUERRY_addLog(numeroBox,nomBox,titreLog,contenuLog):
    return (("INSERT INTO logs (numeroBox,nomBox, titreLog,contenuLog) VALUES ( '{}' , '{}' , '{}' , '{}' );").format(numeroBox,nomBox,titreLog,contenuLog))
def QUERRY_addCarte(UID):
    return (("INSERT INTO cartes (UID, ArgentCarte) VALUES ( '{}' , '{}' );").format(UID,0))
def QUERRY_getArgent(UID):
    return (("SELECT argentCarte FROM cartes WHERE UID = '{}';").format(UID))
def QUERRY_getName(numeroBox):
    return (("SELECT nomBox FROM boxs WHERE numeroBox  =  '{}';").format(numeroBox))
def QUERRY_addTransaction(produit,nombre,numeroBox,UID,montant,reference):
    montant=montant/nombre
    _str=""
    for i in range(nombre):
        if produit=="VenteMontant":
            _str=_str+(("INSERT INTO ventemontant (UID, montant, box) VALUES ('{}','{}','{}');").format(UID,-montant,numeroBox))#Vente montant
        elif produit=="RechargeMontant":
            _str=_str+(("INSERT INTO recharge (UID, montant, box) VALUES ('{}','{}','{}');").format(UID,montant,numeroBox))#Recharge montant
        else:
            _str=_str+(("INSERT INTO venteproduit (UID, produit, box) VALUES ('{}','{}','{}');").format(UID,reference,numeroBox))#Vente produit
            _str=_str+(("UPDATE stock set stock.stock = (stock.stock -(SELECT produits.quantite/matierepremiere.quantite_matiere from produits JOIN matierepremiere on produits.matierepremiere = matierepremiere.id WHERE produits.reference = '{}')) WHERE stock.matierepremiere_id= (SELECT matierepremiere.id FROM matierepremiere JOIN produits on matierepremiere.id=produits.matierepremiere WHERE produits.reference ='{}') AND stock.comptoir_id =(SELECT comptoir.id FROM comptoir JOIN boxs ON comptoir.id = boxs.comptoir where boxs.numeroBox = '{}');").format(reference,reference,numeroBox))
    return _str
def QUERRY_getMode(numeroBox):
    return ("SELECT mode FROM boxs WHERE numeroBox='{}';".format(numeroBox))
def QUERRY_getNomBox(numeroBox):
    return ("SELECT comptoir.name from comptoir JOIN boxs on comptoir.id = boxs.comptoir WHERE boxs.numeroBox = '{}'".format(numeroBox))
def QUERRY_getVersion(numeroBox):
    return ("SELECT version FROM boxs WHERE numeroBox='{}';".format(numeroBox))
def QUERRY_setVersion(versionNew,numeroBox):
    return ("UPDATE boxs SET version = '{}' WHERE numeroBox='{}';".format(versionNew,numeroBox))
def QUERRY_getIP(numeroBox):
    return ("SELECT IP FROM boxs WHERE numeroBox='{}';".format(numeroBox))
def QUERRY_getBoxs():#changer pour mettre une liste d'IP pour pinger
    return ("SELECT numeroBox FROM boxs;")
def QUERRY_setOnline(IP,Online):
    return ("UPDATE boxs SET Online = '{}' WHERE IP = '{}'".format(Online,IP))
def QUERRY_setIP(IP,numeroBox):
    return ("UPDATE boxs SET IP  = '{}' WHERE numeroBox  = '{}';").format(IP,numeroBox)
def QUERRY_setMAC(MAC,numeroBox):
    return ("UPDATE boxs SET MAC  = '{}' WHERE numeroBox  = '{}';").format(MAC,numeroBox)
def QUERRY_getProduits(numeroBox):
    return ("SELECT produits.reference, produits.nomProduit, produits.prix from ((produits JOIN produit_comptoir on produits.reference = produit_comptoir.produit_reference) join boxs on produit_comptoir.comptoir_id = boxs.comptoir) where boxs.numeroBox = '{}'".format(numeroBox))