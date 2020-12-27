set CAVA_SPACE=D:\CAVA_SPACE
set PYTHONPATH=D:\CAVA_SPACE\src
d:
cd %CAVA_SPACE%
cd %CAVA_SPACE%\testcases
cd %CAVA_SPACE%\testcases\Camera_Dome
cd %CAVA_SPACE%\testcases\Camera_Dome\07-Public_Stability
cava client_no_limit=10 execution_plan=IP  log_directory_name=Batch_Set_Basic_Opt_Tool excel_report=true keylog_show=true testdatas=D:\CAVA_SPACE\testcases\Camera_Dome\07-Public_Stability\Batch_Set_Basic_Opt_Tool\Device_List.xls sheet=[1] Batch_Set_Basic_Opt_Tool\Src\Set_Device_Cfg.txt
pause