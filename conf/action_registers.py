#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from modules import views

actions = {
    'start_session': views.start_session,
    # 'stop': views.stop_server,
    'syncdb': views.syncdb,
    'create_users': views.create_users,
    'create_groups': views.create_groups,
    'create_hosts': views.create_hosts,
    'create_bindhosts': views.create_bindhosts,
    'create_remoteusers': views.create_remoteusers,
    # 需要加个交互 看要审计的用户操作，输入用户名，输出所有操作
}