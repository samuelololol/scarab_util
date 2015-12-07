#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import jinja2
import sys

def add_new_template(folder_root_path, name, page_filename, template_filename):
    print 'Generating template ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        #source
        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        Template_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'template_template.jinja2')
        template = templateEnv.get_template(Template_TEMPLATE_FILE)

        #target
        template_file_path = os.path.join(os.path.join(folder_root_path, 'templates'), template_filename)
        variables = {'name': name,
                     'page_filename': page_filename,
                     'template_filename': template_filename}
        outputText = template.render(variables)
        #for item in os.listdir(os.path.join(os.path.join(folder_root_path, 'templates'))):
        #    print item
        with open(template_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

