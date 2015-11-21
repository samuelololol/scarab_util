#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

from scarab_util.generate.routes import add_new_route

def generate_api(folder_root_path, name, method, path, version):
    route_name = ''
    if name[0:4] != 'api_':
        route_name = 'api_%s' % name

    success = True
    if success:
        success = add_new_route(folder_root_path, route_name=route_name, path=path, api_version=version)
    if success:
        success = _add_new_api(folder_root_path, api_name=name, route_name=name, file_name=name,
            method=method, api_version=version)
    return success

def _add_new_api(folder_root_path, api_name, route_name, file_name, method, api_version):
    print 'Generating api ...(fake) ',
    #print 'new api'
    #print 'folder_root_path: %s' % folder_root_path
    #print 'api_name: %s' % api_name
    #print 'route_name: %s' % route_name
    #print 'file_name: %s' % file_name
    #print 'method: %s' % method
    #print 'api_version: %s' % api_version
    print 'done'
    return True

def _add_new_service(folder_root_path, service_name):
    print 'new service'

def _add_new_model(folder_root_path, model_name):
    print 'new model'

