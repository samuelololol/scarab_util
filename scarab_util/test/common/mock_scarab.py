#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import pytest
import tempfile
import shutil
import os


@pytest.fixture(scope='function')
def ScarabRootPath(request):
    folder_name = tempfile.mkdtemp()

    apis_dir       = os.path.join(folder_name, 'apis')
    services_dir   = os.path.join(folder_name, 'services')
    pages_dir      = os.path.join(folder_name, 'pages')
    templates_dir  = os.path.join(folder_name, 'templates')
    models_dir     = os.path.join(folder_name, 'models')
    scripts_dir    = os.path.join(folder_name, 'scripts')
    test_dir       = os.path.join(folder_name, 'test')
    api_test_dir   = os.path.join(test_dir, 'api')
    model_test_dir = os.path.join(test_dir, 'model')

    for folder in [apis_dir, services_dir, pages_dir, templates_dir, models_dir,
                   scripts_dir, test_dir, api_test_dir, model_test_dir]:
        os.mkdir(folder)

    def fin():
        shutil.rmtree(folder_name)
    request.addfinalizer(fin)
    return folder_name

@pytest.fixture(scope='function')
def ScarabRoute(ScarabRootPath, request):
    common_folder_path = os.path.dirname(__file__)
    test_folder_path = os.path.dirname(common_folder_path)
    resource_folder_path = os.path.join(test_folder_path, 'resource')
    route_file_path = os.path.join(resource_folder_path, 'routes.py')
    shutil.copy(route_file_path, ScarabRootPath)
    route_path = os.path.join(ScarabRootPath, 'routes.py')
    def fin():
        os.remove(route_path)
    request.addfinalizer(fin)
    return route_path

