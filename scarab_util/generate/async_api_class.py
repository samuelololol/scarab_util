#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import sys
import os
import jinja2
from scarab_util.utils import create_folders
from scarab_util.utils.fileOp import AppendBottom

def add_new_async_api(folder_root_path, name, route_name, filename):
    """
    add [celery] section in developement.ini
    """
    print 'Generating api(async) ... ',

    #check if [celery] section exist in development.ini and insert the [celery] section
    dev_ini_path = os.path.join(os.path.dirname(folder_root_path), 'development.ini')
    check_section = '[celery]'
    section_line = ''
    with open(dev_ini_path, 'r') as devf:
        for line in devf.readlines():
            if check_section in line:
                section_line = line
    if section_line == '':
        section_title_to_add = '[celery]\n'
        section_attributes_to_add = [
                'BROKER_URL = redis://localhost/1\n',
                '#CELERY_RESULT_BACKEND = redis://localhost/2'
                ]
        insert_text = []
        insert_text.append("\n")
        insert_text.extend(section_title_to_add)
        insert_text.extend(section_attributes_to_add)
        AppendBottom(dev_ini_path, insert_text)
    
    try:
        templateLoader = jinja2.FileSystemLoader(searchpath="/")
        templateEnv = jinja2.Environment(loader=templateLoader)

        TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
        API_TEMPLATE_FILE = os.path.join(TEMPLATE_FOLDER, 'async_api_template.jinja2')
        template = templateEnv.get_template(API_TEMPLATE_FILE)

        create_folders(folder_root_path, ['async_apis'])
        api_file_path = os.path.join(os.path.join(folder_root_path, 'async_apis'), filename)
        variables = {'api_classname': 'Async' + name[0].upper() + name[1:].lower() + 'API',
                     'name': name,
                     'service_name': name,
                     'route_name': route_name,
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

