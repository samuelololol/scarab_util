#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2

def add_new_api(folder_root_path, api_name, route_name, file_name, method, api_version):
    print 'Generating api ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        API_TEMPLATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                'api_template.jinja2')
        template = templateEnv.get_template(API_TEMPLATE_FILE)

        api_file_path = os.path.join(os.path.join(folder_root_path, 'apis'), api_name + '.py')
        variables = {'api_classname': api_name[0].upper() + api_name[1:].lower() + 'API',
                     'api_name':api_name,
                     'service_name': api_name,
                     'route_name':route_name,
                    }
        outputText = template.render(variables)
        with open(api_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

