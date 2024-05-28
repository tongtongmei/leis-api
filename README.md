# ThorApi Client

## 简介

`ThorApi` 是一个Python实现的客户端，用于与特定Web服务进行交互，特别是进行用户身份验证以及管理账户时间状态（如恢复和暂停服务）。该客户端使用`requests`库进行HTTP通信，并对密码进行MD5加密以确保安全性。

## 安装

首先，确保您已经安装了`requests`库。如果没有，请运行以下命令：

pip install requests

## 使用

要使用 `ThorApi`，首先导入类并创建实例，然后调用相关方法：

python from thor_api_client import ThorApi
user = "your_username" pwd = "your_password"
thor = ThorApi(user, pwd) thor.login() thor.recover() # 或者使用 thor.pause() 暂停服务

## 类与方法

### ThorApi

#### 初始化 (`__init__`)

- 接收用户名和密码，对密码进行MD5加密，尝试登录。

#### `_build_login_parameters`

- 私有方法，构建登录请求所需的JSON数据。

#### `login`

- 发送登录请求，处理响应并存储登录信息。

#### `_execute_api_call`

- 私有方法，通用API调用逻辑，处理请求和响应。

#### `recover`

- 调用恢复服务API，需在登录后使用。

#### `pause`

- 调用暂停服务API，需在登录后使用。

## 注意事项

- 用户名和密码不能为空。
- 登录信息会在类实例中存储，用于后续API调用。
- 错误处理包括网络请求异常和业务逻辑错误。








