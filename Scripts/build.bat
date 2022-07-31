echo "Building the project..."
pyinstaller ^
    --onefile ^
    --windowed ^
    --icon "assets//icon.ico" ^
    --name "MaYa_Utility" ^
    --clean ^
    --resource "assets" ^
    --resource "uploads" ^
    --resource ".venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv" ^
    main.py