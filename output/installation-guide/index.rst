.. title: Installation Guide
.. slug: installation-guide
.. date: 2015-11-24 09:38:23 UTC
.. tags: installation
.. category:
.. link:
.. description:
.. type: text

Dependencies
------------

**Colour** requires various dependencies in order to run. Depending your
intended use case, i.e. using or developing, you may not need to install all of
them.

Please refer to the `Installation Methods for Using Colour`_
and `Installation Methods for Developing Colour`_ sections below.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

-   `python>=3.6 <https://www.python.org/download/releases/>`__
-   `imageio <http://imageio.github.io/>`__
-   `scipy>=1.1.0 <https://pypi.org/project/scipy/>`__
-   `six <https://pypi.org/project/six/>`__

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `networkx <https://pypi.org/project/networkx/>`__
-   `openimageio <https://github.com/OpenImageIO/oiio>`__
-   `pandas <https://pypi.org/project/pandas/>`__

Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `matplotlib <https://pypi.org/project/matplotlib/>`__
-   `graphviz <https://www.graphviz.org/>`__
-   `pygraphviz <https://pypi.org/project/pygraphviz/>`__

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^

-   `backports.functools_lru_cache <https://pypi.org/project/backports.functools-lru-cache/>`__
-   `biblib-simple <https://pypi.org/project/biblib-simple/>`__
-   `coverage <https://pypi.org/project/coverage/>`__
-   `coveralls <https://pypi.org/project/coveralls/>`__
-   `flake8 <https://pypi.org/project/flake8/>`__
-   `invoke <https://pypi.org/project/invoke/>`__
-   `jupyter <https://pypi.org/project/jupyter/>`__
-   `mock <https://pypi.org/project/mock/>`__
-   `nbformat>=4 <https://pypi.org/project/nbformat/>`__
-   `nose <https://pypi.org/project/nose/>`__
-   `pre-commit <https://pypi.org/project/pre-commit/>`__
-   `pytest <https://pypi.org/project/pytest/>`__
-   `restructuredtext-lint <https://pypi.org/project/restructuredtext-lint/>`__
-   `sphinx <https://pypi.org/project/Sphinx/>`__
-   `sphinx-rtd-theme <https://pypi.org/project/sphinx-rtd-theme/>`__
-   `sphinxcontrib-bibtex <https://pypi.org/project/sphinxcontrib-bibtex/>`__
-   `twine <https://pypi.org/project/twine/>`__
-   `yapf==0.23.0 <https://pypi.org/project/yapf/>`__

Installation Methods for Using Colour
-------------------------------------

Pypi
^^^^

**Colour** can be easily installed from the
`Python Package Index <https://pypi.org/project/colour-science/>`__ by
issuing this command in a shell:

.. code:: shell

    $ pip install --user colour-science

This *asciicast* demonstrates how to generate a pristine Python *VirtualEnv*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/257384.js"
        id="asciicast-257384" async data-speed=3>
    </script>

The optional features dependencies are installed as follows:

.. code:: shell

    $ pip install --user 'colour-science[optional]'

The development dependencies are installed as follows:

.. code:: shell

    $ pip install --user 'colour-science[development]'

The figures plotting dependencies are installed as follows:

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | `Graphviz <https://www.graphviz.org/>`__ might need to be installed
        beforehand, please refer to the specific section for your platform on
        the `Graphviz download page <https://www.graphviz.org/download/>`__.

.. code:: shell

    $ pip install --user 'colour-science[plotting]'

If you wish to read *OpenEXR* files, you will need to install the *FreeImage*
plugin for `Imageio <http://imageio.github.io/>`__ as follows:

.. code:: shell

    $ python -c "import imageio;imageio.plugins.freeimage.download()"

Continuum Analytics Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Colour** is also available for `Anaconda <https://www.anaconda.com/>`__
from *Continuum Analytics* via `conda-forge <https://conda-forge.org/>`__:

.. code:: shell

    $ conda install -c conda-forge colour-science

This *asciicast* demonstrates how to generate a pristine Python *conda*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/257385.js"
        id="asciicast-257385" async data-speed=3>
    </script>

Github
^^^^^^

Alternatively, you can also install directly from
`Github <https://github.com/colour-science/colour>`__ source repository:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ pip install --user .

Installation Methods for Developing Colour
------------------------------------------

Poetry
^^^^^^

**Colour** adopts `Poetry <https://poetry.eustace.io>`__ to help managing its
dependencies, this is the recommended way to get started with **Colour**
development.

Assuming `python>=3.6 <https://www.python.org/download/releases/>`__ is
available on your system, the development dependencies are installed with
`Poetry <https://poetry.eustace.io>`__ as follows:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ poetry install --extras "optional plotting"

.. class:: alert alert-dismissible alert-warning

    | **Warning**
    |
    | As of this writing, we are still supporting `Python 2.7 <https://www.python.org/download/releases/>`__ which might produce issues when resolving
        dependencies with a `Python 3.8 <https://www.python.org/download/releases/>`__
        interpreter. We are indeed effectively patching the
        `pyproject.toml <https://github.com/colour-science/colour/blob/develop/pyproject.toml>`__
        file on `Github Actions <https://github.com/colour-science/colour/actions>`__:

        .. code:: shell

                $ sed -i.bak 's/python = "~2.7 || ^3.5"/python = "^3.6"/g' pyproject.toml
                $ sed -i.bak 's/matplotlib = { version = "\*"/matplotlib = { version = "^3.1"/g' pyproject.toml
                $ git diff --unified=1
                diff --git a/pyproject.toml b/pyproject.toml
                index 93088d8c..c2b282cf 100644
                --- a/pyproject.toml
                +++ b/pyproject.toml
                @@ -46,3 +46,3 @@ classifiers = [
                 [tool.poetry.dependencies]
                -python = "~2.7 || ^3.5"
                +python = "^3.6"
                 imageio = "*"
                @@ -58,3 +58,3 @@ invoke = { version = "*", optional = true }  # Development dependency.
                 jupyter = { version = "*", optional = true }  # Development dependency.
                -matplotlib = { version = "*", optional = true }
                +matplotlib = { version = "^3.1", optional = true }
                 mock = { version = "*", optional = true }  # Development dependency.

If `Graphviz <https://www.graphviz.org/>`__ is available on your system, you
might issue the following commands instead of the aforementioned ones:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ poetry install --extras "graphviz optional plotting"

Those commands will create a Virtual Environment in which all the required
python packages will be installed.

Tools can then be run as follows:

.. code:: shell

    $ poetry run invoke -l

or alternatively:

.. code:: shell

    $ source $(poetry env info -p)/bin/activate
    $ invoke -l

Vagrant
^^^^^^^

An easy way to get all the pre-requisites at once is to use our
`colour-vagrant <https://github.com/colour-science/colour-vagrant>`__
environment for `Vagrant <https://www.vagrantup.com/>`__.

Please refer to the dedicated blog post for more details about its deployment:
`PyCharm, Vagrant, Ansible & Poetry </posts/pycharm-vagrant-ansible-poetry/>`__
