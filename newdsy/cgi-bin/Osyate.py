
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')


def addOms():
    with open('templates/addOms.html',encoding='utf-8') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute())

def sub_form_addOsName(name):
    with open('templates/puboperation.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.substitute(actionname=name))

def include_header(ms,jsurl):
    with open('templates/header_os.html') as headf:
        head_text = headf.read()
        header = Template(head_text)
        return(header.substitute(title=ms,jsUrl=jsurl))
    
def include_footer():
    with open('templates/footer.html',encoding='utf-8') as footf:
        foot_text = footf.read()       
    return(foot_text)

def include_link(the_links):
    link_string = ''
    for key in the_links:
        link_string = '<a href="' + the_links[key] + '">'+ key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    return(link_string)


def start_form(the_url, form_type="POST",fid=None):
    return('<form action="' + the_url + '" method="' + form_type + '" id="'+fid+'">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '">')


def sub_option(items):
    link_string = ''#'<center><option value=''>&nbsp;&nbsp;</option></center>'
    for key in items:
        #print(key)
        link_string += '<option value="' + str(key) + '">' + items[key]+'</option>'        
        
    return(link_string)

def sub_pubend():
    with open('templates/pubend.html',encoding='utf-8') as fn:
        fn_text = fn.read()
    fn_sub = Template(fn_text)
    return(fn_sub.substitute())

def sub_pubend_next():
    with open('templates/pubend_next.html',encoding='utf-8') as fn:
        fn_text = fn.read()
    fn_sub = Template(fn_text)
    return(fn_sub.substitute())

'''
For editOsname.py
'''
def osn_t1(title):
    with open('templates/editOsname-1.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(header=title))    
    
def osn_t2(name,nid,status):
    with open('templates/editOsname-2.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(osname=name,spid=nid,statusid=status))    
    
def osn_t3(myurl):
    with open('templates/editOsname-3.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(url=myurl)) 
    
'''
For editUrl.py
'''
def url_t1():
    with open('templates/editUrl-1.html',encoding='utf-9=8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute()) 
    
    
def url_t2(d1,d2,d3,d4,d5):
    with open('templates/editUrl-2.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(spid=d1,osname=d2,ip=d3,path=d4,port=d5)) 
    
def url_t3(name):
    with open('templates/editUrl-3.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(actionname=name)) 
    
'''
For editMac.py
'''    
def mac_t1():
    with open('templates/editMac-1.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute())     
    
    
def mac_t2(d1,d2,d3,d4):
    with open('templates/editMac-2.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(mixid=d1,osname=d2,mac1=d3,mac2=d4))   
    
def mac_t3(myurl):
    with open('templates/editMac-3.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(url=myurl))   
    
    
'''
#2014-9-28
'''    

'''
#Print headline H2
'''
def print_h2(title):
    return('<center><h2>"'+title+'"</h2></center>')

'''
#Print words
'''
def print_paragraph(content):
    return('<p align="center">"'+content+'"</p>')

'''
#Edit a <div> element
'''
def start_div(divId,site):
    return('<div id="'+divId+'" align="'+site+'">')

def end_div():
    return('</div>')

'''
#Edit a table
'''

def start_table(classname,width,site):
    return('<table class="'+classname+'" width="'+width+'" align="'+site+'">')

def end_table():
    return('</table>')

def start_tr():
    return('<tr>')

def end_tr():
    return('</tr>')

def table_th(classname,site,ms):
    return('<th class="'+classname+'" align="'+site+'">'+ms+'</th>')

def table_td():
    return('<td class="'+classname+'" align="'+site+'">'+ms+'</td>')

def print_input(pid,ptyte,pname,pvalue):
    return('<input id="'+pid+'" type="'+ptype+'" name="'+pname+'" value="'+pvalue+'"/>')

def print_urlTable():
    with open('/templates/editUrl-2.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute()) 
        

    
def start_select_Epg(name):
    with open('templates/start_select_editEpgUrl.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(actionname=name)) 
        
        
def start_select_mac(name):
    with open('templates/start_select_mac.html',encoding='utf-8') as fn:
        fn_text = fn.read()
        fn_sub = Template(fn_text)
        return(fn_sub.safe_substitute(actionname=name)) 