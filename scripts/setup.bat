pushd "%~dp0"

cd ..

call C:\Python39x64\python.exe -m poetry update
call poetry shell

popd