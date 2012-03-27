#!/usr/bin/python
import os
import sys
import Tail

username = 'a.pachay'  #login and password on factory.ailove.ru
password = ''

employee = ['pachay', 308] #factory

if len(sys.argv) < 2:
    print 'Usage: %s project-name [<n>] [<remote file path>]' % sys.argv[0]
    print '<n>:                 number of lines'
    print '<remote file path>:  tmp/logs/prod.log by default'
    print "\n"
    print 'Available projects:'

    import xml.dom.minidom
    import Redmine
    from HTTP import *

    brw = Browser()
    brw.setCredentials(username, password)

    ProjectsByUserXml = xml.dom.minidom.parseString( brw.curl(Redmine.getProjectsByUser(employee[1])) )

    def getText(nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

    for project in ProjectsByUserXml.getElementsByTagName("project"):
        ProjectXml = xml.dom.minidom.parseString( brw.curl(Redmine.getProject(project.getAttribute("id"))) )
        print "    "+getText(ProjectXml.getElementsByTagName("identifier")[0].childNodes)

else:
    project_name = sys.argv[1]
    project_server_name = "%s.pro.ailove.ru" % project_name
    n = 20 if len(sys.argv)<3 else int(sys.argv[2])
    remote_file_path = 'tmp/logs/prod.log' if len(sys.argv)<4 else sys.argv[3]
    local_file_path = '/tmp/ftp_files/%s/%s' % (project_name, os.path.basename(remote_file_path))

    if not os.path.exists(os.path.dirname(local_file_path)):
        os.makedirs(os.path.dirname(local_file_path))

    try:
        from ftplib import FTP
        ftp = FTP(project_server_name)
        ftp.login("%s@%s" % (username, project_name), password)
        ftp.retrbinary("RETR %s" % remote_file_path, open(local_file_path, 'wb').write)
        ftp.quit()
    except:
        print "Error: file %s not found on server %s" % (remote_file_path, project_server_name)
        raise 

    print Tail.tail(local_file_path, n)
    os.remove(local_file_path)
