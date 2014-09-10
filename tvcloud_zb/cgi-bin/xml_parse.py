#! /usr/bin/env python
#coding=utf-8
######################
# @author kenny
# @date 2014-07-15
######################
import urllib2
import xml.etree.ElementTree as Et

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
        except URLError:
                print 'URLError'
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

        channel_info={}
        for node in lst:
                md5=node.find('MD5')
                fid=node.find('id')
                cid=node.find('ChannelID')               
                cdate=node.find('CatchDate')
                node={'ChannelID':cid.text,'CatchDate':cdate.text,'md5':md5.text,'interface_id':fid.text}
                channel_info[node['ChannelID']] = node
                #print(channel_info[node['ChannelID']])
        print(channel_info)
        return channel_info

if __name__=="__main__":
        parse_tvsou_updatelog()
        


