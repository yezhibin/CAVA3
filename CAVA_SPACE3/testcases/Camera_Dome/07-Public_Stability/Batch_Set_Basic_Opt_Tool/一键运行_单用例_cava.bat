set CAVA_SPACE=D:\CAVA_SPACE
set PYTHONPATH=D:\CAVA_SPACE\src
d:
cd %CAVA_SPACE%
cd %CAVA_SPACE%\testcases
cd %CAVA_SPACE%\testcases\Camera_Dome
cd %CAVA_SPACE%\testcases\Camera_Dome\07-Public_Stability
cava client_no_limit=10 log_directory_name=预置点抓图 testdatas=D:\CAVA_SPACE\testcases\Camera_Dome\07-Public_Stability\Batch_Set_Basic_Opt_Tool\Device_List.xls --test 2-3预置点抓图 Batch_Set_Basic_Opt_Tool\Src\Set_Device_Cfg.txt
pause