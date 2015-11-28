#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import pytest
from scarab_util import ScarabCmd

@pytest.fixture(scope='function')
def generated_Page(request, ScarabRoute, ScarabRootPath):
    check_type = 'page'
    check_route = '/mypage.html'
    check_name = 'mypage'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route, '-n', check_name, '-r', ScarabRootPath]
    ScarabCmd(command_string)

    return {'check_type':     check_type,
            'check_name':     check_name,
            'check_route':    check_route,
            'command_string': command_string,
            }

def test_add_route(ScarabRoute, generated_Page):
    check_name = 'page_' + generated_Page['check_name']


    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_name in line:
                route_line = line
    #with open(ScarabRoute, 'r') as routepy:
    #    print routepy.read()
    print route_line
    assert route_line != ''

def test_add_page(ScarabRootPath, generated_Page):
    check_name = generated_Page['check_name']

    page_file_path = os.path.join(os.path.join(ScarabRootPath, 'pages'), check_name + '.py')
    print page_file_path
    assert True == os.path.isfile(page_file_path)

def test_add_service(ScarabRootPath, generated_Page):
    check_name = generated_Page['check_name']

    service_file_path = os.path.join(os.path.join(ScarabRootPath, 'services'), check_name + '_p.py')
    print service_file_path
    assert True == os.path.isfile(service_file_path)

def test_add_template(ScarabRootPath, generated_Page):
    check_name = generated_Page['check_name']
    check_route = generated_Page['check_route']

    templates_folder = os.path.join(ScarabRootPath, 'templates')
    template_file_path = os.path.join(templates_folder, check_name + '.jinja2')
    print 'filename: %s ' % template_file_path
    print template_file_path
    assert True == os.path.isfile(template_file_path)

    error_uri = "''%s''" % check_route
    with open(template_file_path, 'r') as f:
        assert error_uri not in f.read()

def test_add_page_test(ScarabRootPath, generated_Page):
    check_name = generated_Page['check_name']

    test_file_path = os.path.join(os.path.join(ScarabRootPath, 'test'), 'page')
    page_test_file_path = os.path.join(test_file_path, 'test_page_' + check_name + '.py')
    print page_test_file_path
    assert True == os.path.isfile(page_test_file_path)

