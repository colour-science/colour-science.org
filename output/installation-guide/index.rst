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
intended use, i.e. using or developing, you may not need to install all of them.
Please refer to the `Installation Methods for Using Colour`_
and `Installation Methods for Developing Colour`_ sections below.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

-   `Python>=2.7 <https://www.python.org/download/releases/>`_ or
    `Python>=3.5 <https://www.python.org/download/releases/>`_
-   `Imageio <http://imageio.github.io/>`_, if you wish to read *OpenEXR* files,
    you will need to install the FreeImage plugin as follows:

.. code:: shell

    $ python -c "import imageio;imageio.plugins.freeimage.download()"

-   `SciPy <http://www.scipy.org/>`_
-   `Six <https://pypi.org/project/six/>`_

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `NetworkX <https://networkx.github.io/>`_
-   `OpenImageIO <https://github.com/OpenImageIO/oiio>`_
-   `Pandas <https://pandas.pydata.org/>`_

Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^

-   `Matplotlib <http://matplotlib.org/>`_
-   `PyGraphviz <https://pygraphviz.github.io/>`_,
    `Graphviz <https://www.graphviz.org/>`_ might need to be installed
    beforehand, please refer to the specific section of your platform on the
    `Graphviz download page <https://www.graphviz.org/download/>`_.

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^

-   `biblib-simple <https://pypi.org/project/biblib-simple/>`_
-   `Coverage.py <https://pypi.org/project/coverage/>`_
-   `coveralls <https://pypi.org/project/coveralls/>`_
-   `Flake8 <https://pypi.org/project/flake8/>`_
-   `Invoke <http://www.pyinvoke.org/>`_
-   `Jupyter <https://jupyter.org/>`_
-   `mock <https://pypi.org/project/mock/>`_
-   `nose <https://nose.readthedocs.io/en/latest>`_
-   `pre-commit <https://pre-commit.com/>`_
-   `pytest <https://docs.pytest.org/en/latest/>`_
-   `restructuredtext-lint <https://github.com/twolfson/restructuredtext-lint>`_
-   `Sphinx <https://sphinx-doc.org>`_
-   `sphinx_rtd_theme <https://github.com/rtfd/sphinx_rtd_theme/>`_
-   `sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_
-   `twine <https://pypi.org/project/twine/>`_
-   `YAPF==0.23.0 <https://github.com/google/yapf>`_

Installation Methods for Using Colour
-------------------------------------

Pypi
^^^^

**Colour** can be easily installed from the
`Python Package Index <https://pypi.org/project/colour-science/>`_ by
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

.. code:: shell

    $ pip install 'colour-science[plotting]'

Continuum Analytics Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Colour** is also available for `Anaconda <https://www.continuum.io/downloads>`_
from *Continuum Analytics* via `conda-forge <https://conda-forge.org/>`_:

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
`Github <https://github.com/colour-science/colour>`_ source repository:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ pip install .

Installation Methods for Developing Colour
------------------------------------------

Poetry
^^^^^^

**Colour** adopts `Poetry <https://poetry.eustace.io>`_ to help managing its
dependencies, this is the recommended way to get started with **Colour**
development:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ poetry install

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | At the time of this writing, the preview version of *Poetry*, i.e. 1.0.0b1,
        is recommended to be used. Poetry can be updated to the latest preview
        version by issuing `poetry self:update --preview`.

Those commands will create a Virtual Environment in which all the required
dependencies will be installed. Tools can then be run as follows:

.. code:: shell

    $ poetry run invoke -l

or alternatively:

.. code:: shell

    $ source $(poetry env info -p)/bin/activate
    $ invoke -l

Vagrant
^^^^^^^

An easy way to get all the pre-requisites at once is to use our
`colour-vagrant <https://github.com/colour-science/colour-vagrant>`_
environment for `Vagrant <https://www.vagrantup.com/>`_.

Please refer to the dedicated blog post for more details about its deployment:
`PyCharm, Vagrant, Fabric & Anaconda </posts/pycharm-vagrant-fabric-anaconda/>`_
