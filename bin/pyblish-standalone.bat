@echo off
set PYBLISH_QML_CONSOLE=1
set PYBLISHSTANDALONEBATCH=1  :: Signal that it can't be gracefully shutdown
"%~dp0python" "%~dp0_launcher.py" "%~dp0\" pyblish_standalone %*