@echo off
pushd %~dp0
git submodule update --init --recursive
popd