
Developer Notes
===============


Install Alternatives
--------------------

Installing from source may require upgrading `setuptools` by executing

    pip install --upgrade setuptools

as root (or under sudo).

There are a few different options for installing from source:
    
1) To install from the github `master` branch use:

       $ pip install git+https://github.com/tomduck/pandoc-latex-extensions.git --user

   (to upgrade use the --upgrade flag).

2) To install from a local source distribution, `cd` into its root and use

       pip install -e . --user

   Note that any changes made to the source will be automatically reflected
   when the filter is run (which is useful for development).


Preparing a Release
-------------------

See https://www.python.org/dev/peps/pep-0440/ for numbering conventions,
including for pre-releases.
    
Tagging  (update the version number):

    $ git tag -a 0.1.0 -m "New release."
    $ git push origin 0.1.0


Creating source and binary distributions:

    $ python3 setup.py sdist bdist_wheel

(see https://packaging.python.org/tutorials/packaging-projects/).
    
Uploading to pypi (update the version number):

    $ twine upload dist/pandoc-latex-extensions-0.1.0.tar.gz \
                   dist/pandoc_latex_extensions-0.1.0-py3-none-any.whl

(see https://pypi.python.org/pypi/twine).