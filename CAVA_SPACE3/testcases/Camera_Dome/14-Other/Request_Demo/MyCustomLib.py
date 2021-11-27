# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
时间：2021年11月28日00:25:49
功能：用Python编写RF底层库函数（模板）
版本：V1.0.2
@author: yezhibin
'''
from __future__ import division
import string
import random
import hashlib
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

    def gen_random(self, len=32):
        """
        功能：生成一个小写的随机字符串，长度可以指定，默认32\n
        参数：len\n
        例子：
        | ${random} | gen_random | 16 |
        返回值：\n
        小写的随机字符串
        """

        random_str = ''.join(random.sample(string.ascii_letters + string.digits, len))

        return random_str
    
    def gen_sha256_hash(self, plain):
        """
        功能：对原文数据计算sha256哈希值\n
        参数：plain\n
        例子：
        | ${hash} | gen_sha256_hash | testdata |
        返回值：\n
        对应的sha256哈希值
        """

        m = hashlib.sha256()
        m.update(plain.encode("utf-8"))
        hash = m.hexdigest()
        return hash

if __name__ == "__main__":
    # ret = MyCustomLib().gen_sha256_hash("testtest1234lw4IfjZPdKNOGL6oYXEsD1xhcqiztW9H1638028868")
    # print("ret: %s" %ret)
    pass