#!/usr/bin/python3
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId,'r').read()
  description = description.replace('<', '&lt;')
  description = description.replace('>', '&gt;')
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action = '''
    <form action="process_delete.py" method="post">
      <input type="hidden" name="pageId" value="{}">
      <input type="submit" value="delete">
    </form>
  '''.format(pageId)
else:
  pageId = 'Welcome'
  description = 'Hello, web'
  update_link = ''
  delete_action = ''

print('''<!doctype html>
<html>
  <head>
    <title>Learn python</title>
    <meta charset="utf-8">
  </head>
</html>

<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="creat.py">creat</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
'''.format(title=pageId, 
           desc=description, 
           listStr=view.getlist(), 
           update_link=update_link, 
           delete_action=delete_action))