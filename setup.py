#! /usr/bin/python

"""
codewords - Simple python library to generate "code phrases" based on
provided lists of words and delimiters.

This project uses bumpversion so prior to a release you should run:

  $ bumpversion (major|minor|patch)

depending on which version you are wanting to increment.  See
https://github.com/peritus/bumpversion for more information and options.

"""

from setuptools import setup, find_packages
from distutils.core import Command
import codewords


class PylintCommand(Command):
    description = 'Executes pylint on the package specified.'
    user_options = [('package=', 'p', "the package to be pylint'ed")]

    def initialize_options(self):
        self.package = None

    def finalize_options(self):
        pass

    def run(self):
        if not self.package:
            exit("pylint command requires package option to be specified")
        from pylint.lint import Run
        Run(['--output-format=parseable', self.package])


setup(
    name="codewords",
    version=codewords.get_version(),
    author="Louis Zirkel III",
    author_email="zzzirk@gmail.com",
    description='CodeWords python lbrary',
    url='https://stash.movenetworks.com/projects/OPSTOOLS/',
    license="bsd3",

    cmdclass={'pylint': PylintCommand},
    # test_suite="nose.collector",

    packages=find_packages(),

    install_requires=[
    ],

    setup_requires=[
    ],

    tests_require=[
    ],

)
