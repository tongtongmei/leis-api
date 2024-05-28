# -*- coding: utf-8 -*-
import hashlib
import requests


class ThorApi(object):
    URL_LOGIN = "https://webapi.nn.com/api/auth/login"
    URL_RECOVER = "https://webapi.nn.com/api/user/recover"
    URL_PAUSE = "https://webapi.nn.com/api/user/pause"
    GLOBAL_HEADERS = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://vip-jiasu.nn.com",
        "Referer": "https://vip-jiasu.nn.com/"
    }

    def __init__(self, username, password):
        if not username or not password:
            raise ValueError("用户名和密码不能为空")
        self.username = username
        self.password = hashlib.md5(password.encode('utf8')).hexdigest().lower()  # MD5加密
        self.login_info = None
        self.login()

    def _build_login_parameters(self):
        """
        构造登录所需参数
        :return:
        """
        data = {
            "username": self.username,
            "password": self.password,
            "user_type": 0,
            "src_channel": "guanwang",
            "country_code": 86,
            "lang": "zh_CN",
            "region_code": 1,
            "account_token": "null"
        }
        return data

    def login(self):
        """
        登录
        :return:
        """
        try:
            response_login = requests.post(url=self.URL_LOGIN, headers=self.GLOBAL_HEADERS, json=self._build_login_parameters())
            if response_login.status_code == 200:
                result = response_login.json()
                if result.get("code") == 0:
                    print("==登录成功==")
                    self.login_info = result.get("data").get("login_info")
                else:
                    raise ValueError(f"登录失败, result: {result}")
            else:
                raise ValueError(f"登录失败, Response: {response_login.status_code}")
        except requests.exceptions.RequestException as e:
            raise SystemError(f"网络请求异常: {e}")

    def _execute_api_call(self, url, data):
        """
        执行API调用
        :param url:
        :param data:
        :return:
        """
        try:
            response = requests.post(url=url, headers=self.GLOBAL_HEADERS, json=data)
            if response.status_code == 200:
                result = response.json()
                if result.get("code") == 0:
                    return result
                else:
                    raise ValueError(f"操作失败, result: {result}")
            else:
                raise ValueError(f"操作失败, Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise SystemError(f"网络请求异常: {e}")

    def recover(self):
        """
        恢复时间
        :return:
        """
        if not self.login_info:
            raise ValueError("请先登录")
        result = self._execute_api_call(url=self.URL_RECOVER, data=self.login_info)
        print("==恢复成功==")
        return result

    def pause(self):
        """
        暂停时间
        :return:
        """
        if not self.login_info:
            raise ValueError("请先登录")
        result = self._execute_api_call(url=self.URL_PAUSE, data=self.login_info)
        print("==暂停成功==")
        return result


if __name__ == '__main__':
    user = "000"
    pwd = "000"

    thor = ThorApi(user, pwd)
    # thor.recover()
    thor.pause()
