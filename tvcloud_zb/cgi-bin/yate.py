# -*- conding: utf-8 -*-
#!/usr/bin/env python
#coding:utf-8
import cgitb
cgitb.enable()
from string import Template
import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    fn = BASE_DIR + '/templates/header.html'
    with open(fn) as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    fn = BASE_DIR + '/templates/footer.html'
    with open(fn) as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '">')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

    
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 

def select(name):
    #return('<select name="'+ name +'" >')
    return(' <td align="center" class="td_bg" width="25%" height="15" id="obj"><select name="'+ name +'" >')

def end_select():
    return('</select>')


def select_list(items):
    link_string = '<center><option value=''>&nbsp;&nbsp;</option></center>'
    for key in items:
        #print(key)
        link_string += '<option value="' + items[key] + '">' + items[key]+'</option>'        
        
    return(link_string)

def select_list_new(items):
    link_string = '<center><option value=''>&nbsp;&nbsp;</option></center>'
    for key in items:
        #print(key)
        link_string += '<option value="' + str(key) + '">' + items[key]+'</option>'        
        
    return(link_string)

def select_list_n(items):
    link_string = ''
    for key in items:
        link_string += '<option value="' + str(key) + '">' + items[key]+'</option>'        
        
    return(link_string)

def do_table(key,cn,si,sp,ss):
    fn = BASE_DIR + '/templates/table.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tb = Template(tt_text)           
        return(tb.substitute(chid=key,cname=cn,serverip=si,storagepath=sp,status=ss))

def do_normal_table(key,cn,si,sp,ss):
    fn = BASE_DIR + '/templates/normal_table.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tb = Template(tt_text)           
        return(tb.substitute(chid=key,cname=cn,serverip=si,storagepath=sp,status=ss))   

def do_table_head():
    fn = BASE_DIR + '/templates/edit.html'
    with open(fn) as tf:
        tf_text = tf.read()
        thead = Template(tf_text)
        return(thead.safe_substitute())
    
def do_table_end(myapp,mydel,myres):
    fn = BASE_DIR + '/templates/table_end.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tb = Template(tt_text)  
    return(tb.substitute(url=myapp,delt=mydel,rest=myres))

def normal_table_end():
    return('</table></body></html>')

def submit():
    return('</table> <center> <input type=submit value=add ></center></form>')

def checkboxes(the_links):
    links = ''
    for key in the_links:
        links += '<input type="checkbox" name="'+str(the_links[key][0])+\
                 '"\value="'+str(the_links[key][0]) +'">'+ the_links[key][1] +'</input> <br />'
    return(links)

def render_home():
    fn = BASE_DIR + '/templates1/index.html'
    with open(fn) as hf:
        hf_text = hf.read()
        hfs = Template(hf_text)
        return(hfs.substitute())
    
def render_publish():
    fn = BASE_DIR + '/templates/fabu.html'
    with open(fn) as ff:
        ff_text = ff.read()
        fs = Template(ff_text)
        return(fs.substitute())
    
def render_addrpublish():
    fn = BASE_DIR + '/templates/addrpublish.html'
    with open(fn) as ff:
        ff_text = ff.read()
        fs = Template(ff_text)
        return(fs.substitute())
    
def render_edit():
    fn = BASE_DIR + '/templates/bianji.html'
    with open(fn) as bf:
        bf_text = bf.read()
        bs = Template(bf_text)
        return(bs.substitute())
              
def render_temp():
    fn = BASE_DIR + '/temp/index.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tts = Template(tt_text)
        return ( tts.substitute())
def render_temp_left():
    fn = BASE_DIR + '/temp/left.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tts = Template(tt_text)
        return ( tts.substitute())
def render_temp_top():
    fn = BASE_DIR + '/temp/top.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tts = Template(tt_text)
        return ( tts.substitute())
def render_temp_right():
    fn = BASE_DIR + '/temp/right.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tts = Template(tt_text)
        return ( tts.substitute())
