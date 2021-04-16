import os

# get current path
currentPath = os.getcwd()
use_path = currentPath + '\\data\\ch04\\read_test.txt'

f = open(use_path, 'w')
f.write("All grown up.\n")
f.write("were once children,\n")
f.write("although few of them\n")
f.write("remember it.\n")
f.close()

f = open(use_path, 'r')
data = f.read()
f.close()
print(data)


currentPath = os.getcwd()
use_path = currentPath + '\\data\\ch04\\헌법_cp949.txt'
f=open(use_path, 'r', encoding='cp949')
data = f.read()
f.close()
print(data)


# 한 줄씩 읽기

file_name =  currentPath + '\\data\\ch04\\read_test.txt'
f = open(file_name , 'r')
line1 = f.readline()
line2 = f.readline()
f.close()
print(line1, end='')
print(line2, end='')

# 한 줄씩 모든 줄 읽기

f = open(file_name,'r')
line_num=0
while True :
    line = f.readline()
    if (line == ''):
        break
    line_num += 1
    print("{0}:{1}".format(line_num, line), end='')
f.close()


# 한 줄씩을 리스트로 가져오기

f = open(file_name,'r')
lines = f.readlines()
f.close()

line_num = 0
for line in lines:
    line_num += 1
    print("{0} : {1}".format(line_num, line), end ='')


# with 문으로 파일 읽고 쓰기 - close()가 필요 없음

file_name =  currentPath + '\\data\\ch04\\three_times.txt'
with open(file_name, 'w') as f:
    f.write("구구단 3단의 일부\n")
    for num in range(1 , 6):
        format_string = '3 X {0} = {1}\n'.format(num, num*3)
        f.write(format_string)

with open(file_name, 'r') as f:
    data = f.read()
    print(data)

