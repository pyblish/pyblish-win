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

:: Make Pyblish accessible from local terminal
:: regardless of whether or not --global was chosen.
set PYTHONPATH=%~dp0python;%~dp0python\integrations\maya;%PYTHONPATH%
set NUKE_PATH=%~dp0python\integrations\nuke;%NUKE_PATH%
set HOUDINI_PATH=%~dp0python\integrations\houdini;%HOUDINI_PATH%

echo.
if "%1" == "--global" (
  echo Installing globally..

  :: Install integrations
  setx PYTHONPATH %PYTHONPATH%
  setx NUKE_PATH %NUKE_PATH%
  setx HOUDINI_PATH %HOUDINI_PATH%
)

echo.
echo Successfully installed Pyblish
echo See https://github.com/pyblish/pyblish-win/wiki for more information
pause
