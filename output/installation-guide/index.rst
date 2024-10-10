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
your intended use case, i.e., using or developing, you may not need to install
all of them.

Please refer to the `Installation Methods for Using Colour`_
and `Installation Methods for Developing Colour`_ sections below.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

-   `python >= 3.10, < 3.14 <https://www.python.org/download/releases>`__
-   `imageio >= 2, < 3 <https://imageio.github.io>`__
-   `numpy >= 1.24, < 3 <https://pypi.org/project/numpy>`__
-   `scipy >= 1.10, < 2 <https://pypi.org/project/scipy>`__
-   `typing-extensions >= 4, < 5 <https://pypi.org/project/typing-extensions>`__

Optional, Meshing and Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   `graphviz >= 2, < 3 <https://www.graphviz.org>`__
-   `matplotlib >= 3.7 <https://pypi.org/project/matplotlib>`__
-   `networkx >= 3, < 4 <https://pypi.org/project/networkx>`__
-   `opencolorio >= 2, < 3 <https://pypi.org/project/opencolorio>`__
-   `openimageio >= 2, < 3 <https://github.com/OpenImageIO/oiio>`__
-   `pandas >= 2, < 3 <https://pypi.org/project/pandas>`__
-   `pydot >= 3, < 4 <https://pypi.org/project/pydot>`__
-   `tqdm >= 4, < 5 <https://pypi.org/project/tqdm>`__
-   `trimesh >= 4, < 5 <https://pypi.org/project/trimesh>`__
-   `xxhash >= 3, < 4 <https://pypi.org/project/xxhash>`__

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

-   `biblib-simple <https://pypi.org/project/biblib-simple>`__
-   `coverage <https://pypi.org/project/coverage>`__
-   `coveralls <https://pypi.org/project/coveralls>`__
-   `hatch <https://pypi.org/project/hatch>`__
-   `invoke <https://pypi.org/project/invoke>`__
-   `jupyter <https://pypi.org/project/jupyter>`__
-   `pre-commit <https://pypi.org/project/pre-commit>`__
-   `pyright <https://pypi.org/project/pyright>`__
-   `pydata-sphinx-theme <https://pypi.org/project/pydata-sphinx-theme>`__
-   `pytest <https://pypi.org/project/pytest>`__
-   `pytest-cov <https://pypi.org/project/pytest-cov>`__
-   `pytest-xdist <https://pypi.org/project/pytest-xdist>`__
-   `restructuredtext-lint <https://pypi.org/project/restructuredtext-lint>`__
-   `sphinx <https://pypi.org/project/sphinx>`__
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

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | If you are on macOS, a dedicated guide on how to setup your environment
        is available here: `Setting Up the Development Environment on macOS <../setting-up-the-development-environment-on-macos/index.html>`__.

uv
^^^

**Colour** adopts `uv <https://docs.astral.sh/uv>`__ to help managing its
dependencies, this is the recommended way to get started with **Colour**
development.

Assuming `python >= 3.10, < 3.13 <https://www.python.org/download/releases>`__ is
available on your system, the development dependencies are installed with
`uv <https://docs.astral.sh/uv>`__ as follows:

.. code:: shell

    git clone git://github.com/colour-science/colour.git
    cd colour
    uv sync --all-extras

Those commands will create a Virtual Environment in which all the required
python packages will be installed.

Tools can then be run as follows:

.. code:: shell

    uv run invoke -l

or alternatively:

.. code:: shell

    source .venv/bin/activate
    invoke -l

Vagrant
^^^^^^^

An easy way to get all the pre-requisites at once is to use our
`colour-vagrant <https://github.com/colour-science/colour-vagrant>`__
environment for `Vagrant <https://www.vagrantup.com>`__.

Please refer to the dedicated blog post for more details about its deployment:
`PyCharm, Vagrant, Ansible & Poetry </posts/pycharm-vagrant-ansible-poetry>`__
