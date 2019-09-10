"""noindent.py: for removing indentation."""

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

from pandocfilters import Div, RawBlock

from pandocxnos import PandocAttributes

# LaTeX for removing indentation
PRE = RawBlock('tex', r'{\parindent0pt')
POST = RawBlock('tex', r'}')

def action(key, value, fmt, meta):  # pylint: disable=unused-argument
    """Processes elements."""

    if key == 'Div':

        attrs = PandocAttributes(value[0], 'pandoc')

        if 'noindent' in attrs.classes:
            return [PRE, Div(*value), POST]

    return None
