# Introduction #

[Sphinx](http://sphinx.pocoo.org/index.html) is increasingly being used to generate user documentation for Python projects (including Python itself). We should adopt this for PySAL since it would allow us to easily bundle user docs with the source code.
It relies on [reStructuredText](http://docutils.sf.net/rst.html) for markup and has low startup costs.

This guide gets developers going with Sphinx for documenting the PySAL modules we want end-users to interact with.


# Details #

## Creating a module entry in the documentation index ##

The main index for the documentation is in the file [doc/sources/index.rst](http://code.google.com/p/pysal/source/browse/trunk/doc/source/index.rst).
Each module should have an entry in the `toctree` of this document. The description for a module
gets entered in file `moduleName.rst` which lives in [doc/sources/](http://code.google.com/p/pysal/source/browse/trunk/doc/source) and this can be linked to the toctree as
follows:

```

.. toctree::
   :maxdepth: 2

   moduleName.rst

```

Alternatively, if you wanted a more descriptive entry in the html index:

```

.. toctree::
   :maxdepth: 2

   Descriptive Entry <moduleName.rst>

```

(Note that the `.rst` extension is not required in the toctree).

## Building the docs ##

Using [doc/Makefile](http://code.google.com/p/pysal/source/browse/trunk/doc/Makefile) a `make html` will rebuild the html tree which lives in [doc/build/html](http://code.google.com/p/pysal/source/browse/trunk/doc/build/html) Note that LaTeX can also be generated from the docs (as well as math markup in the documentation), using `make latex`.