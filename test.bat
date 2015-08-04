@echo off
pushd %~dp0lib\pyblish-x\modules\pyblish
"%~dp0lib/Python27/python.exe" "%~dp0lib/pyblish-x/modules/pyblish/run_testsuite.py"
popd
pause
