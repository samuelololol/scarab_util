#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 21, 2015 '
__author__= 'samuel'

import os
from scarab_util.utils.fileOp import InsertAbove
from scarab_util.utils.fileOp import InsertUnder
from scarab_util.utils.fileOp import AppendAbove
from scarab_util.utils.fileOp import AppendUnder


def add_new_initial_script(folder_root_path, name):
    print 'Generating DB initial scripts ... ',
    script_folder = os.path.join(folder_root_path, 'scripts')
    initscript_file_path = os.path.join(script_folder, 'initializedb.py')
    if not os.path.isfile(initscript_file_path):
        print 'fail, "%s" does not exist.' % initscript_file_path
        return False
    model_classname = name[0].upper() + name[1:].lower() + '_TB'
    check_name = model_classname + '('
    with open(initscript_file_path, 'r') as f:
        for line in f.readlines():
            if check_name in line:
                print 'fail, script for model("%s") already exist.' % model_classname
                return False

    # add import
    to_match_string = 'from ..models.'
    to_add_string_list = [
            "from ..models.%s import %s\n" % (name, model_classname),
        ]
    AppendUnder(initscript_file_path, to_add_string_list, to_match_string,
                before=["def "])

    # add instance
    to_match_string = 'DBSession.'
    to_add_string_list = [
         "#add initial script to %s\n" % model_classname,
         "#----\n",
         "#model = %s(%s_name=u'a_uniq_name',\n" % (model_classname, name),
         "#           description=u'a brief description',\n",
         "#          )\n",
         "#DBSession.add(model)\n",
         "#DBSession.flush()\n",
        ]
    AppendUnder(initscript_file_path, to_add_string_list, to_match_string,
                after=["with transaction", "def initialization("],
                before=["def main("])
    print 'done'
    return True

