#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------
# 时间：2016年11月5日16:32:53
# 版本：V1.0.2
# 功能：myRunner启动代码
#-------------------------------------------------------

from tools.MyRunner import *
import datetime
import platform

if __name__ == "__main__":
    if "Linux" == platform.system():
        path_tag = "/"
    else:
        path_tag = "\\"
    demo = MyRunner()
    demo.start_runner_test()
    demo.merge_xml_and_get_html_report(MyRunner.report_dir)
    temp_results = demo.get_all_test_results(MyRunner.report_dir)
    now_timestr = str(datetime.datetime.today().strftime("%Y%m%d-%H%M%S"))
    save_path = MyRunner.report_dir + path_tag + MyRunner.report_dir_tag + "_" + now_timestr + "_Test_Report.xls"
    demo.write_data(temp_results, save_path)
