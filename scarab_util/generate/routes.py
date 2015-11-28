#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
from scarab_util.utils.fileOp import InsertAbove
from scarab_util.utils.fileOp import InsertUnder


def add_new_route(folder_root_path, route_name, route_path, rtype='api'):
    """
    api:
      - insert above to `config.add_route(`
      - insert as 1st `config.add_route`
    page:
      - or condition
          - insert above to `config.add_route('page_`
          - insert above to `config.add_route('home`
    """
    print 'Generating route(%s) ... ' % rtype,
    route_file_path = os.path.join(folder_root_path, 'routes.py')
    if not os.path.isfile(route_file_path):
        print 'fail, "%s" does not exist.' % route_file_path
        return False
    with open(route_file_path, 'r') as f:
        for line in f.readlines():
            if route_name in line:
                raise Exception('fail, route_name("%s") already exist.' % route_name)
    if rtype == 'api':
        to_match_string = 'config.add_route('
    elif rtype == 'page':
        to_match_string = []
        to_match_string.append("config.add_route('page_")
        to_match_string.append("config.add_route('home")

    to_add_string_list = [
        "config.add_route('%s',  %s) #scarab_util generated\n" % (route_name, route_path)
        ]
    InsertAbove(route_file_path, to_add_string_list, to_match_string)
    print 'done'
    return True

