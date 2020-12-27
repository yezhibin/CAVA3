set CAVA_SPACE=D:\CAVA_SPACE
set PYTHONPATH=D:\CAVA_SPACE\src
d:
cd %CAVA_SPACE%
cd %CAVA_SPACE%\testcases
cd %CAVA_SPACE%\testcases\Camera_Dome
cava client_no_limit=9 execution_plan=first_var testdatas=D:\CAVA_SPACE\testcases\Camera_Dome\Router_Web_Test\DeviceList.xls Router_Web_Test\src\update_test.txt
pause