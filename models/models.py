#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from sqlalchemy import Table, Column, Integer,String,DateTime, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils import ChoiceType


Base=declarative_base()

user_m2m_bindhost = Table('user_m2m_bindhost',Base.metadata,
                          Column('userprofile_id',Integer,ForeignKey('user_profile.id')),
                          Column('bindhost_id',Integer,ForeignKey('bind_host.id')),)

bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup',Base.metadata,
                          Column('bindhost_id',Integer,ForeignKey('bind_host.id')),
                          Column('hostgroup_id',Integer,ForeignKey('host_group.id')),)

user_m2m_hostgroup = Table('userprofile_m2m_hostgroup',Base.metadata,
                          Column('userprofile_id',Integer,ForeignKey('user_profile.id')),
                          Column('host_group_id',Integer,ForeignKey('host_group.id')),)




class Host(Base):

    '''主机表'''

    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)


    def __repr__(self):
        return self.hostname

class HostGroup(Base):

    '''主机组'''

    __tablename__ = 'host_group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)

    bind_host=relationship("BindHost",secondary='bindhost_m2m_hostgroup',backref="host_groups")

    def __repr__(self):
        return self.name

class RemoteUser(Base):

    '''远程用户'''

    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_type','username','password',name='_user_passwd_uc'),) # 三个字段做联合唯一 并取名

    id = Column(Integer,primary_key=True)
    AuthTypes=[
        ('ssh-password','SSH/Password'), # 第一个是真正存在数据库的值，第二个是显示的值
        ('ssh-key','SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))


    def __repr__(self):
        return self.username

class BindHost(Base):

    '''
    host            remote_user
    192.168.1.11       root
    '''

    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('host_id','remoteuser_id',name='_host_remoteuser_uc'),) # 联合唯一

    id = Column(Integer,primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    # group_Id = Column(Integer,ForeignKey='host_group.id')
    remoteuser_id = Column(Integer,ForeignKey('remote_user.id'))

    host = relationship('Host',backref='bind_hosts')
   # group = relationship('HostGroup',backref='bind_hosts')
    remote_user = relationship('RemoteUser',backref='bind_hosts')


    def __repr__(self):
        return "<%s -- %s>"%(self.host.ip,
                            self.remote_user.username
                                 )

class UserProfile(Base):

    '''堡垒机用户'''

    __tablename__='user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))

    bind_hosts = relationship('BindHost',secondary='user_m2m_bindhost',backref='user_profiles')
    host_group = relationship('HostGroup',secondary='userprofile_m2m_hostgroup',backref='user_profiles')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user_profile.id'))
    bind_host_id = Column(Integer,ForeignKey('bind_host.id'))
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]
    action_choices2 = [
        (u'cmd',u'CMD'),
        (u'login',u'Login'),
        (u'logout',u'Logout'),
        # (3,'GetFile'),
        # (4,'SendFile'),
        # (5,'Exception'),
    ]
    action_type = Column(ChoiceType(action_choices2))
    #action_type = Column(String(64))
    cmd = Column(String(255))
    date = Column(DateTime)

    user_profile = relationship("UserProfile",backref='audit_logs')
    bind_host = relationship("BindHost",backref='audit_logs')




