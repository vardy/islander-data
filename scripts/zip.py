import tarfile

tar = tarfile.open('./data/data.tar.gz', 'w:gz')
tar.add("data/temp", arcname="data")
tar.close()