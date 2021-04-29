call poetry run python setup.py build


mkdir build\exe.win-amd64-3.8\assets
Xcopy /E assets build\exe.win-amd64-3.8\assets\

copy LICENSE build\exe.win-amd64-3.8\
copy README.md build\exe.win-amd64-3.8\
copy config.ini build\exe.win-amd64-3.8\

mkdir build\exe.win-amd64-3.8\source
copy . build\exe.win-amd64-3.8\source
Xcopy /E assets build\exe.win-amd64-3.8\source\assets\
Xcopy /E scripts build\exe.win-amd64-3.8\source\scripts\
Xcopy /E tbi_calculator build\exe.win-amd64-3.8\source\tbi_calculator\
Xcopy /E tests build\exe.win-amd64-3.8\source\tests\

rename build\exe.win-amd64-3.8\app.exe "TBI Calculator.exe"