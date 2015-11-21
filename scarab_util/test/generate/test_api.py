#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import pytest
from scarab_util.test.common.mock_scarab import ScarabRootPath
from scarab_util.test.common.mock_scarab import ScarabRoute

from scarab_util import ScarabCmd

def test_add_route(ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_route in line:
                route_line = line
    print route_line
    assert route_line != ''

def test_add_api(ScarabRootPath, ScarabRoute):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)
    api_file_path = os.path.join(os.path.join(ScarabRootPath, 'apis'), check_name + '.py')
    print api_file_path
    assert True == os.path.isfile(api_file_path)
    with open(api_file_path, 'r') as f:
        print f.read()

