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

**Colour** requires various dependencies in order to run and follows the
`minimum supported versions <https://scientific-python.org/specs/spec-0000>`__
as given by `Scientific Python <https://scientific-python.org>`__. Depending on
your intended use case, i.e. using or developing, you may not need to install
all of them.

Please refer to the `Installation Methods for Using Colour`_
and `Installation Methods for Developing Colour`_ sections below.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

-   `python >= 3.9, < 3.12 <https://www.python.org/download/releases>`__
-   `imageio >= 2, < 3 <https://imageio.github.io>`__
-   `numpy >= 1.22, < 2 <https://pypi.org/project/numpy>`__
-   `scipy >= 1.8, < 2 <https://pypi.org/project/scipy>`__
-   `typing-extensions >= 4, < 5 <https://pypi.org/project/typing-extensions>`__

Optional, Meshing and Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   `graphviz >= 2, < 3 <https://www.graphviz.org>`__
-   `matplotlib >= 3.5, != 3.5.0, != 3.5.1 <https://pypi.org/project/matplotlib>`__
-   `networkx >= 2.7, < 3 <https://pypi.org/project/networkx>`__
-   `opencolorio >= 2, < 3 <https://pypi.org/project/opencolorio>`__
-   `openimageio >= 2, < 3 <https://github.com/OpenImageIO/oiio>`__
-   `pandas >= 1.4, < 2 <https://pypi.org/project/pandas>`__
-   `pygraphviz >= 1, < 2 <https://pypi.org/project/pygraphviz>`__
-   `tqdm >= 4, < 5 <https://pypi.org/project/tqdm>`__
-   `trimesh >= 3, < 4 <https://pypi.org/project/tqdm>`__
-   `xxhash >= 3.2, < 4 <https://pypi.org/project/xxhash>`__

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

-   `biblib-simple <https://pypi.org/project/biblib-simple>`__
-   `black <https://pypi.org/project/black>`__
-   `blackdoc <https://pypi.org/project/blackdoc>`__
-   `coverage <https://pypi.org/project/coverage>`__
-   `coveralls <https://pypi.org/project/coveralls>`__
-   `flynt <https://pypi.org/project/flynt>`__
-   `invoke <https://pypi.org/project/invoke>`__
-   `jupyter <https://pypi.org/project/jupyter>`__
-   `pre-commit <https://pypi.org/project/pre-commit>`__
-   `pyright <https://pypi.org/project/pyright>`__
-   `pydata-sphinx-theme <https://pypi.org/project/pydata-sphinx-theme>`__
-   `pytest <https://pypi.org/project/pytest>`__
-   `pytest-cov <https://pypi.org/project/pytest-cov>`__
-   `pytest-xdist <https://pypi.org/project/pytest-xdist>`__
-   `restructuredtext-lint <https://pypi.org/project/restructuredtext-lint>`__
-   `ruff <https://pypi.org/project/ruff>`__
-   `sphinx >= 4, < 5 <https://pypi.org/project/sphinx>`__
-   `sphinxcontrib-bibtex <https://pypi.org/project/sphinxcontrib-bibtex>`__
-   `toml <https://pypi.org/project/toml>`__
-   `twine <https://pypi.org/project/twine>`__

Installation Methods for Using Colour
-------------------------------------

Pypi
^^^^

**Colour** can be easily installed from the
`Python Package Index <https://pypi.org/project/colour-science>`__ by
issuing this command in a shell:

.. code:: shell

    pip install --user colour-science

This *asciicast* demonstrates how to generate a pristine Python *VirtualEnv*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/257384.js"
        id="asciicast-257384" async data-speed=3>
    </script>

The optional features dependencies are installed as follows:

.. code:: shell

    pip install --user 'colour-science[optional]'

The development dependencies are installed as follows:

.. code:: shell

    pip install --user 'colour-science[development]'

The graphviz figure plotting dependencies are installed as follows:

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | `Graphviz <https://www.graphviz.org>`__ might need to be installed
        beforehand, please refer to the specific section for your platform on
        the `Graphviz download page <https://www.graphviz.org/download>`__.

    pip install --user 'colour-science[graphviz]'

The meshing dependencies for gamut computations are installed as follows:

.. code:: shell

    pip install --user 'colour-science[meshing]'

If you wish to read *OpenEXR* files, you will need to install the *FreeImage*
plugin for `Imageio <https://imageio.github.io>`__ as follows:

.. code:: shell

    python -c "import imageio;imageio.plugins.freeimage.download()"

Continuum Analytics Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Colour** is also available for `Anaconda <https://www.anaconda.com>`__
from *Continuum Analytics* via `conda-forge <https://conda-forge.org>`__:

.. code:: shell

    conda install -c conda-forge colour-science

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

    git clone git://github.com/colour-science/colour.git
    cd colour
    pip install --user .

Installation Methods for Developing Colour
------------------------------------------

Poetry
^^^^^^

**Colour** adopts `Poetry <https://poetry.eustace.io>`__ to help managing its
dependencies, this is the recommended way to get started with **Colour**
development.

Assuming `python >= 3.8, < 3.11 <https://www.python.org/download/releases>`__ is
available on your system, the development dependencies are installed with
`Poetry <https://poetry.eustace.io>`__ as follows:

.. code:: shell

    git clone git://github.com/colour-science/colour.git
    cd colour
    poetry install --with dev,graphviz,meshing,optional

If `Graphviz <https://www.graphviz.org>`__ is available on your system, you
might issue the following commands instead of the aforementioned ones:

.. code:: shell

    git clone git://github.com/colour-science/colour.git
    cd colour
    poetry install --with dev,graphviz,meshing,optional

Those commands will create a Virtual Environment in which all the required
python packages will be installed.

Tools can then be run as follows:

.. code:: shell

    poetry run invoke -l

or alternatively:

.. code:: shell

    source $(poetry env info -p)/bin/activate
    invoke -l

Vagrant
^^^^^^^

An easy way to get all the pre-requisites at once is to use our
`colour-vagrant <https://github.com/colour-science/colour-vagrant>`__
environment for `Vagrant <https://www.vagrantup.com>`__.

Please refer to the dedicated blog post for more details about its deployment:
`PyCharm, Vagrant, Ansible & Poetry </posts/pycharm-vagrant-ansible-poetry>`__
