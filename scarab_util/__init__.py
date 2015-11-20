#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

import argparse
from argparse import RawTextHelpFormatter
import textwrap

def main():
    description = """\
    CLI tool for scarab web framework.

    scarab generate 
    scarab show
    ...
    """
    #usage = "usage: %prog <command> [parameters]"
    # top-level parser
    parser = argparse.ArgumentParser(
            description=textwrap.dedent(description),
            formatter_class=RawTextHelpFormatter)

    subparsers = parser.add_subparsers(help='sub-command help')

    # generate command
    generate_parser = subparsers.add_parser('generate', help='generate help')
    generate_parser.add_argument(
            '-t', '--type',
            required=True,
            type=str,
            choices=['api','page','service','model'],
            help='component type')

    args = parser.parse_args()
    print args

if __name__ == '__main__':
    main()
