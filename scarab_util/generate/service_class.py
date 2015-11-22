#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import jinja2
import sys

def add_new_service(folder_root_path, service_name, file_name):
    print 'Generating service ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        SERVICE_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'service_template.jinja2')
        template = templateEnv.get_template(SERVICE_TEMPLATE_FILE)

        service_file_path = os.path.join(os.path.join(folder_root_path, 'services'), file_name)
        variables = {'service_name': service_name}
        outputText = template.render(variables)
        with open(service_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

