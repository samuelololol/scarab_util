#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

from scarab_util.generate.routes import add_new_route
from scarab_util.generate.api_class import add_new_api
from scarab_util.generate.api_test_class import add_new_api_test
from scarab_util.generate.service_class import add_new_service

from scarab_util.generate.async_api_class import add_new_async_api
from scarab_util.generate.async_service_class import add_new_async_service

from scarab_util.generate.model_class import add_new_model
from scarab_util.generate.initial_scripts import add_new_initial_script
from scarab_util.generate.model_test_class import add_new_model_test

from scarab_util.generate.page_class import add_new_page
from scarab_util.generate.template_file import add_new_template
from scarab_util.generate.page_test_class import add_new_page_test

def generate_api(folder_root_path, name, path, version=1, prefix=None):
    """
    1. add route
    2. add api file
    3. add service file
    4. add api functional test file
    """
    route_name = ''
    if name[0:4] != 'api_':
        route_name = 'api_%s' % name
    if path[0] != '/':
        path = '/' + path
    if prefix==None and version==None:
        version = 1
    if prefix != None and prefix[0] != '/':
        prefix = '/' + prefix
    filename = name + '.py'
    test_filename = 'test_api_' + filename

    #prepare route_path
    if prefix != None:
        if prefix == '/':
            prefix = ''
        route_path = "'%s'" % (prefix + path)
    else:
        to_add_prefix = "api_prefix + '%s' + " % version
        route_path = to_add_prefix + "'%s'" % path

    success = True
    if success:
        success = add_new_route(folder_root_path, route_name=route_name,
                route_path=route_path, rtype='api')
    if success:
        success = add_new_api(folder_root_path, name=name, route_name=route_name,
                              filename=filename)
    if success:
        success = add_new_service(folder_root_path, name=name, filename=filename)
    if success:
        success = add_new_api_test(folder_root_path, name=name,
                                   route_path=route_path,
                                   route_name=route_name,
                                   filename=test_filename,
                                   api_version=version,
                                   )
    return success

def generate_async_api(folder_root_path, name, path, version=1, prefix=None):
    """
    1. add [celery] section in development.ini
      1.1) add at the bottom
    2. add route
    3. add async api file
      3.1) add at existing async folder or create async folder
    4. add service function
      4.1) add at existing service file or add at the bottom
    5. add api functional test file
      5.1) add at existing test api folder or create test api folder
    """
    route_name = ''
    if name[0:4] != 'async_api_':
        route_name = 'async_api_%s' % name
    if path[0] != '/':
        path = '/' + path
    if prefix==None and version==None:
        version = 1
    if prefix != None and prefix[0] != '/':
        prefix = '/' + prefix
    filename = 'async_' + name + '.py'
    service_filename = name + '.py'
    test_filename = 'test_async_api_' + name + '.py'

    #prepare route_path
    if prefix != None:
        if prefix == '/':
            prefix = ''
        route_path = "'%s'" % (prefix + path)
    else:
        to_add_prefix = "api_prefix + '%s' + " % version
        route_path = to_add_prefix + "'%s'" % path

    success = True
    if success:
        success = add_new_route(folder_root_path, route_name=route_name,
                route_path=route_path, rtype='api')
    if success:
        success = add_new_async_api(folder_root_path, name=name, route_name=route_name,
                              filename=filename)
    if success:
        success = add_new_async_service(folder_root_path, name=name, filename=service_filename)
    if success:
        success = add_new_api_test(folder_root_path, name=name,
                                   route_path=route_path,
                                   route_name=route_name,
                                   filename=test_filename,
                                   api_version=version,
                                   )
    return success

def generate_model(folder_root_path, name):
    """
    1. add model file
    2. add model test file
    """
    filename = name + '.py'
    test_filename = 'test_model_' + filename

    success = True
    if success:
        success = add_new_model(folder_root_path, name=name,
                                filename=filename)
    if success:
        success = add_new_initial_script(folder_root_path, name=name)
    if success:
        success = add_new_model_test(folder_root_path, name=name,
                                     filename=test_filename)
    return success

def generate_page(folder_root_path, path, name):
    """
    1. add route
    2. add page file
    2. add page template file
    4. add page functional test file
    """
    route_name = ''
    if name[0:4] != 'page_':
        route_name = 'scarab.page_%s' % name
    if path[0] != '/':
        path = '/' + path
    route_path = "'%s'" % path
    filename = name + '.py'
    service_name = name + '_p'
    service_filename = name + '_p.py'
    test_filename = 'test_page_' + filename
    template_filename = name + '.jinja2'

    success = True
    if success:
        success = add_new_route(folder_root_path, route_name=route_name,
                route_path=route_path, rtype='page')
    if success:
        success = add_new_page(folder_root_path, name=name, route_name=route_name,
                               filename=filename, template_filename=template_filename,
                               )
    if success:
        success = add_new_service(folder_root_path, name=name, filename=service_filename)
    if success:
        success = add_new_template(folder_root_path, name=name,
                                   page_filename=filename,
                                   template_filename=template_filename)
    if success:
        success = add_new_page_test(folder_root_path,
                                    name=name,
                                    route_path=route_path,
                                    route_name=route_name,
                                    filename=test_filename,
                                    )
    return success

