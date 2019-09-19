"""core.py: Core infrastructure for pandoc-latex-extensions."""

__version__ = '0.2.1'

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

import os
import pkgutil
import argparse
import functools
import json
import textwrap

from pandocfilters import walk

from pandocxnos import get_meta
from pandocxnos import STDIN, STDOUT, STDERR

from . import plugins


# Import the plugins
PLUGINS = [finder.find_module(name).load_module(name) \
           for finder, name, ispkg in \
           pkgutil.iter_modules([os.path.dirname(plugins.__file__)])]

ACTIONS = [plugin.action for plugin in PLUGINS if hasattr(plugin, 'action')]

PROCESSORS = [plugin.processor for plugin in PLUGINS \
              if hasattr(plugin, 'processor')]

def main():
    """Main program"""

    # Read the command-line arguments
    parser = argparse.ArgumentParser(description='Pandoc latex extensions.')
    version = '%(prog)s {version}'.format(version=__version__)
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('fmt')
    args = parser.parse_args()

    # Get the output format and document
    fmt = args.fmt
    doc = json.loads(STDIN.read())

    # This filter only operates on latex documents
    if fmt != 'latex':
        json.dump(doc, STDOUT)
        STDOUT.flush()

    # Chop up the doc
    meta = doc['meta']
    blocks = doc['blocks']

    # Get the warning level
    warninglevel = 2  # 0 - no warnings; 1 - some warnings; 2 - all warnings
    for name in ['pandoc-latex-extensions-warning-level', 'xnos-warning-level']:
        if name in meta:
            warninglevel = int(get_meta(meta, name))
            break

    # Set the warninglevel in each plugin
    for plugin in PLUGINS:
        plugin.warninglevel = warninglevel

    # Apply the actions
    altered = functools.reduce(lambda x, action: walk(x, action, fmt, meta),
                               ACTIONS, blocks)
    # Apply the processors
    if warninglevel == 2:
        msg = textwrap.dedent("""\
                 pandoc-latex-extensions: Wrote the following blocks to
                 header-includes.  If you use pandoc's
                  --include-in-header option then you will need to
                  manually include these yourself.
              """)
        STDERR.write('\n')
        STDERR.write(textwrap.fill(msg))
        STDERR.write('\n')
    for processor in PROCESSORS:
        processor(meta, altered)

    # Finish up
    doc['blocks'] = altered
    json.dump(doc, STDOUT)
    STDOUT.flush()

if __name__ == '__main__':
    main()
