pushd "%~dp0"
call setup.bat
cd..

rmdir .eggs /q /s
rmdir build /q /s
rmdir dist /q /s

call poetry build

popd