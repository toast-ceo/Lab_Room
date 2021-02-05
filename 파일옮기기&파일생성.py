
import os
import shutil


file_path = ' ' #경로
file_name = os.listdir(file_path)

src = file_path
dest = ''#경로

start_num = 417

for i in range(0, 187):
    s = os.path.splitext(file_path + '\\' + file_name[i])
    s = os.path.split(s[0])
    print(s[1])
    shutil.move(src + '\\' + s[1] + '.JPG', dest + '\\' + str(i+start_num) + '\\' + s[1] + '.JPG')
    spare = i

'''
import os

path = '' #경로

start = 304 # 시작 디렉토리 이름
end = 604 # 끝 디렉토리 이름
for i in range(start, end + 1):
    os.mkdir(path + '\\' + str(i))
'''
