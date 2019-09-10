"""newthought.py: tufte-latex newthoughts."""

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

from pandocfilters import RawInline

from pandocxnos import PandocAttributes
from pandocxnos import STDERR
from pandocxnos import get_meta

# pylint: disable=invalid-name

warninglevel = 2

WARNING = textwrap.dedent("""
pandoc-latex/newthought: documentclass must be tufte-book or tufte-handout.
Ignoring.
""")

def action(key, value, fmt, meta):  # pylint: disable=unused-argument
    """Processes elements."""

    if key == 'Span':

        attrs = PandocAttributes(value[0], 'pandoc')

        if 'newthought' in attrs.classes:
            if 'documentclass' in meta and \
              get_meta(meta, 'documentclass') in \
              ['tufte-book', 'tufte-handout']:

                pre = RawInline('tex', r'\newthought{')
                post = RawInline('tex', r'}')

                value[1].insert(0, pre)
                value[1].append(post)

            elif warninglevel:
                STDERR.write(WARNING)
