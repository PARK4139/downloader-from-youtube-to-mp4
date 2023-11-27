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
::set commit_ment=테스트 푸쉬
set commit_ment=작업 이력은 README.md 의 DONE 참조요함(%yyyyMMddHHmmss%)






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
@REM echo %~n0.log
@REM timeout 15
@REM pause

