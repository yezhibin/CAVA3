set CAVA_SPACE=D:\CAVA_SPACE
set PYTHONPATH=D:\CAVA_SPACE\src
d:
cd %CAVA_SPACE%
cd %CAVA_SPACE%\testcases
cd %CAVA_SPACE%\testcases\Camera_Dome
cd %CAVA_SPACE%\testcases\Camera_Dome\14-Other
cava client_no_limit=9 execution_plan=first_var testdatas=D:\CAVA_SPACE\testcases\Camera_Dome\14-Other\modify_net_info\DeviceList.xls modify_net_info\modify_ip.txt
pause