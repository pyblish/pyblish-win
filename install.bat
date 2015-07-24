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
python %~dp0_install.py %*