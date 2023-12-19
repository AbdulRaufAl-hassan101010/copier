@echo off
REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not found in PATH. Please install Python.
    exit /b 1
)

REM Run the Python script
python3 "copier.py" %1 %2 %3
