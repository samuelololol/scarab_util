__date__= 'Nov 20, 2015 '
__author__= 'samuel'
import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

VERSION = '0.1'
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()



requires = ['jinja2',
            'pytest-capturelog',
            'pytest-cov',
            'pytest',
           ]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["-s"]
        self.test_suite = True

    def run(self):
        import pytest
        pytest.main(self.test_args)

setup(name='scarab_util',
      version=VERSION,
      description='CLI tool for scarab web framework',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          ],
      author='samuelololol',
      author_email='samuelololol@gmail.com',
      url='',
      keywords='web scarab pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      test_suite='scarab_util',
      tests_require=[],
      cmdclass = {'test': PyTest},
      entry_points= """\
      [console_scripts]
      scarab = scarab_util:main
      """,
      )

