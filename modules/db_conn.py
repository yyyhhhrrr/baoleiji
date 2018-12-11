#!/usr/bin/env python
# coding:utf-8
# Author:Yang


from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker

from conf import settings


engine = create_engine(settings.ConnParamas,encoding='utf-8')


SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = SessionCls()