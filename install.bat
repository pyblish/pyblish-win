:: Install Pyblish for Windows
::
:: Run this after cloning to fetch essential libraries.

@echo off
pushd %~dp0
git submodule update --init --recursive
popd