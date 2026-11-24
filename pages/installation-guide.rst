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

.. _primary-dependencies:

The current PyPI release of **Colour** supports Python 3.11 through 3.14
and requires NumPy 2.0 or newer in the 2.x series. The package manager
installs NumPy automatically. See the
`release metadata <https://pypi.org/project/colour-science/>`__ for the
requirements of the published package.

The development branch has its own requirements. See
`Installation Methods for Developing Colour`_ if you are contributing to
the project.

Installation Methods for Using Colour
-------------------------------------

PyPI
^^^^

Create a virtual environment with a supported Python version:

.. code:: shell

    python -m venv .venv

Activate it with ``source .venv/bin/activate`` on macOS or Linux, or
``.venv\Scripts\Activate.ps1`` in Windows PowerShell. Then install **Colour**
from the `Python Package Index <https://pypi.org/project/colour-science>`__:

.. code:: shell

    python -m pip install colour-science
    python -c "import colour; print(colour.__version__)"

If you manage your project with `uv <https://docs.astral.sh/uv/guides/projects/>`__,
use a Python version supported by the release and run these commands from
the project directory:

.. code:: shell

    uv add colour-science
    uv run python -c "import colour; print(colour.__version__)"

Optional dependencies
^^^^^^^^^^^^^^^^^^^^^

.. _optional-meshing-and-plotting-dependencies:

The ``optional`` extra enables features such as plotting and image I/O.
The basic installation may report missing SciPy or Matplotlib when you
import ``colour``. Install the extra if you need those features.
The published release also provides a ``meshing`` extra for gamut computations
and a ``docs`` extra for building the documentation.

.. code:: shell

    python -m pip install 'colour-science[optional]'
    uv add 'colour-science[optional]'

Use the command for your package manager. For OpenEXR image I/O, the
``optional`` extra includes OpenImageIO. To render conversion graphs, also
install the `Graphviz command-line tools <https://www.graphviz.org/download/>`__
for your platform.

.. _continuum-analytics-anaconda:

Conda
^^^^^

To create a Conda environment with **Colour** from
`conda-forge <https://anaconda.org/conda-forge/colour-science>`__:

.. code:: shell

    conda create -n colour-science -c conda-forge colour-science
    conda activate colour-science
    python -c "import colour; print(colour.__version__)"

GitHub
^^^^^^

To install a specific release from source, activate a virtual environment
as described under `PyPI`_ and check out the corresponding
`release tag <https://github.com/colour-science/colour/tags>`__:

.. code:: shell

    git clone --branch v0.4.7 https://github.com/colour-science/colour.git
    cd colour
    python -m pip install .

Installation Methods for Developing Colour
------------------------------------------

uv
^^

.. _development-dependencies:

The ``develop`` branch currently supports Python 3.13 through 3.15.
Use Python 3.13 for the broadest coverage of optional packages such as
OpenColorIO. Install `uv <https://docs.astral.sh/uv/getting-started/installation/>`__
and run:

.. code:: shell

    git clone --branch develop https://github.com/colour-science/colour.git
    cd colour
    uv sync --python 3.13 --all-extras
    uv run invoke -l

The `contributing guide </contributing/>`__ covers forking and preflight
checks. For macOS-specific setup, see
`Setting Up the Development Environment on macOS </setting-up-the-development-environment-on-macos/>`__.

Vagrant
^^^^^^^

The `Vagrant article </posts/pycharm-vagrant-ansible-poetry/>`__ documents
an earlier development setup. Use the uv instructions above for current
development.
