@echo off
set PYTHONPATH=%~dp0..\pythonpath;%~dp0..\lib\python-qt5;%PYTHONPATH%
start "" "%~dp0..\lib\Python27\pythonw.exe" %*