#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2

from scarab_util.utils import create_folders

def add_new_api_test(folder_root_path, name, route_path, route_name, filename, api_version):
    print 'Generating api functional test script ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        API_TEST_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'api_test_template.jinja2')
        template = templateEnv.get_template(API_TEST_TEMPLATE_FILE)

        test_file_path = os.path.join(os.path.join(folder_root_path, 'test'), 'api')
        api_test_file_path = os.path.join(test_file_path, filename)

        variables = {'api_classname': name[0].upper() + name[1:].lower() + 'API',
                     'name':          name,
                     'path':          route_path,
                     'api_version':   api_version,
                    }
        outputText = template.render(variables)
        create_folders(os.path.join(folder_root_path, 'test'), ['api', 'model'])
        with open(api_test_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

