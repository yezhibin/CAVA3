#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
时间：2016年12月3日08:23:06
功能：robot根据合并xml获取日志报告
版本：V1.0.1
author:yezhibin
'''
import xmlconvert
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TestDemo:

    def __init__(self):
        pass

if __name__=='__main__':
    report_dir_tag = unicode("Batch_Upgrade_Tool")   # html中工具名称，支持中文，作为标签，可以更改
    xml_path_dir = r"./src_xml"     # xml所在文件夹的父目录， 无需修改
    demo = xmlconvert.ConvertClass()
    flag = demo.get_log_and_report(report_dir_tag.encode("gbk"), xml_path_dir)