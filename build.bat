@echo off
set PYTHONPATH=%~dp0python
"%~dp0bin\python" -m pyblish_win.dist "%~dp0\" --clean %*