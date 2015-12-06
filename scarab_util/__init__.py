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
    def __init__(self, command_string):
        self.command_string = command_string
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
        parser.add_argument('subcommand', choices=['generate', 'show'],
                            help='Subcommand to run')
        args = parser.parse_args(self.command_string[1:2])
        getattr(self, args.subcommand)()

    def generate(self):
        description='Generate scarab component'
        usage = """scarab generate -t <type>

        Available types are:

        api         Generate URI entry, API file, Service file and Test file.
        model       Generate Model file, initial Script entries and Test file.
        async_api   Generate URI entry, API file, Service file ,Test file and
                      Celery setting in development.
        page        Generate URI entry, Page file, Template file and Test file.
        """
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                usage=usage,
                add_help=False,
                )

        parser.add_argument('-t', '--type',
                            required=True,
                            action=GenerateAction,
                            type=str,
                            choices=['api', 'model', 'page'],
                            help='Component type')

        args, others = parser.parse_known_args(self.command_string[2:])
        getattr(self, args.type)(self.command_string[2:])

    def show(self):
        print """scarab show: under construction
        """

    def _generate_api(self, cmd_string):
        description='Generate scarab api components'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type', type=str,
                            required=True,
                            choices=['api'],
                            help='Component type: \'api\'',
                            metavar='')
        parser.add_argument('-p', '--path', type=str,
                            default='',
                            help='API URI, as <path>. If --prefix is not specified, --version will be default applied',
                            metavar='')
        parser.add_argument('-n', '--name', type=str.lower,
                            required=True,
                            help='API name',
                            metavar='')
        parser.add_argument('-r', '--rootpath', type=str,
                            default='.',
                            help='scarab root folder path',
                            metavar='')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--version', type=int, metavar='',
                            help='API version(conflict with --prefix), as \'/api/<version>/<path>\', default: \'1\'')
        group.add_argument('--prefix', type=str, metavar='',
                            help='API prefix(conflict with --version), as \'/<prefix>/<path>\'')
        args = parser.parse_args(cmd_string)

        #default values
        args.rootpath = os.path.abspath(args.rootpath)
        if args.path == '': args.path = '/' + args.name
        args.name = args.name.lower()
        print 'debug', args

        generate.generate_api(
                     args.rootpath,
                     path=args.path,
                     name=args.name,
                     version=args.version,
                     prefix=args.prefix
                     )

    def _generate_model(self, cmd_string):
        description='Generate scarab model components'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type', type=str,
                            required=True,
                            choices=['model'],
                            help='Component type',
                            metavar='')
        parser.add_argument('-n', '--name', type=str.lower,
                            required=True,
                            help='Model name',
                            metavar='')
        parser.add_argument('-r', '--rootpath', type=str,
                            default='.',
                            help='scarab root folder path',
                            metavar='')

        args = parser.parse_args(cmd_string)

        #default values
        args.rootpath = os.path.abspath(args.rootpath)
        args.name = args.name.lower()
        #print cmd_string
        #print 'debug', args

        generate.generate_model(
                     args.rootpath,
                     name=args.name,
                     )

    def _generate_page(self, cmd_string):
        description='Generate scarab page components'
        parser = argparse.ArgumentParser(
                description=textwrap.dedent(description),
                formatter_class=RawTextHelpFormatter,
                )
        parser.add_argument('-t', '--type', type=str,
                            required=True,
                            choices=['page'],
                            help='Component type',
                            metavar='')
        parser.add_argument('-p', '--path', type=str,
                            default='',
                            help='Page URI, as  \'/<path>\'',
                            metavar='')
        parser.add_argument('-n', '--name', type=str.lower,
                            required=True,
                            help='Page name',
                            metavar='')
        parser.add_argument('-r', '--rootpath', type=str,
                            default='.',
                            help='scarab root folder path',
                            metavar='')
        args = parser.parse_args(cmd_string)

        #default values
        args.rootpath = os.path.abspath(args.rootpath)
        if args.path == '': args.path = '/' + args.name
        args.name = args.name.lower()
        print 'debug', args

        generate.generate_page(
                     args.rootpath,
                     path=args.path,
                     name=args.name,
                     )

class GenerateAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, '_generate_'+values)


def main():
    ScarabCmd(sys.argv)

if __name__ == '__main__':
    main()

