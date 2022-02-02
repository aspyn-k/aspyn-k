#--폴더 생성 --> 해시값 추출 -> 해시값 같으면 파일 폴더로 이동, 삭제 --#
import hashlib
import os, shutil

os.mkdir("make directory_dir")  

directory = 'first directory_dir'
for path, dirs, files in os.walk(directory):
    for names in files:
        filedir = os.path.join(path,names)
        afile = open(filedir, 'rb')
        buf = afile.read()

        hash = hashlib.sha256()
        hash.update(buf)

        a = str(hash.hexdigest())
        # print(a, path, files)


directory_compare = 'compare directory_dir'
for root, dirs, files in os.walk(directory_compare):
    for names in files:
        
        filedir = os.path.join(root,names)
        afile = open(filedir, 'rb')
        buf = afile.read()

        hash = hashlib.sha256()
        hash.update(buf)

        b = str(hash.hexdigest())
        # print(b)

if a == b :

    # print (files)

    get_files = os.listdir(directory)
    file_destination = "make directory_dir"
    for g in get_files:
        shutil.move(directory + g, file_destination)

shutil.rmtree("make directory_dir")


