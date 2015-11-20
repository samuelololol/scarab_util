#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

from scarab_util.utils.fileOp import InsertAbove
from scarab_util.utils.fileOp import InsertAbove

def generate_api(folder_root_path, path, method, name, version):
    _add_new_route(folder_root_path, path=path, name=name, method=method,
            api_version=version)
    _add_new_api(folder_root_path, api_name=name, name=name, method=method,
            api_version=version)

def _add_new_route(folder_root_path, path, name, method, api_version):
    print 'new route'

def _add_new_api(folder_root_path, api_name, name, method, api_version):
    print 'new api'
    print 'folder_root_path: %s' % folder_root_path
    print 'api_name: %s' % api_name
    print 'name: %s' % name
    print 'method: %s' % method
    print 'api_version: %s' % api_version

def _add_new_service(folder_root_path, service_name):
    print 'new service'

def _add_new_model(folder_root_path, model_name):
    print 'new model'

