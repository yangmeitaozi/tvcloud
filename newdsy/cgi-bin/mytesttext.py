import cgi
import cgitb
import yate

cgitb.enable()

print(yate.start_response())
print('<html><head>中文</head><body>')
print('''<form name="input" action="myedittt.py" method="post">
Username: 
<input type="text" name="user" />
<input type="submit" value="Submit" />
</form>''')
print('</body></html>')