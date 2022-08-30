@echo off
echo Creating virtual env...
python -m venv FlipBuilderPDF\venv
call %~dp0FlipBuilderPDF\venv\Scripts\activate
pip install -r FlipBuilderPDF\requirements.txt
