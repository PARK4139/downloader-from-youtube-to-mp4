import os
import subprocess
import sys
from pytube import Playlist
import traceback


__author__ = 'PARK4139 : Jung Hoon Park'

# :: 정규식 검색
import re


def is_regex_searched(string, regex):
    if re.compile(regex).search(string):
        return True
    else:
        return False

  

def get_length_of_mp3(target_address):
    from mutagen.mp3 import MP3
    try:
        audio = MP3(target_address)
        return audio.info.length
    except Exception as e:
        print('20231129003814')


def helper_speak(text):
    from gtts import gTTS
    import time
    address = rf'{os.getcwd()}\.sound\{text}.mp3'

    try:
        os.makedirs(rf'.\.sound')
    except Exception as e:
        pass

    # :: 가지고 있는 mp3 파일 확인
    if os.path.exists(address):
        os.system(rf'cmd.exe /C call "{address}"')

    else:
        gtts = gTTS(text=text, lang='ko')
        gtts.save(address)
        os.system(rf'cmd.exe /C call "{address}"')



    # :: mp3 파일의 재생 길이 만큼 대기
    length_of_mp3 = get_length_of_mp3(address)
    length_of_mp3 = float(length_of_mp3)
    length_of_mp3 = round(length_of_mp3, 1)
    # time.sleep(length_of_mp3*0.95)
    time.sleep(length_of_mp3 * 1.00)
    # time.sleep(length_of_mp3 * 1.05)


if __name__ == '__main__':
    try:
        # python 코드 실행 하며 인자 받아오기
        file_v=sys.argv[1]
        file_a=sys.argv[2]


        # :: 다운로드 디렉토리 생성
        directories = ["storage"]
        for directory in directories:
            if not os.path.isdir(rf'./{directory}'):
                os.makedirs(rf'mkdir {directory}')

        
        # :: yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge.
        print(rf':: 비디오 사운드를 하나의 파일로 만드는 중입니다')


        # :: 비디오 파일, 음성 파일 절대주소 get
        destination = rf'{os.getcwd()}\storage'
        file_v = os.path.abspath(file_v)
        file_a = os.path.abspath(file_a)
        paths = [os.path.abspath(destination), os.path.basename(file_v)]
        file_va = os.path.join(*paths)
        print(rf'file_v : {file_v}')
        print(rf'file_a : {file_a}')
        print(rf'file_va : {file_va}')
        
        
        # :: ffmpeg.exe 위치 설정
        location_ffmpeg = fr"C:\Users\WIN10PROPC3\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        trouble_characters = ['Ä' ]
        trouble_characters_alternatives = {'Ä': 'A'}
        for trouble_character in trouble_characters:
            file_v = file_v.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_a = file_a.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_va = file_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            # :: 파일명 변경
            try: 
                if trouble_character in file_va:
                    os.rename(file_v, file_v.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
                    os.rename(file_a, file_a.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
            except Exception as e:
                print('파일명 변경 중 에러가 발생하였습니다')
        # :: 파일머지
        try:
            print(fr'echo y | "{location_ffmpeg}" -i "{file_v}" -i "{file_a}" -c copy "{file_va}"')
            lines = subprocess.check_output(fr'echo y | "{location_ffmpeg}" -i "{file_v}" -i "{file_a}" -c copy "{file_va}"', shell=True).decode('utf-8').split("\n")
            for line in lines:
                print(line)
        except Exception as e:
            print('파일머지 중 에러가 발생하였습니다')

        # :: 파일머지 결과확인
        try:
            print(rf':: 다운로드 및 merge 결과 확인')
            print(rf'explorer "{file_va}"')
            subprocess.check_output(rf'explorer "{file_va}"', shell=True).decode('utf-8').split("\n")
        except Exception as e:
            print('파일실행 중 에러가 발생하였습니다')


        # :: 불필요 리소스 삭제
        print(rf':: 불필요 리소스 삭제')
        if os.path.exists(file_va):
            subprocess.check_output(rf'echo y | del /f "{file_v}"', shell=True).decode('utf-8').split("\n")
            lines = subprocess.check_output(rf'echo y | del /f "{file_a}"', shell=True).decode('utf-8').split("\n")
            for line in lines:
                print(line)

 

    except Exception as e:
        # :: trouble shooting
        print(f':: trouble shooting id : 20231129112936')
        print(f'e : {e}')
        print(f'traceback.print_exc(file=sys.stdout) : {traceback.print_exc(file=sys.stdout)}')
        # traceback.print_exc(file=sys.stdout)
