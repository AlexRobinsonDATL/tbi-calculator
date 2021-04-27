call poetry run python setup.py build
copy config.ini build\exe.win-amd64-3.8\
rename build\exe.win-amd64-3.8\tbi_calculator_exe.exe "TBI Calculator.exe"