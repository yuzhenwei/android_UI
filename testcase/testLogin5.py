# -*-coding:utf-8-*-
import sys,os, importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
sys.path.append(os.path.abspath('../..'))
from app import util
from app.mytest import Myunittest
from app.testcase import Testcase
import unittest

'''
===========说明============
功能:测试用例定义
入口:ecxel表格测试用例
==========================
'''

class TestLogin(Myunittest):
    """:登录测试"""
    testcaseList = util.getXlsTestCase('bingli')
    for testcase in testcaseList:
        # 判断测试用例是否执行 1——执行,0——不执行;
        exec (util.FUNC_TEMPLATE.format(
                                   func=testcase.get('case_id'),
                                   casename=testcase.get('case_name'),
                                   onecase=testcase,
                                   sheetname='bingli',
                                   state=testcase['state']
                                   ))

if __name__ == '__main__':
    unittest.main()