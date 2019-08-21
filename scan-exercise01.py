import os
import glob
import shutil

# 정리할 디텍토리 생성
# c:/my-job/scans 생성

print(os.getcwd())
os.mkdir()

# c:/my-job/scans/01 ~ 20 까지 디렉토리 20개를 만든다.
os.mkdir()  # for 문 사용

# cwd 를 c:/work-for-python(스캔원본이 있는 디렉토리)로 이동
os.chdir()

glob.glob('*.pdf')

# 0000~00010 파일은 01 디렉토리에 복사 후 삭제
# 00011~00020 파일은 02 디렉토리에 복사 후 삭제
# 위 작업을 20번 반복
