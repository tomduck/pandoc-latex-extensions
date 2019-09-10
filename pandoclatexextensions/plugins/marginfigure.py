"""marginfigure.py: tufte-latex marginfigures."""

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

from pandocfilters import Para, RawBlock

import pandocxnos
from pandocxnos import PandocAttributes
from pandocxnos import STDERR
from pandocxnos import get_meta

# pylint: disable=invalid-name

warninglevel = 2

# Flags that the figure environment is replaced
replaced_figure_env = False

# LaTeX environment that replace figures with marginfigures
MARGINFIGURE_TEX = r"""
\newenvironment{marginfigure_}[1][]{
  \let\oldfigure\figure
  \let\oldendfigure\endfigure
  \renewenvironment{figure}{\begin{marginfigure}[#1]}{\end{marginfigure}}
}{
  \let\figure\oldfigure
  \let\endfigure\oldendfigure
}
"""

WARNING = textwrap.dedent("""
pandoc-latex/marginfigure: documentclass must be tufte-book or tufte-handout.
Ignoring.
""")

def is_figure(key, value):
    """Returns True if element represents a figure; False otherwise."""
    return key == 'Para' and len(value) == 1 and \
      value[0]['t'] == 'Image' and value[0]['c'][-1][1].startswith('fig:')


def action(key, value, fmt, meta):  # pylint: disable=unused-argument
    """Processes elements."""

    global replaced_figure_env  # pylint: disable=global-statement

    if is_figure(key, value):

        attrs = PandocAttributes(value[0]['c'][0], 'pandoc')

        # Convert figures with `marginfigure` class to marginfigures
        if 'marginfigure' in attrs.classes:

            if 'documentclass' in meta and \
              get_meta(meta, 'documentclass') in \
              ['tufte-book', 'tufte-handout']:

                replaced_figure_env = True

                # Get the marginfigure options
                offset = attrs['offset'] if 'offset' in attrs else '0pt'

                # LaTeX used to apply the environment
                pre = RawBlock('tex', r'\begin{marginfigure_}[%s]' % offset)
                post = RawBlock('tex', r'\end{marginfigure_}')

                return [pre, Para(value), post]

            if warninglevel:
                STDERR.write(WARNING)

    return None


def processor(meta, blocks):  # pylint: disable=unused-argument
    """Document processor."""
    if replaced_figure_env:
        pandocxnos.add_to_header_includes(meta, 'tex', MARGINFIGURE_TEX,
                                          warninglevel)
