#! /usr/bin/env python
#coding=utf-8
######################
# @author kenny
# @date 2014-07-15
######################
import urllib2
import xml.etree.ElementTree as Et
from socket import errno as SocketError
import errno

def parse_tvsou():
        urls = 'http://hz.tvsou.com/jm/bjxest/channellist.asp'
        filename = 'channel.xml'

        s=urllib2.urlopen(urls)
        ss=s.read()

        try:
                with open(filename,'w') as fd:
                        for each_line in ss:
                                fd.write(each_line)
        except IOError as error:
                print('open file error:'+str(error))

        tree = Et.parse(filename)
        root = tree.getroot()
        lst=root.getiterator('C')

        channel_info={}
        for node in lst:
                c=node.find('ChannelName')
                #print(c.text)
                cc=node.find('Tvid')
                #print(cc.text)
                tt=node.find('id')
                node={'channelid':tt.text,'channelname':c.text,'tvid':cc.text}
                channel_info[node['channelid']] = node
                #print(channel_info[node['channelid']])
        return channel_info

def parse_tvsou_updatelog():
        urls = 'http://hz.tvsou.com/jm/bjxest/catchindex.asp'
        filename = 'updatelog.xml'
        try:
                s=urllib2.urlopen(urls)
                ss=s.read()
        except urllib2.URLError,SocketError:
                return
        try:
                with open(filename,'w') as fd:
                        for each_line in ss:
                                fd.write(each_line)
        except IOError as error:
                print('open file error:'+str(error))

        tree = Et.parse(filename)
        root = tree.getroot()
        lst=root.getiterator('sdd') 
        if lst == []:
                return None
        channel_info={}
        
        for node in lst:    
                try:
                        md5=node.find('MD5')
                        fid=node.find('id')
                        cid=node.find('ChannelID')               
                        cdate=node.find('CatchDate')
                        node={'ChannelID':cid.text,'CatchDate':cdate.text,'md5':md5.text,'interface_id':fid.text}
                        channel_info[node['interface_id']] = node
                        #print(channel_info[node['ChannelID']])       
                except AttributeError as error:
                        print 'xml_parse.py AttributeError:',str(error)
                        return None
        print(channel_info)
        return channel_info                

if __name__=="__main__":
        parse_tvsou_updatelog()
        


