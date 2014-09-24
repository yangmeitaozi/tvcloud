#!/usr/bin/env python
#coding:utf-8


class User:
    def __init__(self,username,password,age,sex):
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex
        
    def tell(self):
        print'UserContext:Name:%s,pass:%s,age:%s,sex:%s' % (self.username,self.password,self.age,self.sex)
        
        

class Member(User):
    def __init__(self, username, password, age, sex,user_id):
        User.__init__(self,username,password,age,sex)
        self.user_id = user_id
        print'AdminUser:%s' % self.username
        
    def tell(self):
        User.tell(self)
        if self.user_id == 1:
            print 'this is Administrator!'
        else:
            print 'this is User'


if __name__ == '__main__':
    ysex = u'男'.encode('utf-8')
    t = Member('admin', '123456', '28', ysex, 1)
    s = Member('jack','22222','19',ysex,0)
    
    user_member = [t,s]
    for m_user in user_member:
        m_user.tell()