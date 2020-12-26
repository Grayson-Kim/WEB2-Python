#!/usr/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

os.rename('data/'+pageId, 'data/'+title)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
