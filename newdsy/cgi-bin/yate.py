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
    return('<p></p><center><input type=submit value="' + submit_msg + '"></center></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + str(rb_value[0]) + '"/> ' + rb_value[1] + '<br />')

def checked_radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + str(rb_value[0]) + '" checked="checked"/> ' + rb_value[1] + '<br />')

    
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

def start_table(tb_width, tb_height="100%", tb_border="0", tb_bgcolor='white', tb_background=''):
    return ('<table width="' + tb_width + '" cellspacing="1" cellpadding="2" border="' + tb_border + '" bgcorlor="' + tb_bgcolor + '" background="' + tb_background + '">')

def tb_caption(tb_caption):
    return ('<caption>' + tb_caption + '</caption>')

def tb_header(items):
    u_string = '<tr>'
    for item in items:
        u_string += '<th>' + item + '</th>'
    u_string += '</tr>'
    return(u_string)

def tb_data(items):
    u_string = '<tr>'
    for item in items:
        u_string += '<td>'
        if isinstance(item, int):
            u_string += str(item)
        else:
            u_string += item
        u_string += '</td>'
    u_string += '</tr>'
    return(u_string)

def end_table():
    return('</table>')


def select(name):
    return('<select name="'+ name +'" >')
    #return(' <td align="center" class="td_bg" width="25%" height="15" id="obj"><select name="'+ name +'" id="'+ name +'">')

def select_addr(name):
    #return('<select name="'+ name +'" >')
    return(' <td align="center" class="td_bg" width="25%" height="15" id="obj"><select id="'+ name +'" name="'+ name +'"onchange="showUser(this.value)" >')

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

def select_option(items):
    link_string = '<option value=''>&nbsp;&nbsp;</option>'
    for key in items:
        link_string += '<option value="' + str(key[0]) + '" >' + key[1]+'</option>'        
        
    return(link_string)

def select_optione_with_selected(item,opselect=False):
    
    if opselect:
        link_string = '<option value="'+str(item[0])+'" selected="selected">' + item[1] + '</option>'
        return(link_string)
    else:
        link_string = '<option value=''>&nbsp;&nbsp;</option>'
        link_string += '<option value="' + str(item[0]) + '" >' + item[1]+'</option>' 
        return(link_string)
    
def do_table(items, channel_offline=True):
    fn = BASE_DIR
    if channel_offline:
        fn += "/templates/table_offline.html"
    else:
        fn += "/templates/normal_table.html"
    with open(fn) as tt:
        tt_text = tt.read()
    #    print(tt_text)
     #   print(items)
        tb = Template(tt_text)           
        return(tb.substitute(channel_id=items[0],channel_name=items[1], channel_storagepath=items[2],publish_status=items[3]))

def do_operationtable(items):
    fn = BASE_DIR
    fn += "/templates/operationtable.html"
    with open(fn) as tt:
        tt_text = tt.read()    
        tb = Template(tt_text)           
        return(tb.substitute(channel_id=items[0],channel_name=items[1]))
        
def checked_operationtable(items):
    fn = BASE_DIR
    fn += "/templates/checkedOperationTable.html"
    with open(fn) as tt:
        tt_text = tt.read()    
        tb = Template(tt_text)           
        return(tb.substitute(channel_id=items[0],channel_name=items[1]))    
    
def do_normal_table(key,cn,si,sp,ss):
    fn = BASE_DIR + '/templates/normal_table.html'
    with open(fn) as tt:
        tt_text = tt.read()
        tb = Template(tt_text)           
        return(tb.substitute(chid=key,cname=cn,serverip=si,storagepath=sp,status=ss))   

def do_table_head():
    fn = BASE_DIR + '/templates/edit.html'
    with open(fn, encoding='utf-8') as tf:
        tf_text = tf.read()
        return(tf_text.encode('utf-8'))
    
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
    with open(fn, encoding='utf-8') as hf:
        hf_text = hf.read().encode('utf-8')
        hfs = Template(hf_text)
        return(hfs.substitute())
    
def render_publish(urls):
    fn = BASE_DIR + '/templates/fabu.html'
    with open(fn) as ff:
        ff_text = ff.read()
        fs = Template(ff_text)
        return(fs.substitute(the_url=urls))
    
def render_addrpublish(urls):
    fn = BASE_DIR + '/templates/addrpublish.html'
    with open(fn, encoding='utf-8') as ff:
        ff_text = ff.read().encode('utf-8')
        fs = Template(ff_text)
        return(fs.substitute(the_url=urls))
    
def render_edit():
    fn = BASE_DIR + '/templates/bianji.html'
    with open(fn) as bf:
        bf_text = bf.read()
    return bf_text
              
def render_temp():
    fn = BASE_DIR + '/templates/index.html'
    with open(fn, encoding='utf-8') as tt:
        tt_text = tt.read()
    return tt_text
    
def render_temp_left():
    fn = BASE_DIR + '/templates/left.html'
    with open(fn) as tt:
        tt_text = tt.read()
    return tt_text
    
def render_temp_top(head):
    fn = BASE_DIR + '/templates/top.html'
    with open(fn) as tt:
        tt_text = tt.read()
    header = Template(tt_text)
    return(header.substitute(name=head))

def render_temp_right():
    fn = BASE_DIR + '/templates/right.html'
    with open(fn, encoding='utf-8') as fd:
        tt_text = fd.read()
        
    return tt_text

def generata_data():
    fn = BASE_DIR + '/templates/ajaxmysql.html'
    with open(fn, encoding='utf-8') as tt:
        tt_text = tt.read()
    return tt_text

'''
With a simple <a> element to show links
'''
def gen_left(the_links):
    fn = BASE_DIR + '/templates/left.html'
    with open(fn) as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<p><a href="' + key[1] + '" target="main">' + key[0] + '</a></p>'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

'''
with js,<ul> <li> <a> to show a list of links
'''
def gen_left_ul(*args):
    fn = BASE_DIR + '/templates/left_li.html'
    with open(fn) as footf:
        foot_text = footf.read()
    link_string = ''
    #sub_strings = ''
    for item in args:
        listname = item['listname']
        elementId = item['elementId']
        the_links = item['the_links']
        jsfun = "showHide(this,'"+elementId+"');"
        link_string += '<li><a href="#" onclick="'+jsfun+'">'+listname+'</a>'
        link_string += '<ul id="'+elementId+'" style="display: block;">'
        for key in the_links:
            link_string += '<li><a href="' + key[1] + '" target="main">' + key[0] + '</a></li>'
        link_string += '</ul></li>'
        #sub_strings += link_string
        #link_string = ''
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_div(classname):
    return("<div class='"+classname+"' align='center'>")

def end_div():
    return("</div>")

def start_row():
    return('<tr><td>')

def end_row():
    return('</td></tr>')   

def start_td():
    return('<td>')

def end_td():
    return('</td>')

def start_tr():
    return('<tr>')

def end_tr():
    return('</tr>')

def input_text(name,value):
    return('<input type="text" name="'+name+'" value="'+value+'" />')


def start_select_onblur(name,myid,fname):
    return("<select name='"+name+"' id='"+myid+"' onblur='"+fname+"'>")

def render_guidepage_header(titles,head,url,formname):
    fn = BASE_DIR
    fn += "/templates/guidepageHeader.html"
    with open(fn) as tt:
        tt_text = tt.read()  
        tt = Template(tt_text)
        return(tt.substitute(title=titles,h=head,furl=url,alias=formname))
        
        
def render_guidepage_form(n1,n2):
    fn = BASE_DIR
    fn += "/templates/guidepageform.html"
    with open(fn) as tt:
        tt_text = tt.read()  
        tt = Template(tt_text)
        return(tt.substitute(appname=n1,logo=n2))
    
def select_id_name(name,myid):
    return('<select name="'+name+'" id="'+myid+'">')

def rend_guidepage_end(value):
    fn = BASE_DIR
    fn += "/templates/guidepageEnd.html"
    with open(fn) as tt:
        tt_text = tt.read()  
        tt = Template(tt_text)
        return(tt.substitute(subvalue=value))    