@echo off
chcp 65001 >nul
title Stock Dashboard
set "ROOT=%~dp0"
set "VENV_PYTHON=%ROOT%stock-sentiment\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Python not found in virtual environment:
    echo %VENV_PYTHON%
    pause
    exit /b 1
)

REM Server runs in this window and opens the browser by itself. Close the window to stop.
"%VENV_PYTHON%" "%ROOT%launch_dashboard.py"
if errorlevel 1 pause
