@echo off
pushd %~dp0lib\pyblish-suite\pyblish
"%~dp0lib/Python27/python.exe" %~dp0lib/pyblish-suite/pyblish/run_testsuite.py
popd
pause
