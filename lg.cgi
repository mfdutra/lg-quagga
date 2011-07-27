#!/usr/bin/python

import cgi
import json
import subprocess

form = cgi.FieldStorage()

print 'Content-type: application/json\n'

result = {}

vtysh = subprocess.Popen(('/usr/bin/vtysh', '-c', form.getvalue('command') + ' ' + form.getvalue('dst')), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = vtysh.communicate()

result['stdout'] = stdout
result['stderr'] = stderr

print json.dumps(result)
