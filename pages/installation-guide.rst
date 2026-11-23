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

-   `python >= 3.11, < 3.15 <https://www.python.org/download/releases>`__
-   `numpy >= 2.0.0, < 3 <https://pypi.org/project/numpy>`__

Optional, Meshing and Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   `imageio >= 2, < 3 <https://imageio.github.io>`__
-   `matplotlib >= 3.9 <https://pypi.org/project/matplotlib>`__
-   `networkx >= 3.3, < 4 <https://pypi.org/project/networkx>`__
-   `opencolorio >= 2, < 3 <https://pypi.org/project/opencolorio>`__
-   `openimageio >= 3, < 4 <https://github.com/OpenImageIO/oiio>`__
-   `pandas >= 2.2, < 3 <https://pypi.org/project/pandas>`__
-   `pydot >= 3, < 4 <https://pypi.org/project/pydot>`__
-   `scipy >= 1.13.0, < 2 <https://pypi.org/project/scipy>`__
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

PyPI
^^^^

To install **Colour** from the
`Python Package Index <https://pypi.org/project/colour-science>`__, activate
your Python virtual environment and run:

.. code:: shell

    pip install colour-science

To add **Colour** as a dependency of an existing
`uv project <https://docs.astral.sh/uv/concepts/projects/dependencies/>`__,
run this command from the project directory:

.. code:: shell

    uv add colour-science

This *asciicast* demonstrates how to generate a pristine Python *VirtualEnv*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/257384.js"
        id="asciicast-257384" async data-speed=3>
    </script>

The optional features dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[optional]'

The development dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[development]'

The graphviz figure plotting dependencies are installed as follows:

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | `Graphviz <https://www.graphviz.org>`__ might need to be installed
        beforehand, please refer to the specific section for your platform on
        the `Graphviz download page <https://www.graphviz.org/download>`__.

    pip install 'colour-science[graphviz]'

The meshing dependencies for gamut computations are installed as follows:

.. code:: shell

    pip install 'colour-science[meshing]'

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

GitHub
^^^^^^

Alternatively, you can also install directly from the
`GitHub <https://github.com/colour-science/colour>`__ source repository:

.. code:: shell

    git clone https://github.com/colour-science/colour.git
    cd colour
    pip install --user .

Installation Methods for Developing Colour
------------------------------------------

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | If you are on macOS, a dedicated guide on how to set up your environment
        is available here: `Setting Up the Development Environment on macOS <../setting-up-the-development-environment-on-macos/index.html>`__.

uv
^^^

**Colour** adopts `uv <https://docs.astral.sh/uv>`__ to help manage its
dependencies. This is the recommended way to get started with **Colour**
development.

Assuming `python >= 3.11, < 3.15 <https://www.python.org/download/releases>`__ is
available on your system, the development dependencies are installed with
`uv <https://docs.astral.sh/uv>`__ as follows:

.. code:: shell

    git clone https://github.com/colour-science/colour.git
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
