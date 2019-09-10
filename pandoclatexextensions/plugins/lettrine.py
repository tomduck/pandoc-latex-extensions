"""lettrine.py: drop caps."""

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

import textwrap

from pandocfilters import Str, RawInline

import pandocxnos
from pandocxnos import PandocAttributes

# pylint: disable=invalid-name

warninglevel = 2

has_lettrine = False  # Flags that a lettrine was found

PRE = RawInline('tex', r'\lettrine{')
MID = RawInline('tex', r'}{')
POST = RawInline('tex', r'}')

def action(key, value, fmt, meta):  # pylint: disable=unused-argument
    """Processes elements."""

    global has_lettrine  # pylint: disable=global-statement

    if key == 'Span':

        attrs = PandocAttributes(value[0], 'pandoc')

        if 'lettrine' in attrs.classes:

            has_lettrine = True

            firstword = value[1][0]['c']
            content = value[1][1:]

            # Replace span in para with the elements
            ret = [PRE, Str(firstword[0]), MID]
            if len(firstword) > 1:
                ret.append(Str(firstword[1:]))
            ret += content
            ret.append(POST)

            return  ret

    return None

def processor(meta, blocks):  # pylint: disable=unused-argument
    """Document processor."""

    if has_lettrine:
        pandocxnos.add_to_header_includes(
            meta, 'tex', textwrap.dedent(r'''
            \usepackage{lettrine}
            '''), warninglevel)
