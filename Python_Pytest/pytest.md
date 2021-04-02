## pytest

 

**测试的目的是查看特定行为的结果，并确保结果与您的预期一致** 



命名：必须以 `test_` 开头或者 `_test` 结尾，才能被 pytest识别，自动执行测试用例





### pytest 参数

- #### -k

  匹配的范围是文件名、类名、函数名为变量，用and来区分 

  ```python
  class TestClassDemo:
      def test_one(self):
          assert 1 == 1
  
      def test_two(self):
          assert 1 == 1
  ```

   `` pytest -k "TestClassDemoand or test_o" ``

  

  -  **-q, --quiet**

   极简结果显示，简化控制台的输出，可以看出输出信息和之前不添加-q不信息不一样

- **-x**

  第一次失败即停止

  **--maxfail=2**  遇到第二个错误即停止

  

  

  

### 测试

-  **在模块中运行测试** 

  `pytest test_mod.py`

-  **在目录中运行测试** 

  `pytest testing/`

-  **按关键字表达式运行测试** 

  `pytest -k "MyClass and not method"`

-  **按节点ID运行测试** 

  每个收集的测试都被分配一个唯一的 `nodeid` 它由模块文件名和诸如类名、函数名和参数化参数等说明符组成，用 `::` 字符。 

   在模块内运行特定测试 

  `pytest test_mod.py::test_func`

   在命令行中指定测试方法的另一个示例： 

  `pytest test_mod.py::TestClass::test_method`

### 从python代码调用pytest

`pytest.main()`

- 可以指定参数和路径
  （1）‘-s’：关闭捕捉，输出打印信息。
  （2）‘-v’:用于增加测试用例的冗长。
  （3）‘-k’ ：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行XX.py中包含add的测试用例。
  （4）‘q’:减少测试的运行冗长。
  （5）‘-x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。

- 指定某个测试类或测试方法，用“::”隔开。如：
  命令格式：pytest 文件名.py::测试方法
  `pytest.main([模块.py::类或方法])`

- 指定某个测试类下的测试方法，用“::”隔开。如：
  命令格式：pytest 文件名.py::测试类::测试方法
  `pytest.main([模块.py::类::方法])`

  `pytest.main(["testCase/campaign/test_campaign_list.py::TestListCampaign::test_list_campaign_success"])`

- 指定运行某个目录下的某个用例，其中路径为当前执行文件的相对路径
  `pytest.main(["testCase/campaign/test_campaign_list.py"])`

- 执行运行某个目录下的全部用例，写到文件夹名字即可，不需要写到py文件
      `pytest.main(["testCase/campaign/"])`



### fixtures

**参数**
` scope` :  

- `function` ：默认范围，则在测试结束时销毁fixture。
- `class` ：在课程中最后一次测试的拆卸过程中，夹具被破坏。
- `module` ：在模块中最后一次测试的拆卸过程中，夹具被破坏。
- `package` ：在拆下包装中的最后一次试验时，夹具被破坏。
- `session` ：夹具在测试会话结束时被销毁。



### `yield` 



### `conftest.py` 

跨多个文件共享装置


pytest.ini
```
;[pytest]
;addopts = -s  --html=./report.html
;# 测试路径
;testpaths = ./Test
;# 测试文件名
;python_files = test_*.py
;# 测试类名
;python_classes = Test_*
;# 测试的方法名
;python_functions = test_*