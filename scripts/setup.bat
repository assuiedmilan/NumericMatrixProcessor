pushd "%~dp0"

cd ..

rmdir .venv /q /s
virtualenv .venv --python=C:\Python39x64\python.exe
call .venv\Scripts\activate.bat
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install .

popd