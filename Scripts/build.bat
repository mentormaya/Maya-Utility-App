echo "Building the project..."
echo off
pyinstaller ^
    --onefile ^
    --windowed ^
    --icon "assets//icon.ico" ^
    --name "MaYa_Utility" ^
    --resource "assets" ^
    --resource "uploads" ^
    main.py