import os
import glob
import shutil


def make_dir_for_arrange():
    if not os.path.exists('c:\\my-job'):
        os.mkdir('c:\\my-job')
    if not os.path.exists('c:\\my-job\\scans'):
        os.mkdir('c:\\my-job\\scans')
    os.chdir('c:\\my-job\\scans')
    # c:/my-job/scans/1 ~ 20 까지 디렉토리 20개를 만든다.
    for dir_name in range(1, 21):
        try:
            os.mkdir(str(dir_name))  # for 문 사용
        except:
            pass


def check_for_work_and_get_files():
    os.chdir('c:\\work-for-python')
    return glob.glob('*.pdf')


def arrange_scanfiles(files):
    for file in files:
        the_number = int(file.split('-')[1])
        if the_number <= 10:
            shutil.copy(file, 'c:\\my-job\\scans\\1')
        elif the_number <= 20:
            shutil.copy(file, 'c:\\my-job\\scans\\2')
        elif the_number <= 30:
            shutil.copy(file, 'c:\\my-job\\scans\\3')
        elif the_number <= 40:
            shutil.copy(file, 'c:\\my-job\\scans\\4')
        else:
            shutil.copy(file, 'c:\\my-job\\scans\\5')


def main():
    make_dir_for_arrange()
    files = check_for_work_and_get_files()

    if not len(files) == 0:
        arrange_scanfiles(files)
    else:
        print('정리할 파일이 없습니다.')

    print('job completed..')


main()
