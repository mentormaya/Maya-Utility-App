echo off
echo "Building the project..."
pyinstaller --onefile --windowed --icon "assets//icon.ico" --name "MaYa_Utility" --clean --resource "assets" --resource "uploads" --add-data ".venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv;nepali_datetime/data/" main.py