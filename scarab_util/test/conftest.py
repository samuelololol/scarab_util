#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 28, 2015 '
__author__= 'samuel'
import logging
FORMAT = "%(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().addHandler(logging.StreamHandler())

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

    dev_ini_path   = os.path.join(os.path.dirname(folder_name), 'development.ini')

    for folder in [apis_dir, services_dir, pages_dir, templates_dir, models_dir,
                   scripts_dir, test_dir, api_test_dir, model_test_dir]:
        os.mkdir(folder)

    open(dev_ini_path, 'a').close()

    def fin():
        shutil.rmtree(folder_name)
    request.addfinalizer(fin)
    return folder_name

@pytest.fixture(scope='function')
def ScarabRoute(ScarabRootPath, request):
    test_folder_path = os.path.dirname(__file__)
    resource_folder_path = os.path.join(test_folder_path, 'resource')
    route_file_path = os.path.join(resource_folder_path, 'routes.py')

    shutil.copy(route_file_path, ScarabRootPath)

    route_path = os.path.join(ScarabRootPath, 'routes.py')
    def fin():
        os.remove(route_path)
    request.addfinalizer(fin)
    return route_path

@pytest.fixture(scope='function')
def ScarabInitialScript(ScarabRootPath, request):
    test_folder_path = os.path.dirname(__file__)
    resource_folder_path = os.path.join(test_folder_path, 'resource')
    initscript_file_path = os.path.join(resource_folder_path, 'initializedb.py')
    script_folder = os.path.join(ScarabRootPath, 'scripts')

    shutil.copy(initscript_file_path, script_folder)

    initscript_path = os.path.join(script_folder, 'initializedb.py')
    def fin():
        #with open(initscript_path, 'r') as f:
        #    print f.read()
        os.remove(initscript_path)
    request.addfinalizer(fin)
    return initscript_path

