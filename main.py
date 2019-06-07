#-*- coding: utf-8 -*-

# 모듈 임포트
import os
import time
from bs4 import BeautifulSoup
import requests
import urllib.request
import zipfile
import shutil

if __name__=="__main__":
    '''
    # 압축 상태 확인
    if not os.path.exists("system/Real-time_inspection_test"):
        print("Please unzip the file properly and execute it.\n\nPress the ENTER key to exit the program.")
        os.system("pause")
        exit()
'''
    # 기본설정
    os.system("title Real-time_inspection_tester V.2.0")
    os.system("mode.com con cols=120 lines=40")
    version="*.*"
    if 

    print("""
                                                   QESASDDS
                                                    .BgK.
                                                   :BBEE.
                                               JBQYBBBsPAW
                                                 EBBPi
                                               .BBPP.
                                              vBBgS
                                             bBBgi
                                            BBM2:
                                          iBBPS
                                         SBQQr
                                        BBBq.
                                      :J::L.
                                     ru7i.
                                    :usJ:
                                   .BU..       ..
                                  :BE       iKBBBBB
                                  ;'     .dBBBBBBRBK
                                 /    :vPEbSBBDSjv12
                       .iv.     / .7IZDZU7. .SYssJv.
                      :iUQM7   / ::7PUr....  71r.
                     .....:uE/.  .........
                      ....../EbL    ...
                       ..  iPBBBB
                         .v2uqRBBB:
                          sj77IgBBBX
                           rJvvIEBBBq
                            .jY77rrLq
                             .JULJjj.
                                :i:.
    Version : V.%s
    Loading. . .
    """ %version)
    language="language"
    while True:
        if not os.path.exists("setting.xml"):
            print("""언어를 선택하세요
Please select a language

1. 한글 - Korean
2. English - 영어
""")

            language = input()

            if language == '1' or language == 'ko' or language == '한글' or language == 'korean':
                language="ko"
                break
            elif language == '2' or language == 'en' or language == '영어' or language == "english":
                language="en"
                break
            else:
                pass
        else:
            break

    if language == "ko" or language == "en":
        file = open("setting.xml", "w", encoding='UTF-8')
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write("<!-- Language (언어) -->\n")
        file.write("<language>%s</language>\n" %language)
        file.write("\n")
        file.write("<!-- File name (미끼파일 이름) -->\n")
        file.write("<filename>EICAR.TXT</filename>\n")
        file.write("\n")
        file.write("<!-- File internal code (미끼파일 내부 코드) -->\n")
        file.write("<!-- default value  (기본값) : X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* -->\n")
        file.write("<fileinside>X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*</fileinside>\n")
        file.close()
    else:
        pass
            
    file = open("setting.xml", "r", encoding='UTF-8')
    html=file.read()
    file.close()
    soup = BeautifulSoup(html, 'html.parser')
    language = soup.find("language")
    language = language.get_text()
    filename = soup.find("filename")
    filename = filename.get_text()
    fileinside = soup.find("fileinside")
    fileinside = fileinside.get_text()
    if language == "ko" or language == "en":
        pass
    else:
        print("Language error\n언어오류\n\nModify the language settings of the setting.xml file(en/ko)\nsetting.xml 파일의 언어설정을 수정하세요(en/ko)")
        os.system("pause")
        exit()

    # 버전 확인
    url = "https://newpremium.github.io/version/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    rtit = soup.find("rtit")
    rtit = rtit.get_text()
    rtitdownload = soup.find("rtitdownload")
    url = rtitdownload.get_text()

    if not os.path.exists("system/1d"):

    if rtit==version or not os.path.exists("system/1d"):
        print("프로그램을 새 버전으로 업데이트 해야 합니다. 자동으로 업데이트가 진행됩니다.\nYou need to update the program to a new version. The update will proceed automatically.")
        
        # 업데이트 폴더 초기화
        try:
            shutil.rmtree('update')
        except FileNotFoundError:
            pass
        os.mkdir("update")

        # 최신버전 다운로드
        urllib.request.urlretrieve(url, "update/master.zip")

        # 압축풀기
        zip_ref = zipfile.ZipFile("update/master.zip", 'r')
        zip_ref.extractall("update")
        zip_ref.close()

        # 현재버전 저장
        file = open("system", "w", encoding='UTF-8')
        file.write(rtit)
        file.close()

        # 설정파일 설치
        file = open("update\Real-time_inspection_tester_V.%s-master\setting.xml" %rtit, "w", encoding='UTF-8')
        file.write(html)
        file.close()

        # 최초 최신버전 다운로드 기록 저장
        file = open("system/1d", "w", encoding='UTF-8')
        file.write("1d")
        file.close()

        # 최신버전 실행
        os.system("call update\Real-time_inspection_tester_V.%s-master\Real-time_inspection_tester.py" %rtit)
        exit()
        