#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import pytest
from scarab_util.test.common.mock_scarab import ScarabRootPath
from scarab_util.test.common.mock_scarab import ScarabRoute
from scarab_util.test.common.mock_scarab import ScarabInitialScript

from scarab_util import ScarabCmd

@pytest.fixture(scope='function')
def generated_Model(request, ScarabRoute, ScarabRootPath, ScarabInitialScript):
    check_type = 'model'
    check_name = 'company'
    command_string = ['scarab', 'generate', '-t', check_type, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    return {'check_type': check_type,
            'check_name': check_name,
            'command_string': command_string,
            'root_path': ScarabRootPath,
            'init_script_path': ScarabInitialScript,
            }

def test_add_model(generated_Model):
    check_name = generated_Model['check_name']
    root_path = generated_Model['root_path']

    model_file_path = os.path.join(os.path.join(root_path, 'models'), check_name + '.py')
    #with open(model_file_path, 'r') as f:
    #    print f.read()
    print model_file_path
    assert True == os.path.isfile(model_file_path)

def test_add_initial_script(generated_Model):
    check_name = generated_Model['check_name']
    init_script_path = generated_Model['init_script_path']
    model_classname = check_name[0].upper() + check_name[1:].lower() + '_TB'
    check_initial_script = model_classname + '('

    initial_script_line = ''
    with open(init_script_path, 'r') as initial_scriptpy:
        for line in initial_scriptpy.readlines():
            if check_initial_script in line:
                initial_script_line = line
    print initial_script_line
    #with open(init_script_path, 'r') as f:
    #    print f.read()
    assert initial_script_line != ''

def test_add_model_test(generated_Model):
    check_name = generated_Model['check_name']
    root_path = generated_Model['root_path']

    test_file_path = os.path.join(os.path.join(root_path, 'test'), 'model')
    model_test_file_path = os.path.join(test_file_path, 'test_' + check_name + '.py')
    print model_test_file_path
    #with open(model_test_file_path, 'r') as f:
    #    print f.read()
    assert True == os.path.isfile(model_test_file_path)

