# -*- coding: utf-8 -*-
import allure
import pytest
import os
from utils.tools import classify_hist_with_split
from service.upload import uploadpagetest

@allure.feature('DVWA')
@allure.story('登录')
@allure.title('admin登录')
def test_login(page,set_data):
    page.goto('http://127.0.0.1/dvwa/login.php')
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("admin")
    page.locator("input[name=\"password\"]").fill("password")
    page.get_by_role("button", name="Login").screenshot(path=r"screenshot\login1.png")
    page.get_by_role("button", name="Login").click()
    set_data("cookies",page.context.cookies())
    assert page.get_by_role("heading", name="Welcome to Damn Vulnerable Web Application!").count() == 1

def test_upload(page,get_data):
    page.context.add_cookies(get_data("cookies"))
    uploadpagetest(page)

def test_logout(page,get_data):
    page.context.add_cookies(get_data("cookies"))
    page.goto("http://127.0.0.1/dvwa/index.php")
    page.get_by_role("link", name="Logout").click()
    assert page.get_by_text("Username").count() == 1
    assert page.get_by_text("Password").count() == 1
    assert page.get_by_role("button", name="Login").count() == 1
    page.get_by_role("button", name="Login").screenshot(path=r"screenshot\login2.png")
    assert classify_hist_with_split("screenshot/login2.png","screenshot/login1.png") > 0.9



if __name__ == '__main__':
    pytest.main(['test.py',
                 '-v',
                 '-s',
                 '--headed',
                 '--video=on',
                 '--clean-alluredir',
                 '--screenshot=on',
                 '--alluredir','./report/result'])
    # os.system('allure generate ./report/result -o ./report/html --clean')
    os.system('allure serve ./report/result')
