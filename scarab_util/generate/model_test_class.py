#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2

def add_new_model_test(folder_root_path, model_name, file_name):
    print 'Generating model functional test script ... (fake)',
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        MODEL_TEST_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'model_test_template.jinja2')
        template = templateEnv.get_template(MODEL_TEST_TEMPLATE_FILE)

        test_file_path = os.path.join(os.path.join(folder_root_path, 'test'), 'model')
        model_test_file_path = os.path.join(test_file_path, file_name)

        variables = {'model_classname':     model_name[0].upper() + model_name[1:].lower() + '_TB',
                     'model_name':          model_name,
                     'model_instance_name': 'A_' + model_name[0].upper() + model_name[1:].lower()
                    }
        outputText = template.render(variables)
        with open(model_test_file_path, 'wb') as f:
            f.write(outputText)
    except Exception, e:
        print 'fail'
        exp = sys.exc_info()[0]
        print exp
        print e
        return False
    print 'done'
    return True

