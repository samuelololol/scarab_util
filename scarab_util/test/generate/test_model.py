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
def generated_Model(request, ScarabRoute, ScarabRootPath):
    check_type = 'model'
    check_name = 'test'
    command_string = ['scarab', 'generate', '-t', check_type, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    return {'check_type': check_type,
            'check_name': check_name,
            'command_string': command_string,
            }

#add model
#------------------
def test_add_model(ScarabRootPath, generated_Model):
    check_name = generated_Model['check_name']

    model_file_path = os.path.join(os.path.join(ScarabRootPath, 'models'), check_name + '.py')
    print model_file_path
    assert True == os.path.isfile(model_file_path)
    with open(model_file_path, 'r') as f:
        print f.read()

#add initial script
#------------------
#def test_add_route(ScarabRoute, generated_Model):
#    check_route = generated_Model['check_name']
#
#    route_line = ''
#    with open(ScarabRoute, 'r') as routepy:
#        for line in routepy.readlines():
#            if check_route in line:
#                route_line = line
#    assert route_line != ''
#    print route_line

#add model test
#--------------
#def test_add_model_test(ScarabRootPath, generated_Model):
#    check_name = generated_Model['check_name']
#
#    test_file_path = os.path.join(os.path.join(ScarabRootPath, 'test'), 'model')
#    model_test_file_path = os.path.join(test_file_path, 'test_' + check_name + '.py')
#    print model_test_file_path
#    assert True == os.path.isfile(model_test_file_path)

