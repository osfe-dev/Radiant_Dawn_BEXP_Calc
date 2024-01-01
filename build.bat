@ECHO OFF

rem Cleanup Releases folder
del ./Releases/new_release.zip
del -r ./Releases/new_release

rem Build new EXE
pyinstaller --onefile --distpath ./ RD_BEXP_CALC.py

rem Create new zip named new_release.zip in the Releases folder
Tar -a -cf ./Releases/new_release.zip RD_BEXP_CALC.exe Resources

rem Cleanup working directory
del RD_BEXP_CALC.exe

PAUSE