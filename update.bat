@echo off
pushd %~dp0
git reset --hard
git pull
git submodule update --init --recursive
popd