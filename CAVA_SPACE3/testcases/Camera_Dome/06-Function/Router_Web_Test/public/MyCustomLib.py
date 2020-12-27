#!/usr/bin/env Python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月21日12:55:29
功能：自定义RF关键字_底层库函数
版本：V1.0.7
@author: yezhibin
'''
import string
import random
import logging
import sys
import os
import datetime
import zipfile
import win32clipboard as w
import win32con
import win32api
# from sdk.HCNetSDK import HCNetSDK
# import HCNetSDK
import time

class MyCustomLib:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_SCOPE = 0.1
    ROBOT_LIBRARY_DOC_FORMAT = 'reST'

    def __init__(self):
        """Library 文档  *斜体* 这个文档用的是reST结构  reStructuredText__.

            __http：//yezhibin.giyhub.io
        """
        #print 'Library arg %s' % arg
        #self._hsdk = HCNetSDK()
        pass

    def make_dir(self,dir_path):
        """
                        功能：新建一级目录，如存在，则提示“已存在!”\n
                        参数：dir_path——一级目录路径\n
                        如：D:/New test
                       返回值：无\n
                       作者：yezhibin
            """
        if os.path.exists(dir_path):
            print dir_path + u"已存在!"
        else:
            os.mkdir(dir_path)
            print dir_path + u"创建完成!"

    def make_dirs(self,dirs_path):
        """
                        功能：新建多级目录,如存在，则提示“已存在!”\n
                        参数：dirs_path——多级目录路径\n
                        如：D:/New test/Log
                       返回值：无\n
                       作者：yezhibin
            """
        #os.makedirs(dirs_path)
        if os.path.exists(dirs_path):
            print dirs_path + u"已存在!"
        else:
            os.makedirs(dirs_path)
            print dirs_path + u"创建完成!"

    def get_element_from_list(self,*myList):
        """
                        功能：获取列表中随机的一个元素条目\n
                        参数：*myList\n
                        例子：
            | ${a} | get_element_from_list | @{list1} |
                        返回值：\n
                        返回列表中随机的一个条目\n
                        作者：yezhibin
            """

        for arg in range (len(myList)):
            print '*INFO* Set List %d Item : %s' % (arg,myList[arg])
        t = random.randint(0, len(myList)-1)
        item1 = myList[t]
        print '*INFO* Get List %d Items : %s' % (t,item1)
        return  item1

    def get_elements_from_list(self,k,*theList):
        """
                        功能：获取列表中随机的若干个元素条目\n
                        参数：*theList\n
            K-抽取个数\n
                        例子：
            | ${a} | get_element_from_list | ${n} | @{list1} |
                        返回值：\n
                        抽取元素组成的新列表\n
                        作者：yezhibin
            """

        for arg in range (len(theList)):
            print '*INFO* Set List %d Item : %s' % (arg,theList[arg])
        #k = random.randint(1, len(theList))
        newList = random.sample(theList, k)
        for args in range (len(newList)):
            print '*INFO* Get newList %d Item : %s' % (args,newList[args])
        return  newList

    def get_length_of_list (self,*thisList):
        """
                        功能：获取列表的长度（元素个数）\n
                        参数：*thisList \n
                        例子：
            | ${a} | get_element_from_list | @{list1} |
                        返回值：\n
                        抽取元素组成的新列表\n
                        作者：yezhibin
            """
        length = len(thisList)
        print "*INFO* 该列表的长度是 : %d" %length
        return length

    def get_items_operator(self,*ranList):
        """
                        功能：获取操作员权限列表中随机的6个元素条目\n
                        参数：*theList\n
                        例子：
            | ${a} | get_element_from_list | ${n} | @{list1} |
                        返回值：\n
                        抽取元素组成的新列表\n
                        作者：yezhibin
            """
        for argx in range (len(ranList)):
            print '*INFO* Set List %d Item : %s' % (argx,ranList[argx])
        #k = random.randint(1, len(ranList))
        k = 6
        newList = random.sample(ranList,k)
        for argnx in range (len(newList)):
            print '*INFO* operator Get List %d Item : %s' % (argnx,newList[argnx])
        return newList

    def get_items_user(self,*ranListu):
        """
                        功能：获取普通用户权限列表中随机的2个元素条目\n
                        参数：*theList\n
                        例子：
            | ${a} | get_element_from_list | ${n} | @{list1} |
                        返回值：\n
                        抽取元素组成的新列表\n
                        作者：yezhibin
            """
        for argy in range (len(ranListu)):
            print '*INFO* Set List %d Item : %s' % (argy,ranListu[argy])
        #k = random.randint(1, len(ranList))
        q = 2
        newListu = random.sample(ranListu,q)
        for argny in range (len(newListu)):
            print '*INFO* user Get List %d Item : %s' % (argny,newListu[argny])
        return newListu

    def get_time_period(self,startTime,endTime):
        """
                        功能：获取时间差，单位为s\n
                        参数：startTime，endTime\n
                        返回值：\n
                        时间差，单位为秒 \n
                        作者：yezhibin
            """
        start_time = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        delta_time = end_time - start_time
        time_period = delta_time.days * 24 * 60 * 60 + delta_time.seconds
        # time_period = delta_time
        # print "*INFO* 时间差是%ds" %time_period
        return time_period

    def get_pc_nowtime(self):
        """
                        功能：获取当前PC时间，格式为"2016-01-27 13:14:40"\n
                        参数：无\n
                        返回值：\n
            PC当前时间 \n
                        作者：yezhibin
            """
        pcNowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print pcNowTime
        return pcNowTime

    def get_dict_value(self,key,mydict):
        """
                        功能：获取字典中某键对应的值\n
                        参数：key——键，mydict——字典\n
                        返回值：key对应的值\n
                        作者：yezhibin
            """
        mylist = mydict.get(key)
        print mylist
        return mylist

    def get_SD_State(self,SD_dict):
        """
                        功能：获取SD卡信息字典中State的值\n
                        参数：SD_dict——磁盘信息字典\n
                        返回值：SD_status———硬盘状态，包括：\n
                    'Active': 活动, 'Sleep': 休眠, 'Abnormal': 异常\n
                    'Sleep&Abnormal': 休眠硬盘异常, 'Unformatted': 未格式化\n
                    'Off-line': 离线(网络硬盘), 'Formatting': 正在格式化\n
                        作者：yezhibin
              """
        dic_list = SD_dict.keys()
        HD_num = dic_list[0]
        SD_status = SD_dict[HD_num]['State']
        print SD_status
        return SD_status

    def get_value_of_Dic_byKey(self,theKey,myDict):
        """
                        功能：获取字典中指定键的值\n
                        参数：myDict——字典\n
                        返回值：指定键的值\n
                        作者：yezhibin
              """
        theValue = myDict[theKey]
        print theValue
        return theValue

    def get_allKey_of_Dict(self, myDict):
        """
                功能：获取字典中所有键组成的列表\n
                参数：myDict——字典名\n
                返回值：所有键组成的列表\n
                作者：yezhibin
            """
        list_of_dict_key = myDict.keys()
        return list_of_dict_key


    def check_Dict_is_null(self, myDict):
        """
                功能：判断字典是否为空\n
                参数：myDict——字典名\n
                返回值：True,字典为空\n
                False，非空\n
                作者：yezhibin
            """
        list_of_dict_key = myDict.keys()
        list_len = self.get_length_of_list(*list_of_dict_key)
        if list_len == 0:
            status = True
        else:
            status = False
        return status

    def check_contain_substring(self,mystr,substring):
        """
                功能：判断字符串是否包含子字符串，注意字符串大小写\n
                参数：mystr——字符串，mydict——子字符串\n
                返回值：True,包含字符串；\n
                False则不包含
                作者：yezhibin
            """
        index = mystr.find(substring)
        if index > -1:
            str_status = True
        elif index == -1:
            str_status = False
        return str_status

    def get_length_of_string(self,thestring):
        """
                功能：返回字符串长度\n
                参数：thestring——字符串\n
                返回值：字符串长度\n
                作者：yezhibin
            """
        str_len = len(thestring)
        return str_len

    def check_stringlen_more_than(self,thestring,comlen):
        """
                功能：判断字符串长度是否大于某个值\n
                参数：thestring——字符串，comlen——比较值\n
                返回值：True,大于；\n
                False则小于或者等于\n
                作者：yezhibin
            """
        leno = len(thestring)
        if leno > comlen:
            str_status = True
        else:
            str_status = False
        return str_status

    def unzip_file(self, zipfilename, unziptodir):
        if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\','/')

            if name.endswith('/'):
                os.mkdir(os.path.join(unziptodir, name))
            else:
                ext_filename = os.path.join(unziptodir, name)
                ext_dir= os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()


    def GetFileList(self, dir, fileList):
        newDir = dir
        if os.path.isfile(dir):
            fileList.append(dir.decode('utf-8'))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                #如果需要忽略某些文件夹，使用以下代码
                #if s == "xxx":
                    #continue
                newDir=os.path.join(dir,s)
                GetFileList(self,newDir, fileList)
        return fileList

    def visit_dir(self, path):
        fileList = []
        li = os.listdir(path)
        for p in li:
            pathname = os.path.join(path, p)
            if not os.path.isfile(pathname):
                visit_dir(self, pathname)
            else:
                fileList.append(pathname)
                #print pathname
        return fileList

    def uzip_program_package_to_theDir(self, package_dir , theDir):
                #theDir = r'D:/AutoTestTool/Batch_Upgrade_ToolV1_0/package/'
                #package_dir = r'D:/AutoTestTool/Batch_Upgrade_ToolV1_0/package/temp'
        testList = self.visit_dir(package_dir)
        for i in testList:
            if self.check_contain_substring(i, "_CN_STD_"):
                #print "CN_STD haha"
                uzip_object_dir = theDir + r'CN'

            elif self.check_contain_substring(i, "_CN_NEU_"):
                #print "CN_NEU haha"
                uzip_object_dir = theDir + r'CNNEU'

            elif self.check_contain_substring(i, "_EN_STD_"):
                #print "EN_STD haha"
                uzip_object_dir = theDir + r'EN'

            elif self.check_contain_substring(i, "_EN_NEU_"):
                #print "EN_NEU haha"
                uzip_object_dir = theDir + r'ENNEU'

            self.make_dirs(uzip_object_dir)
            if os.path.exists(uzip_object_dir + r"/digicap.dav"):
                print uzip_object_dir + "/digicap.dav" + " 已经存在!" #如果已经存在，则不再进行解压缩
            else:
                self.unzip_file(i, uzip_object_dir)
                print uzip_object_dir + "/digicap.dav" + " 创建完成!"

    # def check_device_pt_change(self, ip,port,userName,password):
    #     """
    #                     功能：登录球机，进入循环判断，隔1秒获取设备PT信息，作比较，如无变化则退出判断\n
    #                     参数：\n
    #             ip : 设备的IP地址\n
    #             port : 设备端口号\n
    #             username : 设备的用户名，支持中文\n
    #             password : 设备的密码，支持中文\n
    #                     返回值：False——设备静止\n
    #                     作者：yezhibin
    #         """
    #     ip_dome = HCNetSDK()
    #     ip_dome.netsdk_login(ip,port,userName,password)
    #     num = 1
    #     while True:
    #         fir_pt_dict = ip_dome.netsdk_get_ptz_pos("1")
    #         fir_pz_list = self.get_Device_PT(fir_pt_dict)
    #         for i in range(len(fir_pz_list)):
    #             print u"列表的第" + str(i+1) + u"个元素是：" + str(fir_pz_list[i])
    #             if i == len(fir_pz_list) - 1:
    #                 print ""
    #         time.sleep(1) #隔1秒再次获取PT位置
    #         las_pt_dict = ip_dome.netsdk_get_ptz_pos("1")
    #         las_pt_list = self.get_Device_PT(las_pt_dict)
    #         for j in range(len(las_pt_list)):
    #             print u"列表的第" + str(j+1) + u"个元素是：" + str(las_pt_list[j])
    #             if j== len(las_pt_list) - 1:
    #                 #print "----------------------------------------"
    #                 pass
    #         if fir_pz_list == las_pt_list:
    #             print u"第%d次判断：PT不再变换，设备已静止，退出循环!"%num
    #             num = num + 1
    #             print "---------------------------------"
    #             return False
    #             break
    #         else:
    #             print u"第%d次判断：PT值还在变化，继续循环! " %num
    #             num = num + 1
    #             print "---------------------------------"



    def get_Device_PT(self, ptz_dict):
        """
                        功能：解析PTZ位置字典，返回PT信息列表\n
                        参数：ptz_dict——PTZ位置字典\n
                        返回值：T信息列表\n
                        作者：yezhibin
            """
        p_pos = self.get_value_of_Dic_byKey("Pan", ptz_dict)
        t_pos = self.get_value_of_Dic_byKey("Tilt", ptz_dict)
        pt_list = [p_pos, t_pos]
        return pt_list


    def creat_New_Ini_File(self,soureFile,obejectDir,oldIP,newIP,IPFormat="0"):
        """
                        功能：通过.ini模板文件生成新的ini,可批量\n
                        参数：soureFile——.ini模板文件绝对路径\n
                  obejectDir——新.ini文件绝对路径\n
                  oldIP——.ini模板文件主机IP\n
                  newIP——新.ini文件主机IP\n
                  IPFormat——新.ini文件名后缀，非必选形参
                      :0，文件名为IP.ini形式（默认格式）
                      :1，文件名为IP-1.ini形式
                      :2，文件名为IP-2.ini形式
                        返回值：True——设置成功\n
                        作者：yezhibin
            """

        if(IPFormat == "0"):
            tempStr = newIP + ".ini"
        elif(IPFormat == "1"):
            tempStr = newIP + "-1.ini"
        elif(IPFormat == "2"):
            tempStr = newIP + "-2.ini"
        obejectFile = obejectDir + "\\" + tempStr
        fin = open(soureFile, "r")
        fout = open(obejectFile, "w")
        # header line
        header = fin.readline()
        fout.write(header)
        # data lines
        set_status = False
        for line in fin:
            #if line == 11:
            dat_in = line.split()
            #dat_in[0] = "5.2" # modify datas
            dat_out = " ".join(dat_in)
            if line.find(oldIP) >= 0:
                s = line.replace(oldIP, newIP)
                fout.write(s)
                set_status = True
                print "*INFO* "+ tempStr +" 生成完毕!"

            else:
                fout.write(dat_out+"\n")
            #print line
        # close file
        fin.close()
        fout.close()
        return set_status


    def get_text_from_clipboard(self):
        """
        功能：获取剪切板文本内容并返回
        参数：无
        返回值：剪切板文本字符串
        """
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        return d


    def set_text_to_clipboard(self, str_text):
        """
        功能：复制文本内容到剪切板
        参数：
        str_text：文本内容
        返回值：无
        """
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_TEXT, str_text)
        w.CloseClipboard()


    def keyboard_simulate_ctrl_v(self):
        """
        功能：模拟键盘输入ctrl+v（粘贴）
        参数：
        无
        返回值：无
        """
        win32api.keybd_event(17,0,0,0)  # ctrl键位码是17
        win32api.keybd_event(86,0,0,0)  # v键位码是86
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)   # 释放按键
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)


    def keyboard_simulate_ctrl_c(self):
        """
        功能：模拟键盘输入ctrl+c
        参数：
        无
        返回值：无
        """
        win32api.keybd_event(17,0,0,0)  # ctrl键位码是17
        win32api.keybd_event(67,0,0,0)  # c键位码是67
        win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0)   # 释放按键
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)


    def keyboard_simulate_tab(self):
        """
        功能：模拟键盘输入tab
        参数：
        无
        返回值：无
        """
        win32api.keybd_event(9,0,0,0)  # tab键位码是9
        win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)   # 释放按键


    def keyboard_simulate_enter(self):
        """
        功能：模拟键盘输入enter
        参数：
        无
        返回值：无
        """
        win32api.keybd_event(13,0,0,0)  # enter键位码是13
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)   # 释放按键


if __name__ == "__main__":
    pass
    # a = "2016-11-05 23:46:26"
    # b = "2016-11-06 23:46:27"
    # c = MyCustomLib().get_time_period(a, b)
    # print c
