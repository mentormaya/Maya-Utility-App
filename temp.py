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

self.setting_name = QtWidgets.QLabel(self.right_menu)
font = QtGui.QFont()
font.setPointSize(9)
font.setBold(True)
font.setUnderline(True)
font.setWeight(75)
self.setting_name.setFont(font)
self.setting_name.setObjectName("setting_name")
self.verticalLayout_12.addWidget(self.setting_name)
self.setting_value = QtWidgets.QLineEdit(self.right_menu)
font = QtGui.QFont()
font.setPointSize(10)
self.setting_value.setFont(font)
self.setting_value.setObjectName("setting_value")
self.verticalLayout_12.addWidget(self.setting_value)
spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)