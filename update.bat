@echo off
pushd %~dp0
git pull
git submodule update --init --recursive
popd