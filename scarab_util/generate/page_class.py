#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2

def add_new_page(folder_root_path, page_name, route_name, filename, template_filename):
    print 'Generating page ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        Page_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'page_template.jinja2')
        template = templateEnv.get_template(Page_TEMPLATE_FILE)

        page_file_path = os.path.join(os.path.join(folder_root_path, 'pages'), filename)
        variables = {'page_classname': page_name[0].upper() + page_name[1:].lower() + 'Page',
                     'service_name': page_name + '_p',
                     'route_name': route_name,
                     'template_filename': template_filename,
                     'page_name':page_name,
                     'page_filename': filename,
                    }
        outputText = template.render(variables)
        with open(page_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

