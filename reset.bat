:: Reset repository to clone state
::
:: This command will permanently erase any changes you may have
:: made to the repository after the time of cloning.

@echo off
pushd %~dp0
git reset --hard
popd