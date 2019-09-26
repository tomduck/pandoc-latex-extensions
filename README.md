
pandoc-latex-extensions 0.2.2
=============================

*pandoc-latex-extensions* is a [pandoc] filter that adds latex extensions.

Bug reports and feature requests may be posted on the project's [Issues tracker].  If you find pandoc-latex-extensions useful, then please kindly give it a star [on GitHub].

Plugin contributions are welcome.  Information for developers is given in [DEVELOPERS.md].

See also: [pandoc-fignos], [pandoc-eqnos], [pandoc-tablenos], [pandoc-secnos], and [pandoc-comments].

[pandoc]: http://pandoc.org/
[Issues tracker]: https://github.com/tomduck/pandoc-latex-extensions/issues
[on GitHub]:  https://github.com/tomduck/pandoc-latex-extensions
[DEVELOPERS.md]: DEVELOPERS.md
[pandoc-fignos]: https://github.com/tomduck/pandoc-fignos
[pandoc-eqnos]: https://github.com/tomduck/pandoc-eqnos
[pandoc-tablenos]: https://github.com/tomduck/pandoc-tablenos
[pandoc-secnos]: https://github.com/tomduck/pandoc-secnos
[pandoc-comments]: https://github.com/tomduck/pandoc-comments


Contents
--------

 1. [Installation](#installation)
 2. [Usage](#usage)
 3. [Markdown Syntax](#markdown-syntax)


Installation
------------

Pandoc-latex-extensions requires [python], a programming language that comes pre-installed on macOS and linux.  It is easily installed on Windows -- see [here](https://realpython.com/installing-python/).

Pandoc-latex-extensions may be installed using the shell command

    pip install pandoc-latex-extensions --user

and upgraded by appending `--upgrade` to the above command.  Pip is a program that downloads and installs software from the Python Package Index, [PyPI].  It normally comes installed with a python distribution.<sup>[1](#footnote1)</sup>


[python]: https://www.python.org/
[PyPI]: https://pypi.python.org/pypi


Usage
-----

Pandoc-latex-extensions is activated by using the

    --filter pandoc-latex-extensions

option with pandoc.


Extensions
----------

The following extensions are enabled.  Options for each extension will be implemented on request.


### newpage ###

Synopsis: Converts pandoc [horizontal rules](https://pandoc.org/MANUAL.html#horizontal-rules) to `\newpage` commands.


### lettrine ###

Synopsis: Converts pandoc [spans](https://pandoc.org/MANUAL.html#divs-and-spans) of class `lettrine` to `\lettrine` (drop caps) commands.

Installs: The [lettrine](https://www.ctan.org/pkg/lettrine) package.

Example markdown:

~~~markdown
[Lorem]{.lettrine} ipsum dolor sit amet, consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo. Donec id velit non mauris porttitor semper. Suspendisse non pharetra lorem, luctus euismod odio. Integer eu diam at odio feugiat venenatis vitae sit amet libero. Duis ut auctor libero, et venenatis nisi. Fusce nec posuere nisi, porta rutrum justo. Suspendisse blandit tellus eget venenatis scelerisque.
~~~

Result:

![lettrine demonstration](../demos/lettrine.png)


### noindent ###

Synopsis: Removes indentation from the content of pandoc [divs](https://pandoc.org/MANUAL.html#divs-and-spans) with class `noindent`.

Example markdown:

~~~markdown
::: {.noindent}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo. Donec id velit non mauris porttitor semper.
:::
~~~

Result:

![noindent demonstration](../demos/noindent.png)


### epigraph ###

Synopsis: Converts pandoc [divs](https://pandoc.org/MANUAL.html#divs-and-spans) with class `epigraph` to `\epigraph` commands.

Installs: The [epigraph](https://ctan.org/pkg/epigraph) package.

Example markdown:

~~~markdown
::: {.epigraph}
Aliquam erat volutpat.

Lorem Ipsum Generatis
:::

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo. Donec id velit non mauris porttitor semper.
~~~

Result:

![epigraph demonstration](../demos/epigraph.png)

The last line in the div is taken to be the quote author.  There must be a blank line above it.

Indentation is removed from the first paragraph after the epigraph.


### newthought ###

Synopsis: Converts pandoc [spans](https://pandoc.org/MANUAL.html#divs-and-spans) with class `newthought` to [tufte-latex](https://www.ctan.org/pkg/tufte-latex) `\newthought` commands.

Documentclass: `tufte-book` or `tufte-handout`.

Example markdown:

~~~markdown
---
documentclass: tufte-handout
...

[Lorem ipsum dolor sit amet,]{.newthought} consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo.
~~~

Result:

![newthought demonstration](../demos/newthought.png)


### marginnote ###

Synopsis: Converts pandoc [divs](https://pandoc.org/MANUAL.html#divs-and-spans) with class `marginnote` to [tufte-latex](https://www.ctan.org/pkg/tufte-latex) `\marginnote` commands.

Documentclass: `tufte-book` or `tufte-handout`.

Options: `offset`.

Example markdown:

~~~markdown
---
documentclass: tufte-handout
...

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo. Donec id velit non mauris porttitor semper. Suspendisse non pharetra lorem, luctus euismod odio. Integer eu diam at odio feugiat venenatis vitae sit amet libero. Duis ut auctor libero, et venenatis nisi. Fusce nec posuere nisi, porta rutrum justo. Suspendisse blandit tellus eget venenatis scelerisque.

::: {.marginnote offset=-2cm}
Maecenas vehicula hendrerit massa, sed consequat ipsum facilisis et. Fusce eu velit neque. Duis vel aliquam ex.
:::
~~~

Result:

![marginnote demonstration](../demos/marginnote.png)


### marginfigure ###

Synopsis: Converts pandoc [implicit figures](https://pandoc.org/MANUAL.html#extension-implicit_figures) with class `marginfigure` to [tufte-latex](https://www.ctan.org/pkg/tufte-latex) `marginfigure` environments.

Documentclass: `tufte-book` or `tufte-handout`.

Options: `offset`.

Example markdown:

~~~markdown
---
documentclass: tufte-handout
...

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non massa semper, commodo massa a, molestie justo. Donec id velit non mauris porttitor semper. Suspendisse non pharetra lorem, luctus euismod odio. Integer eu diam at odio feugiat venenatis vitae sit amet libero. Duis ut auctor libero, et venenatis nisi. Fusce nec posuere nisi, porta rutrum justo. Suspendisse blandit tellus eget venenatis scelerisque.

![Duis nisi eros, consectetur facilisis odio id, vehicula accumsan justo.](img/fig-1.png){.marginfigure offset=-2cm}
~~~

Result:

![marginfigure demonstration](../demos/marginfigure.png)


----

**Footnotes**

<a name="footnote1">1</a>: Anaconda users may be tempted to use `conda` instead.  This is not advised.  The packages distributed on the Anaconda cloud are unofficial, are not posted by me, and in some cases are ancient.  Some tips on using `pip` in a `conda` environment may be found [here](https://www.anaconda.com/using-pip-in-a-conda-environment/).
