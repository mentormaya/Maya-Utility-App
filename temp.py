        # async with aiohttp.ClientSession() as session:
        #     pan_details = await UI_Functions.getPan(session, _pan, _statusBar, _output_container)
        #     _output_container.findChild(QLabel, "raw_pan_output").setText(json.dumps(pan_details, indent=4, ensure_ascii=False))
        #     _statusBar.setText(f'Details fetched Successfully for PAN {_pan}!')
        #     async def getPan(_session, _pan, _statusBar, _container):
        # 
        # async with _session.get(_api_url) as resp:
        #         return await resp.json()
        # asyncio.get_event_loop().run_until_complete(pan_search_thread.start())
        
# echo "Building the project..."
# echo off
# pyinstaller ^
#     --onefile ^
#     --windowed ^
#     --icon "assets//icon.ico" ^
#     --name "MaYa_Utility" ^
#     --clean ^
#     --resource "assets" ^
#     --resource "uploads" ^
#     main.py