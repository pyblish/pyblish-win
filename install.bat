:: Install Pyblish for Windows
::
:: Run this after cloning to fetch essential libraries and add relevant
:: directories to your local PYTHONPATH. For further information about
:: installation into a distributed environment, see the main Pyblish
:: wiki: https://github.com/pyblish/pyblish/wiki

@echo off
pushd %~dp0
git submodule update --init --recursive
popd

:: Add to PYTHONPATH
setx PYTHONPATH %~dp0python;%PYTHONPATH%