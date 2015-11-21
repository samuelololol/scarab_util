#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

from scarab_util.generate.routes import add_new_route
from scarab_util.generate.api_class import add_new_api
from scarab_util.generate.service_class import add_new_service
from scarab_util.generate.model_class import add_new_model

def generate_api(folder_root_path, name, method, path, version):
    route_name = ''
    if name[0:4] != 'api_':
        route_name = 'api_%s' % name

    success = True
    if success:
        success = add_new_route(folder_root_path, route_name=route_name, path=path, api_version=version)
    if success:
        success = add_new_api(folder_root_path, api_name=name, route_name=name, file_name=name,
            method=method, api_version=version)
    if success:
        success = add_new_service(folder_root_path, service_name=name)
    return success

