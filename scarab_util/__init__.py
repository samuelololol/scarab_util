#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'

import argparse
from argparse import RawTextHelpFormatter
import textwrap
import sys
import os

import generate

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
        description='Generate scarab component'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type',
                            required=True,
                            action=GenerateAction,
                            type=str,
                            choices=['api', 'page', 'model'],
                            help='Component type')

        args, others = parser.parse_known_args(sys.argv[2:])
        return getattr(self, args.type)()

    def show(self):
        print """scarab show: under construction
        """

    def _generate_api(self):
        description='Generate scarab api component'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type', type=str,
                            required=True,
                            choices=['api'],
                            help='Component type')
        parser.add_argument('-p', '--path', type=str,
                            default='',
                            help='API URI')
        parser.add_argument('-n', '--name', type=str,
                            required=True,
                            help='API name')
        parser.add_argument('-m', '--method', type=str,
                            default='GET',
                            choices=['GET', 'POST', 'PUT', 'DELETE', 'ALL4'],
                            help='API request method')
        parser.add_argument('-v', '--version', type=str,
                            default='1',
                            help='API version')
        parser.add_argument('-r', '--rootpath', type=str,
                            default='.',
                            help='scarab root folder path')

        args = parser.parse_args(sys.argv[2:])

        #default values
        args.rootpath = os.path.abspath(args.rootpath)
        if args.path == '': args.path = '/' + args.name
        print 'debug', args

        generate.generate_api(
                args.rootpath,
                path=args.path,
                method=args.method,
                name=args.name,
                version=args.version
                )


class GenerateAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, '_generate_'+values)


def main():
    ScarabCmd()

if __name__ == '__main__':
    main()

