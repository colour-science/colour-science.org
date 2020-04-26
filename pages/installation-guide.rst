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

-   `Python>=2.7 <https://www.python.org/download/releases/>`__ or
    `Python>=3.5 <https://www.python.org/download/releases/>`__
-   `Imageio <http://imageio.github.io/>`__
-   `SciPy <http://www.scipy.org/>`__
-   `Six <https://pypi.org/project/six/>`__

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `NetworkX <https://networkx.github.io/>`__
-   `OpenImageIO <https://github.com/OpenImageIO/oiio>`__
-   `Pandas <https://pandas.pydata.org/>`__

Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `Matplotlib <http://matplotlib.org/>`__
-   `Graphviz <https://www.graphviz.org/>`__
-   `PyGraphviz <https://pygraphviz.github.io/>`__

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^

-   `biblib-simple <https://pypi.org/project/biblib-simple/>`__
-   `Coverage.py <https://pypi.org/project/coverage/>`__
-   `coveralls <https://pypi.org/project/coveralls/>`__
-   `Flake8 <https://pypi.org/project/flake8/>`__
-   `Invoke <http://www.pyinvoke.org/>`__
-   `Jupyter <https://jupyter.org/>`__
-   `mock <https://pypi.org/project/mock/>`__
-   `nose <https://nose.readthedocs.io/en/latest>`__
-   `pre-commit <https://pre-commit.com/>`__
-   `pytest <https://docs.pytest.org/en/latest/>`__
-   `restructuredtext-lint <https://github.com/twolfson/restructuredtext-lint>`__
-   `Sphinx <https://sphinx-doc.org>`__
-   `sphinx_rtd_theme <https://github.com/rtfd/sphinx_rtd_theme/>`__
-   `sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`__
-   `twine <https://pypi.org/project/twine/>`__
-   `YAPF==0.23.0 <https://github.com/google/yapf>`__

Installation Methods for Using Colour
-------------------------------------

Pypi
^^^^

**Colour** can be easily installed from the
`Python Package Index <https://pypi.org/project/colour-science/>`__ by
issuing this command in a shell:

.. code:: shell

    $ pip install colour-science

This *asciicast* demonstrates how to generate a pristine Python *VirtualEnv*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/257384.js"
        id="asciicast-257384" async data-speed=3>
    </script>

The optional features dependencies are installed as follows:

.. code:: shell

    $ pip install 'colour-science[optional]'

The development dependencies are installed as follows:

.. code:: shell

    $ pip install 'colour-science[development]'

The figures plotting dependencies are installed as follows:

.. class:: alert alert-dismissible alert-info

    | *Note*
    |
    | `Graphviz <https://www.graphviz.org/>`__ might need to be installed
        beforehand, please refer to the specific section for your platform on
        the `Graphviz download page <https://www.graphviz.org/download/>`__.

.. code:: shell

    $ pip install 'colour-science[plotting]'

If you wish to read *OpenEXR* files, you will need to install the *FreeImage*
plugin for `Imageio <http://imageio.github.io/>`__ as follows:

.. code:: shell

    $ python -c "import imageio;imageio.plugins.freeimage.download()"

Continuum Analytics Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Colour** is also available for `Anaconda <https://www.continuum.io/downloads>`__
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
    $ pip install .

Installation Methods for Developing Colour
------------------------------------------

Poetry
^^^^^^

**Colour** adopts `Poetry <https://poetry.eustace.io>`__ to help managing its
dependencies, this is the recommended way to get started with **Colour**
development.

Assuming `Python>=3.5 <https://www.python.org/download/releases/>`__, and
`Graphviz <https://www.graphviz.org/>`__ are available on your system, install
the development dependencies using `Poetry <https://poetry.eustace.io>`__:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ poetry install --extras "graphviz optional plotting"

Those commands will create a Virtual Environment in which all the required
python packages will be installed.

.. class:: alert alert-dismissible alert-warning

    | *Warning*
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
