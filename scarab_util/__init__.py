#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

import argparse
from argparse import RawTextHelpFormatter
import textwrap
import sys
import os

def main():
    ScarabCmd()

class ScarabCmd(object):
    def __init__(self):
        description = "CLI tool for scarab web framework"
        usage = """scarab <sub_command> [<args>]

        Available <sub_command> are:

        generate    Generate API server component
        show        Show API server related status
        """
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                usage=usage,
                )
        parser.add_argument('subcommand', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.subcommand):
            print 'Unrecognized subcommand'
            parser.print_help()
            exit(1)
        return getattr(self, args.subcommand)()

    def generate(self):
        description='Generate API server component'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type',
                            required=True,
                            type=str,
                            choices=['api', 'page', 'model'],
                            help='Component type')
        parser.add_argument('-p', '--path',
                            default='.',
                            type=str,
                            help='scarab root folder path')
        args = parser.parse_args(sys.argv[2:])
        args.path = os.path.abspath(args.path)
        print args

    def show(self):
        print """scarab show: under construction
        """


if __name__ == '__main__':
    main()

