# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pytest

if __name__ == '__main__':
    # 运行指定文件夹下的方法
    # pytest.main(['-x', 'D:\github\Python_Learning\Python_Pytest\com\kxj'])

    # 运行某个测试类
    # pytest.main(["com/kxj/test_02_simple.py"])
    # pytest.main(["-sv", "com/kxj/test_02_simple.py"])

    # 运行某个测试类下的方法
    pytest.main(["-sv", "com/kxj/test_02_simple.py::TestClassDemo::test_one"])
