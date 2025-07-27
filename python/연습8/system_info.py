import os
import sys


file_name = 'text.txt'

python_version = sys.version
python_path = sys.path

path = os.getcwd()
os_name = os.name
os_env = os.environ
find_dir = os.path.exists(file_name)
abs_path = os.path.abspath(file_name)
name, ext = os.path.splitext(file_name)


print(f"현재 작업 디렉토리 : {path}")
print(f'파이썬 버전 : {python_version}')
print(f"운영 체제 : {os_name}")
print(f"환경 변수 PATH 일부 : {os_env}")
print("파일 경로 정보 : ")
print(f"- 디렉토리 : {abs_path}")
print(f"- 파일명 : {name}")
print(f"- 확장자 : {ext}")
print(f"파일 존재 여부 : {find_dir}")
