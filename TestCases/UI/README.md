# UI自动化设计

利用playwright+pytest+allure简单构造一个UI自动化

优点：1-2天完成UI自动化覆盖

1、无需设计执行代码，使用codegen生成代码，速度效率

2、playwright使用websocket和浏览器通信，相对selenium稳定性更高

3、成熟的pytest和allure框架，简单易学，迅速推广

为什么要写：
1、网上的教程使用大都粗糙，且没有完整的实现一套流程

2、利用pytest-playwright实现，看介绍大都没有观察过源码

3、同事正好有需求，就写一个，实现一个UI自动化最重要的还是提高投入的效率


# 安装

## 1、安装python3
尽量使用python3.11，并未在其他版本验证

安装教程网上大把

## 2、安装pycharm
安装教程略

## 3、安装requirements python包
1、打开pycharm，加载AutoTest工程

2、创建venv  File-setting-Project-Python Interpreter  创建一个venv  python的独立虚拟环境，会在项目中新增一个venv目录

3、点击TestCases/UI/test.py   pycharm会在上方提示安装requirements，全部安装即可

4、也可以手工安装，进入到venv/scripts目录下执行pip install -r requirements.txt安装

## 4、安装playwright浏览器
1、进入到venv/scripts目录下，执行playwright install安装playwright的浏览器，相当于selenium的chrome.exe

## 5、更新pytest_playwright.py文件
1、需要更新将截图和视频增加到allure报告中的语句，如果安装的版本与笔者相同，可以拿utils里的此文件剪切过去直接覆盖venv\Lib\site-packages\pytest_playwright/pytest_playwright.py

2、也可以手工更新allure.attach.file两句，复制utils里pytest_playwright.py中allure.attach.file两句到venv\Lib\site-packages\pytest_playwright/pytest_playwright.py中

## 6、安装allure命令行程序
安装过程略

# 使用
进入到UI目录下，此目录下保存的是UI自动化的相关文档

## 结构

report：保存的执行记录

screenshot：截图放置路径

service：业务封装的函数放置路径，提高主体测试py的可阅读性

conftest.py: pytest的特性文件，在每个用例执行前执行，相当于setup和teardown

test.py:主体类 以test为开头的函数为测试用例

## 样本代码讲解

### conftest.py

```python
	如果测试用例中引用，可以将执行数据保存在data字典中
	setdata()
	如果测试用例中引用，可以将保存在data字典中的数据获取出来
	getdata()
```

### test.py

```python
	allure报告中的目录结构   三层   测试DVWA靶场的登录
	@allure.feature('DVWA')
	@allure.story('登录')
	@allure.title('admin登录')
	
```

```python
	三个用例
	test_login  测试登录，并将登录cookie保存
	test_upload 测试文件上传，并利用login的cookies，不重复登录，使用封装的方式，简化测试用例展示
	test_logout 测试登出
```

### 测试代码生成

```python
	在venv/Scripts目录下执行playwright codegen，跳出代码生成器和浏览器
	选择生成python代码
	在浏览器中操作，代码生成器会自动记录所有操作事件
	生成的代码直接copy到pytest用例中，增加部分等待事件确保页面能渲染成功
	增加最后的断言
	upload用例中，增加了最终页面存在succesfully字样
	logout用例中，判断退出后和登录前的login截图几乎相等
	
```



## 执行

1、右键test.py，选择Run test，运行后出报告

```python
test.py::test_login[chromium] PASSED
test.py::test_upload[chromium] PASSED
test.py::test_logout[chromium] PASSED

============================= 3 passed in 10.59s ==============================
Generating report to temp directory...
Report successfully generated to C:\Users\sml\AppData\Local\Temp\10228255547571767729\allure-report
Starting web server...
2023-07-06 08:55:28.700:INFO::main: Logging initialized @2736ms to org.eclipse.jetty.util.log.StdErrLog
Server started at <http://127.0.0.1:61028/>. Press <Ctrl+C> to exit
```

# 报告

1、会自动跳出报告，可以在behaviors中查看用例的执行情况

2、在右边窗口execution--teardown--context中，会附上最后页面的截图和完整测试过程的视频