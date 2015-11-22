#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 22, 2015 '
__author__= 'samuel'

import os, errno

def create_folders(root_path, folders):
    for folder in folders:
        folder_path = os.path.join(root_path, folder)
        try:
            os.mkdir(folder_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(folder_path):
                pass
            else:
                raise


