:: Install Pyblish for Windows
::
:: Run this after cloning to fetch essential libraries and add relevant
:: directories to your local PYTHONPATH. For further information about
:: installation into a distributed environment, see the main Pyblish
:: wiki: https://github.com/pyblish/pyblish/wiki

@echo off

echo "Downloading Pyblish.."
pushd %~dp0
git submodule update --init --recursive
popd

:: Add to PYTHONPATH
echo "Installing to local system.."
setx PYTHONPATH %~dp0python;%PYTHONPATH%

:: Install integrations
echo "Installing integrations.."
setx PYTHONPATH %~dp0lib/pyblish-suite/pyblish-maya/pyblish_maya/pythonpath;%~dp0lib/pyblish-suite/pyblish-nuke/pyblish_nuke/nuke_path;%PYTHONPATH%