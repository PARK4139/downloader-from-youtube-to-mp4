title %~n0
echo "__________________________________________________________________________________________________________________________ minimized window s
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized
echo "__________________________________________________________________________________________________________________________ minimized window e
echo "__________________________________________________________________________________________________________________________ variable defination
chcp 65001
@echo off
@rem @echo on
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
cls
echo "__________________________________________________________________________________________________________________________ add / commit / push


::set commit_ment=%yyyyMMddHHmmss%
::set commit_ment=테스트 커밋.
::set commit_ment=테스트 푸쉬
::set commit_ment=프로젝트 이니셜 커밋.
::set commit_ment=개발환경 이동 및 프로젝트 작동 테스트 완료
::set commit_ment=깃허브 레포지토리명 변경전 백업
::set commit_ment=깃허브 레포지토리명 변경후 첫 커밋 테스트
::set commit_ment=README.md 최신화
::set commit_ment=신규 기능 추가, 추가코드샘플 테스트, README.md 참조
set commit_ment=flask로는 연습 개발 종료.






git add *  
git commit -m "%commit_ment%" 
git push -u origin main  
git status | find "working tree clean" 




set DIRECTORY_THAT_CONTAINING_GIT_FILE=%cd%
CD ..
set DIRECTORY_THAT_CONTAINING_GIT_USELESS_PART=%cd%
echo %DIRECTORY_THAT_CONTAINING_GIT_FILE%
echo %DIRECTORY_THAT_CONTAINING_GIT_USELESS_PART%
SET OPENING_DIRECTORY=%DIRECTORY_THAT_CONTAINING_GIT_FILE%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*\=FOO%
SET OPENING_DIRECTORY=%OPENING_DIRECTORY:*FOO=%
ECHO %OPENING_DIRECTORY%
explorer https://github.com/PARK4139/%OPENING_DIRECTORY%
del /f "git push by auto.py"


timeout 33


