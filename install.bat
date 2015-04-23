:: Install Pyblish for Windows
::
:: Run this after cloning to fetch essential libraries and add relevant
:: directories to your local PYTHONPATH. For further information about
:: installation into a distributed environment, see the main Pyblish
:: wiki: https://github.com/pyblish/pyblish/wiki
::
:: Usage:
::   $ # To install locally, without modifying the users
::   $ install
::
::   $ # To install globally
::   $ install --global

@echo off

echo Installing Pyblish..
echo.

pushd %~dp0
git submodule update --init --recursive
popd

:: Initialise environment variables
set libraries=%~dp0python
set integrations=%~dp0lib\pyblish-suite\pyblish-maya\pyblish_maya\pythonpath;%~dp0lib\pyblish-suite\pyblish-nuke\pyblish_nuke\nuke_path

:: Make Pyblish accessible from local terminal
:: regardless of whether or not --global was chosen.
set PYTHONPATH=%libraries%;%integrations%;%PYTHONPATH%

echo.
if "%1" == "--global" (
  echo Installing globally..
  setx PYTHONPATH %libraries%;%integrations%;%PYTHONPATH%

) else (
  echo Installing locally..
)

echo.
echo Successfully installed Pyblish
echo See https://github.com/pyblish/pyblish-win/wiki for more information