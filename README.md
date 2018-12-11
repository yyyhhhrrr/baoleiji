# baoleiji

# 轻量级堡垒机demo实现

实现思路：
表设计：1.远程用户表
       2.host表
       3.堡垒机用户表
       4.host组表
       5.bindhost表
       6.中间表见ORM模块
       
数据的插入使用yaml

通过修改paramiko的交互模块interactive进行交互，并将用户操作写入数据库，达到用户操作审计的功能。底层数据库操作使用SQLalchemy ORM框架。

# 文件结构

|-- bin
|   |-- run_jmp.py  命令参数启动方式
|   |-- run_server.py  不用输入命令参数的启动方式
|   |-- __init__.py
|-- conf
|   |-- action_registers.py 操作注册
|   |-- settings.py  配置文件
|   |-- __init__.py

|-- log
|   |-- __init__.py
|-- models
|   |-- models.py 表结构创建
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- models.cpython-37.pyc
|   |   |-- __init__.cpython-37.pyc
|-- modules
|   |-- actions.py 参数解析 操作调用
|   |-- db_conn.py 数据库连接engine
|   |-- interactive.py paramiko原生interactive 修改版
|   |-- ssh_login.py  ssh连接
|   |-- utils.py 工具
|   |-- views.py 视图操作（用户认证，登录，数据添加等）
|   |-- __init__.py
|   |
|-- share
|   |-- example
|   |   |-- new_bindhost.yml bindhost表
|   |   |-- new_groups.yml group表
|   |   |-- new_hosts.yml host表
|   |   |-- new_remoteusers.yml 远程用户表
|   |   |-- new_user.yml 堡垒机用户表


