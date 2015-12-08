#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import jinja2
import sys
from service_class import add_new_service
from scarab_util.utils.fileOp import AppendBottom

def add_new_async_service(folder_root_path, name, filename):
    """
    check if service files exist
    1. yes, append broke function
    2. no, create and append broker function
    """
    service_file_path = os.path.join(os.path.join(folder_root_path, 'services'), filename)
    if not os.path.isfile(service_file_path):
        #1. add service file
        add_new_service(folder_root_path, name, filename)

    print 'Generating service(asnyc) ... ',
    #2. append broker function
    import_to_add = ['from pyramid_celery import celery_app as app\n']
    function_to_add = [
            "def %s_send_task(params):\n" % name,
            "     r = app.send_task('<task_name>', (params))\n",
            "     return r.id\n"]
    insert_text = []
    insert_text.append("\n")
    insert_text.extend(import_to_add)
    insert_text.append("\n")
    insert_text.extend(function_to_add)
    AppendBottom(service_file_path, insert_text)
    print 'done'
    return True

