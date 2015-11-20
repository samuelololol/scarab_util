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
        usage = """scarab <command> [<args>]

        The available commands are:
        generate  Generate API server component
        show      Show API server related status
        """
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                usage=usage,
                )
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        return getattr(self, args.command)()

    def generate(self):
        description='Generate API server component'
        usage = """scarab generate -t TYPE [<args>]

        The available TYPEs are:
        api         Add route, api, service, and test
        page        Add route, page, service, and test
        model       Add model, initial script, and test
        """

        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                usage=usage,
                )

        parser.add_argument('-t', '--type',
                            required=True,
                            type=str,
                            choices=['api', 'page', 'model'],
                            help='component type')
        args = parser.parse_args(sys.argv[2:])
        print args



if __name__ == '__main__':
    main()
    
#deprecated
#def main():
    #description = "CLI tool for scarab web framework"
    #usage = """scarab <command> [<args>]

    #The available commands are:
    #generate  Generate API server component
    #show      Show API server related status
    #"""

    ## top-level parser
    #parser = argparse.ArgumentParser(
    #        description=textwrap.dedent(description),
    #        formatter_class=RawTextHelpFormatter,
    #        usage=usage)

    #subparsers = parser.add_subparsers(help='sub-command help')

    ## generate command
    #generate_parser = subparsers.add_parser('generate', help='generate help')
    #generate_parser.add_argument(
    #        '-t', '--type',
    #        required=True,
    #        type=str,
    #        choices=['api','page','service','model'],
    #        help='component type')

    #args = parser.parse_args()
    #print args
