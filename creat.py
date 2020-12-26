#!/usr/bin/python3
# -*- coding: UTF-8 -*-
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId,'r').read()
else:
  pageId = 'Welcome'
  description = 'Hello, web'

print('''<!doctype html>
<html>
  <head>
    <title>learn python</title>
    <meta charset="utf-8">
  </head>
</html>

<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="creat.py">creat</a>
  <form action="process_creat.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
'''.format(title=pageId, desc=description, listStr=view.getlist()))