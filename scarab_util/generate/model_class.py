#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2

def add_new_model(folder_root_path, name, filename):
    print 'Generating model ... ',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        Model_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'model_template.jinja2')
        template = templateEnv.get_template(Model_TEMPLATE_FILE)

        model_file_path = os.path.join(os.path.join(folder_root_path, 'models'), filename)
        variables = {'model_classname': name[0].upper() + name[1:].lower() + '_TB',
                     'name':      name,
                     'service_name':    name,
                    }
        outputText = template.render(variables)
        with open(model_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

