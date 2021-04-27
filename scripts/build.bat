call poetry run python setup.py build
copy config.ini build\exe.win-amd64-3.8\
rename build\exe.win-amd64-3.8\app.exe "TBI Calculator.exe"