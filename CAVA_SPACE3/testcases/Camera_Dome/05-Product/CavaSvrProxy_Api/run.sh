#!/bin/sh
export PYTHONPATH=/usr/local/bin/CAVA3/CAVA_SPACE3/src:$PYTHONPATH
cd ..
cava client_no_limit=4 execution_plan=first_var testdatas=/usr/local/bin/CAVA3/CAVA_SPACE3/testcases/Camera_Dome/05-Product/CavaSvrProxy_Api/DeviceList.xls CavaSvrProxy_Api/src

