#!/usr/bin/env python
#coding=utf-8

import my_sql
import yate
import cgi

def start_response():
    print(yate.start_response())
    
    
def substitution(**kwargs):
    for key,keyvalue in kwargs.items():
        pass       
    

def get_formData(*args):    
    responseData = []
    form_data = cgi.FieldStorage()   
    for key in args:       
        responseData.append(form_data.getvalue(key,None))   
    return(responseData)
 
class deal_mysql():
    def __init__(self,dbname=None):
        self.msg = None
        self.response = None     
        def connect(self):
            if dbname is not None:
                return(my_sql.connect(dbname))
            else:
                return(my_sql.connect())        
        self.conn = connect(self)
        def cursor(self):
            return(self.conn.cursor())        
        self.cursor = cursor(self)
        
    def __del__(self):       
        self.conn.close()
        
    def askdata(self,msg):
        self.cursor.execute(msg)
        response = self.cursor.fetchall()
        #self.conn.close()
        return(response)
    
    def updateDb(self,msg):
        self.cursor.execute(msg)
        self.conn.commit()
       # self.conn.close()
       
    def Close(self):
        self.conn.close()
        

    