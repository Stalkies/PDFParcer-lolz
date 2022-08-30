@echo off
echo Configuring parser...
call %~dp0venv\Scripts\activate
python main.py
pause