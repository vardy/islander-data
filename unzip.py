import tarfile

tar = tarfile.open("data/data.tar.gz", "r:gz")
tar.extractall()
tar.close()