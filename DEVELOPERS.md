
Developer Notes
===============

Overview
--------

Pandoc-latex-extensions is a [pandoc filter](https://pandoc.org/filters.html).  It is written in python, and so uses the [pandocfilters](https://github.com/jgm/pandocfilters) module. [Pandocxnos](https://github.com/tomduck/pandocxnos) provides additional support.

The `pandoclatex/core.py` module provides common infrastructure for each extension.

Extensions are implemented as plugins.  Installing a new plugin is as easy as dropping it into `pandoclatex/plugins/`.

Plugins may define `action(key, value, fmt, meta)` and `processor(meta, blocks)` functions.  These are automatically detected and called by `pandoclatex/core.py`.

The `action(...)` functions are applied to each element in a pandoc document's abstract syntax tree.  As per the [pandocfilters](https://github.com/jgm/pandocfilters) documentation,

* `key` is the type of the pandoc object (e.g. 'Str', 'Para');
* `value` is the contents of the object (e.g. a string for 'Str', a
  list of inline elements for 'Para')
* `format` is the target output format (as supplied by the format
   argument of walk)
* `meta` is the document's metadata

Processors process document `meta`data and content `blocks`.  These are used mostly for injecting LaTeX into the document `meta`data.  Block processing can also be performed, although `action(...)` is generally preferred.

The best way to write a new plugin is to adapt an existing plugin that does something close to what is desired.


Install Alternatives
--------------------

Installing from source may require upgrading `setuptools` by executing

    pip install --upgrade setuptools

as root (or under sudo).

There are a few different options for installing from source:
    
1) To install from the github `master` branch use:

       pip install git+https://github.com/tomduck/pandoc-latex-extensions.git --user

   (to upgrade append the `--upgrade` flag).

2) To install from the `nextrelease` branch on github, use

       pip install git+https://github.com/tomduck/pandoc-latex-extensions.git@nextrelease --user

   (to upgrade use the --upgrade flag).

3) To install from a local source distribution, `cd` into its root
   and use

       pip install -e . --user

   Note that any changes made to the source will be automatically
   reflected when the filter is run (which is useful for development).


Preparing a Release
-------------------

These are notes for release managers.


### Merging ####

Merge the `nextrelease` branch into `master` using

    git checkout master
    git merge nextrelease
    git push


### Updating Demos ###

Starting from the root of the `master` branch, update demos in the `demos` branch using

    cd demos
    make -B
    git checkout demos
    cp -rf out/* ..
    git commit --amend -am "Updated demos."
    git push --force

This procedure ensures that there will only be a single revision of each file (see https://stackoverflow.com/a/22827188).


### Tagging ###

See https://www.python.org/dev/peps/pep-0440/ for numbering conventions, including for pre-releases.

Check that you are in the `master` branch.

Tagging  (update the version number):

    git tag -a 0.2.1 -m "New release."
    git push origin 0.2.1


### Distributing ###

Create source and binary distributions using

    python3 setup.py sdist bdist_wheel

(see https://packaging.python.org/tutorials/packaging-projects/).
    
Upload to pypi (update the version number) using

    twine upload dist/pandoc-latex-extensions-0.2.1.tar.gz \
                 dist/pandoc_latex_extensions-0.2.1-py3-none-any.whl

(see https://pypi.python.org/pypi/twine).
