import os
import shutil

source_path = "C:\\Users\\issac\\Desktop\\몰핑 완성본\\91-100\\" # 사진이 있는 폴더
destination_path = "C:\\Users\\issac\\Desktop\\temp\\" # 사진 저장할 폴더 이름 (단, 1~100 혹은 101 ~ 200폴더는 아래 start_num, end_num이 됨)

start_num = 91 # destination_path폴더 안에 있는 숫자 폴더의 시작부분
end_num = 100 # destination_path폴더 안에 있는 숫자 폴더의 끝 부분

for j in range(start_num, end_num + 1):
    file_name = os.listdir(source_path)
    for i in range(102):
        shutil.move(source_path + file_name[i], destination_path + str(j) + '\\' + str(j)+'_{}.bmp'.format(i + 1))

# 위의 경로부분과 시작폴더 숫자, 끝 폴더 숫자만 변경하면 됨

'''
import os

path = 'C:\\Users\\issac\\Desktop\\temp'

start = 1 # 시작 디렉토리 이름
end = 100 # 끝 디렉토리 이름
for i in range(start, end + 1):
    os.mkdir(path + '\\' + str(i))
'''