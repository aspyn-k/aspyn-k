#2--딕셔너리 이용 -- 폴더생성 --> 해시값 추출 -> 해시값 같으면 파일 폴더로 이동, 삭제 --#

from curses import KEY_MARK
import hashlib
from re import A, X
from tkinter import Y
from unittest import result

import os, shutil

a_list =[]
a_name = []

directory = 'C:/Users/user/yolo/test/'
for path, dirs, files in os.walk(directory):
    for names in files:
        filedir = os.path.join(path,names)
        afile = open(filedir, 'rb')
        buf = afile.read()

        filename, fileExtension = os.path.splitext(names)

        hash = hashlib.sha256()
        hash.update(buf)

        a = str(hash.hexdigest())
        a_hash = "".join(a)
        a_list.append(a_hash)
        
        a_filename = str(filename+fileExtension)
        a_hash_name = "".join(a_filename)
        a_name.append(a_hash_name)


x = {'hash': a_list, 'filename': a_name}
print(x)


b_list=[]
b_name=[]
directory_compare = 'C:/Users/user/yolo/remove/'
for root, dirs, files in os.walk(directory_compare):
    for names in files:
        
        filedir = os.path.join(root,names)
        afile = open(filedir, 'rb')
        buf = afile.read()
        filename, fileExtension = os.path.splitext(names)
        hash = hashlib.sha256()
        hash.update(buf)
        b =str(hash.hexdigest())
        m = "".join(b)
        b_list.append(m)

        b_filename = str(filename+fileExtension)
        b_hash_name = "".join(b_filename)
        b_name.append(b_hash_name)


y = {'hash': b_list, 'filename': b_name}
print(y)


os.mkdir("C:/Users/user/yolo/ki")  
for xx in x['hash'] :
    for xxx in x['filename']:
        for yy in y['hash']:
            for yyy in y['filename']:
                if xx == yy:
                    print(xxx)
                    file_destination = 'C:/Users/user/yolo/ki'
                    shutil.move(directory + xxx, file_destination)
                else:
                    print("안뇽")

                break
            break
        break
    break
shutil.rmtree('C:/Users/user/yolo/ki')



#1--폴더 생성 --> 해시값 추출 -> 해시값 같으면 파일 폴더로 이동, 삭제 --#
#--문제점: 파일 여러개가 있을 때 오류 발생 --#

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


