@echo off
title CyberArena Security - Red Team vs Blue Team
chcp 65001 > nul
cls
echo ============================================================
echo      Starting CyberArena Security (Red vs Blue Team)       
echo ============================================================
echo.
cd /d "%~dp0cyberarenasecurity"
python main.py
echo.
pause
