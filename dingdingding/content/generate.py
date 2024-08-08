#!/usr/bin/env python

from Cheetah.Template import Template
import sys

t=Template(file='ding.tmpl')

www=sys.argv[1]
args=sys.argv[2:]

for fn in args:
  f=open(fn, 'r')
  t.content = f.read()
  if fn!="contact.html":
    t.extra_style = ""
  else:
    t.extra_style = \
     '<link rel="stylesheet" href="bounce.css" type="text/css" media="screen"/>'

  f.close()
  f=open(www+fn, 'w')
  f.write(str(t))
  f.close()

