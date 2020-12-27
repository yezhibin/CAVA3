#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from APscheduleLib import APscheduleLib
from Sendmail import Sendmail

class MyCustomLib(APscheduleLib, Sendmail):

    def __init__(self, parent=None):
        pass

if __name__ == "__main__":
    pass
