
# from ....A.B import *
import inspect

import sys

class MyFinder(object):
    @classmethod
    def find_module(cls, name, path, target=None):
        print("Importing", name, path, target)
        # 将在后面定义
        return None
        # return MyLoader()

# 由于 finder 是按顺序读取的，所以必须插入在首位
# sys.meta_path.insert(0, MyFinder)
# import json
# from ...json import *


try:
	from ..os import *
except Exception as e:
	for info in inspect.stack():
		print(info)

	# print(e)
# find_module

