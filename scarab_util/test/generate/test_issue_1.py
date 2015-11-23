#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
import pytest
from scarab_util.test.common.mock_scarab import ScarabRootPath
from scarab_util.test.common.mock_scarab import ScarabRoute
import random

from scarab_util import ScarabCmd

def test_version_argument(ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    check_version = '%s' % str(random.randint(0,9))
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route,
            '-n', check_name, '-r', ScarabRootPath, '--version', check_version]
    ScarabCmd(command_string)

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if "+ '%s'" % check_version in line:
                route_line = line
                break
    assert route_line != ''
    print route_line

def test_prefix_argument(ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    check_prefix = 'my_%s_prefix' % str(random.randint(0,9))
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route,
            '-n', check_name, '-r', ScarabRootPath, '--prefix', check_prefix]
    ScarabCmd(command_string)

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if check_prefix in line:
                route_line = line
                break
    assert route_line != ''
    print route_line

def test_root_as_prefix_argument(ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    check_prefix = '/'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route,
            '-n', check_name, '-r', ScarabRootPath,'--prefix', check_prefix,
            ]
    print 'before parsine: %s' % ''.join(command_string)
    ScarabCmd(command_string)

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if '  \'//' in line:
                route_line = line
                break
    assert route_line == ''
    print route_line

def test_both_argument(ScarabRoute, ScarabRootPath):
    check_type = 'api'
    check_route = '/myapi'
    check_name = 'test'
    check_prefix = 'myprefix'
    command_string = ['scarab', 'generate', '-t', check_type, '-p', check_route,
            '-n', check_name, '-r', ScarabRootPath, '--version', '3', '--prefix',
            check_prefix,
            ]

    with pytest.raises(SystemExit) as excinfo:
        ScarabCmd(command_string)

