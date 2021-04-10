"""setup.py - install script for pandoc-latex-extensions."""

# Copyright 2019 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import io

from setuptools import setup, find_packages

DESCRIPTION = 'A pandoc filter that adds latex extensions.'

# From https://stackoverflow.com/a/39671214
__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open('pandoclatexextensions/core.py', encoding='utf_8_sig').read()
    ).group(1)

setup(
    name='pandoc-latex-extensions',
    version=__version__,

    author='Thomas J. Duck',
    author_email='tomduck@tomduck.ca',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    license='GPL',
    keywords='pandoc latex extensions filter',
    url='https://github.com/tomduck/pandoc-xnos',
    download_url=\
    'https://github.com/tomduck/pandoc-latex-extensions/tarball/'+__version__,

    install_requires=['pandocfilters >= 1.4.2, < 2.0',
                      'pandoc-xnos >= 2.1.2, < 3.0'],

    packages=find_packages(),

    entry_points={'console_scripts':
                  ['pandoc-latex-extensions = pandoclatexextensions:main']},

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
        ],
)
