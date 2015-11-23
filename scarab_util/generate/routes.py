#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
from scarab_util.utils.fileOp import InsertAbove
from scarab_util.utils.fileOp import InsertUnder


def add_new_route(folder_root_path, route_name, path, api_version, prefix):
    print 'Generating route ... ',
    route_file_path = os.path.join(folder_root_path, 'routes.py')
    if not os.path.isfile(route_file_path):
        print 'fail, "%s" does not exist.' % route_file_path
        return False
    with open(route_file_path, 'r') as f:
        for line in f.readlines():
            if route_name in line:
                print 'fail, route_name("%s") already exist.' % route_name
                return False

    #prepare route_path
    if prefix != None:
        if prefix == '/':
            prefix = ''
        to_add_route_path = "'%s'" % (prefix + path)
    else:
        to_add_prefix = "api_prefix + '%s' + " % api_version
        to_add_route_path = to_add_prefix + "'%s'" % path

    to_match_string = 'config.add_route('
    to_add_string_list = [
        "config.add_route('%s',  %s) #scarab_util generated\n" % (route_name, to_add_route_path)
        ]
    InsertAbove(route_file_path, to_add_string_list, to_match_string)
    print 'done'
    return True

