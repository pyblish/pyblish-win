:: Update to the latest version of Pyblish for Windows
::
:: This update applies to all of Pyblish and it's dependencies.

@echo off
pushd %~dp0
git checkout master
git reset --hard
git pull
git submodule update --init --recursive
git clean -xffd
popd
pause
