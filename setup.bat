REM this is a batch file consisting of steps for creating python environment and dependency installation, will run only on windows

@echo off
IF EXIST "env" (
    echo Virtual environment already exists. Activating...
) ELSE (
    echo Creating virtual environment...
    python -m venv env
)

REM Activate the virtual environment
call .\env\Scripts\activate

REM Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

echo The virtual environment is now activated.
