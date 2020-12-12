# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
时间：2016年2月23日01:29:34
功能：用Python编写RF底层库函数（模板）
版本：V1.0.2
@author: yezhibin
'''
from __future__ import division
import string
import random
import logging
import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class MyCustomLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_SCOPE = 0.1
    ROBOT_LIBRARY_DOC_FORMAT = 'reST'

    def __init__(self):
        """Library 文档  *斜体* 这个文档用的是reST结构  reStructuredText__.\n
            __http：//yezhibin.giyhub.io
        """
        pass
    def get_element_from_list(self,*myList):
        """
                        功能：从指定列表中随机获取一个元素\n
                        参数：*myList\n
                        例子：
            | ${a} | get_element_from_list | @{list1} |
                        返回值：\n
                        列表中随机的一个元素条目
            """

        for arg in range (len(myList)):
            print('*INFO* Set List %d Item : %s' % (arg,myList[arg]))
        t = random.randint(0, len(myList)-1)
        item1 = myList[t]
        print('\n*INFO* Get List %d Items : %s' % (t,item1))
        return  item1

    def get_elements_from_list(self,*theList):
        """
                        功能：获取列表中随机的若干个元素条目\n
                        参数：*theList\n
                        例子：
            | ${a} | get_element_from_list | @{list1} |
                        返回值：\n
                        抽取元素组成的新列表\
            """

        for arg in range (len(theList)):
            print('*INFO* Set List %d Item : %s' % (arg,theList[arg]))
        k = random.randint(1, len(theList))
        newList = random.sample(theList, k)
        for args in range (len(newList)):
            print('*INFO* Get newList %d Item : %s' % (args,newList[args]))
        return  newList

    def get_length_of_list (self,*thisList):
        """
                        功能：获取列表的长度\n
                        参数：*thisList \n
                        例子：
            | ${a} | get_element_from_list | @{list1} |
                        返回值：\n
                        列表的长度值
            """
        length = len(thisList)
        print(u"*INFO* 该列表的长度是：%d" %length)
        return length
    def printSomething(self,n=2):
        for i in range(int(n)):
            print(u"第%d次输出：东北大学" %(i+1))

    def printSomething1(self,n):
        i = 0
        while(i<n):
            print(u"第%d次输出：东北大学" %(i+1))
            i = i + 1

    def get_dict(self):
        dic2 = {0:1234, 1:2, 2:3}
        return dic2

    def f(self,n):
        s = 1
        for i in range (1,n+1):
            s = s * i
        print(u"%d的阶乘是：%d" %(i,s))
        return s

    def for_loop(self):
        for i in range(1,101):
            if(i == 5): #break不能直接用于if，除非if属于循环内部的一个子句
                break   #break用于循环，是用来终止循环。此处break可以用return代替
            print("%d" %i)

    def creat_New_Ini_File(self, sourceFile, objectDir, oldIP, newIP, IPFormat = 0):
        """
                        功能：通过.ini模板文件生成新的.ini文件，可批量\n
                        参数：
                    sourceFile：.ini模板文件绝对路径\n
                    objectDir:新.ini文件绝对路径\n
                    oldIP:.ini模板文件中的主机IP\n
                    newIP：新.ini文件中的主机IP\n
                    IPFormat:新.ini文件名后缀，非必填参数，取值如下：
                        :0，文件名为IP.ini形式（默认格式）
                        :1,文件名为IP-1.ini形式
                        :2,文件名为IP-2.ini形式
                        返回值：True，表示设置成功\n
                        作者：叶志彬
            """
        if(IPFormat == "0"):
            tempStr = newIP + ".ini"
        elif(IPFormat == "1"):
            tempStr = newIP + "-1.ini"
        elif(IPFormat == "2"):
            tempStr = newIP + "-2.ini"
        objectFile = objectDir + "/" + tempStr
        fin = open(sourceFile,"r")
        fout = open(objectFile,"w")
        # header line
        header = fin.readline()
        fout.write(header)
        # data line
        set_status = False
        for line in fin:
            # if line = 11:
            dat_in = line.split()
            #dat_in[0] = "5.2" # modify datas
            dat_out = " ".join(dat_in)
            if line.find(oldIP) >= 0:
                s= line.replace(oldIP, newIP)
                fout.write(s)
                set_status = True
                print(u"*INFO* " + tempStr + " 生成完毕！")

            else:
                fout.write(dat_out + "\n")
            #print line
        # close file
        fin.close()
        fout.close()
        return set_status


if __name__ == "__main__":
    #MyCustomLib().get_length_of_list(u"管理员",u"操作员",u"普通用户",u"会员",u"东北大学")
    #MyCustomLib().get_elements_from_list(u"管理员",u"操作员",u"普通用户",u"会员",u"东北大学")
    #mn = 1 / 2
    #print mn
    #MyCustomLib().for_loop()
    #print
    # MySrcFile = "C:\\Users\Administrator\\Desktop\\10.8.5.72.ini"
    # MyDstDir = "C:\\Users\\Administrator\\Desktop\\output\\"
    # SrcIP = "10.8.5.72"
    # DstIp = "10.8.5.200"

    # MyCustomLib().creat_New_Ini_File(MySrcFile, MyDstDir, SrcIP, DstIp)
    print(MyCustomLib().get_dict())
