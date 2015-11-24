#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

from scarab_util.generate.routes import add_new_route
from scarab_util.generate.api_class import add_new_api
from scarab_util.generate.api_test_class import add_new_api_test
from scarab_util.generate.service_class import add_new_service

from scarab_util.generate.model_class import add_new_model
from scarab_util.generate.initial_scripts import add_new_initial_script
from scarab_util.generate.model_test_class import add_new_model_test

def generate_api(folder_root_path, name, path, version=1, prefix=None):
    route_name = ''
    if name[0:4] != 'api_':
        route_name = 'api_%s' % name
    if path[0] != '/':
        path = '/' + path
    if prefix==None and version==None:
        version = 1
    if prefix != None and prefix[0] != '/':
        prefix = '/' + prefix
    file_name = name + '.py'
    test_file_name = 'test_' + file_name

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
                                route_path=route_path, prefix=prefix)
    if success:
        success = add_new_api(folder_root_path, api_name=name,
                              route_name=route_name, file_name=file_name,
                              )
    if success:
        success = add_new_service(folder_root_path, service_name=name,
                                  file_name=file_name)
    if success:
        success = add_new_api_test(folder_root_path, api_name=name,
                                   route_path=route_path,
                                   route_name=route_name,
                                   file_name=test_file_name,
                                   )
    return success

def generate_model(folder_root_path, name):
    file_name = name + '.py'
    test_file_name = 'test_' + file_name

    success = True
    if success:
        success = add_new_model(folder_root_path, model_name=name,
                                file_name=file_name)
    if success:
        success = add_new_initial_script(folder_root_path, model_name=name)
    if success:
        success = add_new_model_test(folder_root_path, model_name=name,
                                     file_name=test_file_name)
    return success

