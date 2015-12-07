#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#__date__= 'Dec 07, 2015 '
#__author__= 'samuel'

import os
import pytest

from scarab_util import ScarabCmd

@pytest.fixture(scope='function')
def generated_API(request, ScarabRoute, ScarabRootPath):
    check_type = 'async_api'
    check_route = '/myapi'
    check_name = 'test'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    return {'check_type': check_type,
            'check_route': check_route,
            'check_name': check_name,
            'command_string': command_string,
            }

@pytest.mark.devini
def test_add_celery_section_in_development(ScarabRootPath, generated_API):
    outer_foler = os.path.dirname(ScarabRootPath)
    dev_ini_path = os.path.join(outer_foler, 'development.ini')

    check_section = '[celery]'
    section_line = ''
    with open(dev_ini_path, 'r') as devf:
        for line in devf.readlines():
            if check_section in line:
                section_line = line
    assert section_line != ''

def test_add_route(ScarabRoute, generated_API):
    check_route = generated_API['check_route']
    check_name = generated_API['check_name']
    check_name = "async_api_" + check_name

    #check route_path
    print 'check_route: %s' % check_route
    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_route in line:
                route_line = line
    assert route_line != ''
    print 'check route_path: %s' % route_line

    #check route_name
    print 'check_name: %s' % check_name
    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_name in line:
                route_line = line
    assert route_line != ''
    print 'check route_name: %s' % route_line

def test_add_api(ScarabRootPath, generated_API):
    check_name = 'async_' + generated_API['check_name']

    api_file_path = os.path.join(os.path.join(ScarabRootPath, 'async_apis'), check_name + '.py')
    print api_file_path
    assert True == os.path.isfile(api_file_path)
    #with open(api_file_path, 'r') as f:
    #    print f.read()

def test_add_service(ScarabRootPath, generated_API):
    #check service file
    check_name = generated_API['check_name']

    service_file_path = os.path.join(os.path.join(ScarabRootPath, 'services'), check_name + '.py')
    print service_file_path
    assert True == os.path.isfile(service_file_path)

    #check celery broke function exist
    celery_exp = 'app.send_task('
    celery_line = ''
    with open(service_file_path, 'r') as sfile:
        for line in sfile.xreadlines():
            if celery_exp in line:
                celery_line = line
    assert celery_line != ''
    with open(service_file_path, 'r') as f:
        print f.read()

#def test_add_api_test(ScarabRootPath, generated_API):
#    check_name = generated_API['check_name']
#
#    test_file_path = os.path.join(os.path.join(ScarabRootPath, 'test'), 'api')
#    api_test_file_path = os.path.join(test_file_path, 'test_api_' + check_name + '.py')
#    print api_test_file_path
#    assert True == os.path.isfile(api_test_file_path)
#
