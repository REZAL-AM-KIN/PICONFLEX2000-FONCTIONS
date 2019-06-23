print("Demarrage 'SQL.py'")
def SQL_SELECT(querry):
    _cnx=mysql.connector.connect(**setting.connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _select=_cursor.fetchall()
    _cnx.close()
    return _select
def SQL_UPDATE(querry):
    _cnx=mysql.connector.connect(**setting.connection)
    _cursor=_cnx.cursor()
    querrys=querry.split(";")
    print("Synchronisation SQL: "+str(len(querrys))+" requetes")
    n=len(querrys)
    for i in range(len(querrys)):
        hint("SYNCH SQL "+str(i)+" / "+str(n),4)
        q=querrys[i]
        _cursor.execute(q)
        _cnx.commit()
    _cnx.close()
    DATA_add('/home/pi/PICONFLEX2000-LOGS/LOG_SQL.txt',querry+"\n")
def SQL_EXECUTE(querry):
    _cnx=mysql.connector.connect(**setting.connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _cnx.commit()
    _cnx.close()
    DATA_add('/home/pi/PICONFLEX2000-LOGS/LOG_SQL.txt',querry+"\n")
def SQL_getVersion(numeroBox):
    return SQL_SELECT(QUERRY_getVersion(numeroBox))[0][0]
def SQL_getProduits(numeroBox):
    _produits_SQL=SQL_SELECT(QUERRY_getProduits(numeroBox))
    produits={}
    for i in _produits_SQL:
        produits[i[0]]=[i[1],i[2]]
    return produits
def SQL_getIP(numeroBox):
    return SQL_SELECT(QUERRY_getIP(numeroBox))[0][0]
def SQL_getBoxs():
    _SQL=SQL_SELECT(QUERRY_getBoxs())
    Boxs=[]
    for i in _SQL:
        Boxs.append(i[0])
    return Boxs
def SQL_setRezalOn(IP,Online):
    SQL_EXECUTE(QUERRY_setOnline(IP,Online))