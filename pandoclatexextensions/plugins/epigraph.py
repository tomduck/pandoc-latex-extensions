"""epigraph.py - epigraphs"""

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
import copy

from pandocfilters import RawInline, stringify

import pandocxnos
from pandocxnos import PandocAttributes
from pandocxnos import quotify

# pylint: disable=invalid-name

warninglevel = 2

# Inline tex to be inserted into epigraph divs
PRE = RawInline('tex', r'\epigraph{')
MID = RawInline('tex', r'}{')
POST = RawInline('tex', r'}')

def processor(meta, blocks):
    """Document processor."""

    has_epigraph = False  # Flags that an epigraph was found
    noindent = False      # Flags that next para should not be indented

    # Process the blocks
    for block in blocks:
        if block['t'] == 'Div':
            attrs = PandocAttributes(block['c'][0])

            # Process epigraph divs
            if 'epigraph' in attrs.classes:

                # Insert tex into div content
                content = block['c'][1]
                content[0]['c'].insert(0, PRE)
                content[-2]['c'].append(MID)
                for el in content[-1]['c']:
                    content[-2]['c'].append(el)
                content[-2]['c'].append(POST)
                del content[-1]

                # Set flags and continue
                has_epigraph = True
                noindent = True
                continue

        # Don't indent the first non-empty paragraph after an epigraph
        if block['t'] == 'Para' and noindent:
            content = stringify(quotify(copy.deepcopy(block['c'])))
            if content.strip():
                block['c'].insert(0, RawInline('tex', r'\noindent '))
                noindent = False

    if has_epigraph:
        pandocxnos.add_to_header_includes(
            meta, 'tex', textwrap.dedent(r'''
            \usepackage{epigraph}
            '''), warninglevel)
