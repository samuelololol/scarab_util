#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import pytest
from scarab_util.test.common.mock_scarab import ScarabRootPath
from scarab_util.test.common.mock_scarab import ScarabRoute

from scarab_util import ScarabCmd

@pytest.fixture(scope='function')
def generated_API(request, ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    return {'check_type': check_type,
            'check_route': check_route,
            'check_name': check_name,
            'command_string': command_string
            }

def test_add_route(ScarabRoute, generated_API):
    check_route = generated_API['check_route']

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_route in line:
                route_line = line
    assert route_line != ''
    print route_line

def test_add_api(ScarabRootPath, generated_API):
    check_name = generated_API['check_name']

    api_file_path = os.path.join(os.path.join(ScarabRootPath, 'apis'), check_name + '.py')
    print api_file_path
    assert True == os.path.isfile(api_file_path)
    with open(api_file_path, 'r') as f:
        print f.read()

def test_add_service(ScarabRootPath, generated_API):
    check_name = generated_API['check_name']

    service_file_path = os.path.join(os.path.join(ScarabRootPath, 'services'), check_name + '.py')
    print service_file_path
    assert True == os.path.isfile(service_file_path)
    with open(service_file_path, 'r') as f:
        print f.read()

