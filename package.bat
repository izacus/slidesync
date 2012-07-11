@echo off
rem Packages slidesync in previous directory
echo
echo Pulling new revision from Git...
call git pull
echo Cleaning...
rmdir /S /Q dist
rmdir /S /Q slidesync
echo
echo Building executable...
python setup.py py2exe
echo
echo Packaging to slidesync_%date:~-4,4%%date:~-7,2%%date:~-10,2%.7z ...
rename dist slidesync
7z a -t7z ..\slidesync_%date:~-4,4%%date:~-7,2%%date:~-10,2%.7z slidesync

echo
echo
echo ===============================================================
echo  Packaging DONE! File is located in ..\slidesync_%date:~-4,4%%date:~-7,2%%date:~-10,2%.7z
echo ===============================================================