#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import pytest
from scarab_util.test.common.mock_scarab import ScarabRootPath
from scarab_util.test.common.mock_scarab import ScarabRoute

from scarab_util import ScarabCmd

def test_add_route(ScarabRoute, ScarabRootPath):
    command_string = ['scarab', 'generate', '-t', 'api', '-p', '/myapi', '-n', 'test', '-r', ScarabRootPath]
    ScarabCmd(command_string)

    route_line = ''
    with open(ScarabRoute, 'r') as routepy:
        for line in routepy.readlines():
            if '/myapi' in line:
                route_line = line
    print route_line
    assert route_line != ''

