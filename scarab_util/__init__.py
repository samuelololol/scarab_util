#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

import argparse
from argparse import RawTextHelpFormatter
import textwrap

def main():
    #print "hello scarab_util"
    #pass
    description = """\
    CLI tool for scarab web framework.

    scarab -a generate 
    scarab -a show
    ...
    """
    usage = "usage: %prog -a {action} [parameters]"
    parser = argparse.ArgumentParser(
            description=textwrap.dedent(description),
            formatter_class=RawTextHelpFormatter)
            #description=description)
    args = parser.parse_args()

if __name__ == '__main__':
    main()
