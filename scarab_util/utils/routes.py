#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 13, 2014 '
__author__= 'samuel'

api_prefix = '/api/v'
api_version = 1

def api_routes(config):
    #apis
    <<<<<<<
    right here
    <<<<<<<
    config.add_route('api_login',  api_prefix + str(api_version) + '/login')
    config.add_route('api_logout', api_prefix + str(api_version) + '/logout')

    #static at bottom
    config.add_static_view('static', 'static', cache_max_age=3600)

    #pages
    config.add_route('scarab.page_login', 'login')
    config.add_route('home', '/')


