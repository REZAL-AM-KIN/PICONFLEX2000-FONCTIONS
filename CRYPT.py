print("Demarrage 'CRYPT.py'")
def CRYPT_hashage(data):
    seed(data)
    seed(random())
    return str(random()).replace("0.","")[:8]
def CRYPT_HashDossier(path,noList):
    digest = hashlib.sha1()

    for root, dirs, files in os.walk(path):
        for names in files:
            file_path = os.path.join(root, names)
            
            bool_Continue=False
            for No in noList:
                if No in file_path:
                    bool_Continue=True
            if bool_Continue:
                continue
            
            print(file_path)
            digest.update(hashlib.sha1(file_path[len(path):].encode()).digest())

            # Per @pt12lol - if the goal is uniqueness over repeatability, this is an alternative method using 'hash'
            # digest.update(str(hash(file_path[len(path):])).encode())

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f_obj:
                    while True:
                        buf = f_obj.read(1024 * 1024)
                        if not buf:
                            break
                        digest.update(buf)

    return digest.hexdigest()