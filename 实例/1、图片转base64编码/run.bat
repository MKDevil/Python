@echo off
:label
set /p name=
python main/main_for_bat.py %name%
echo finished.
start main/result.txt
goto label
