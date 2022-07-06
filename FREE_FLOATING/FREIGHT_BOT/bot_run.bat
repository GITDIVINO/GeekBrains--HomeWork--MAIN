@echo off

call %~dp0FREIGHT_BOT\venv\Script\activate

cd %~dp0FREIGHT_BOT

set TOKEN=5485308566:AAEIeTY0SqaR5XKo70zY6QMcEBJixDmG74Q

python main.py

pause

