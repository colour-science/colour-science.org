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

**Colour** requires various dependencies in order to run. Depending your usage
you may not need to install all of them.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

-  `Python>=2.7 <https://www.python.org/download/releases/>`_ or
   `Python>=3.6 <https://www.python.org/download/releases/>`_
-  `NumPy>=1.8.1 <http://www.numpy.org/>`_
-  `SciPy>=0.16.0 <http://www.scipy.org/>`_
-  `Six>=1.10.0 <https://pypi.python.org/pypi/six>`_

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

-  `OpenImageIO <https://github.com/OpenImageIO/oiio>`_
-  `Pandas <https://pandas.pydata.org/>`_

Optional Figures Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Matplotlib>=2.2.0 <http://matplotlib.org/>`_

Documentation Building Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Sphinx>=1.6.6 <https://sphinx-doc.org>`_
-  `sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_
-  `sphinx_rtd_theme <https://github.com/rtfd/sphinx_rtd_theme/>`_

Unit Tests Dependencies
^^^^^^^^^^^^^^^^^^^^^^^

-  `Coverage.py>=3.7.1 <https://pypi.python.org/pypi/coverage>`_
-  `Flake8>=2.1.0 <https://pypi.python.org/pypi/flake8>`_
-  `mock>=1.3.4 <https://pypi.python.org/pypi/mock>`_
-  `nose <https://nose.readthedocs.io/en/latest>`_

Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Invoke <http://www.pyinvoke.org/>`_
-  `restructuredtext-lint <https://github.com/twolfson/restructuredtext-lint>`_
-  `twine <https://pypi.python.org/pypi/twine>`_
-  `YAPF <https://github.com/google/yapf>`_

Continuum Analytics Anaconda
----------------------------

`Anaconda <https://www.continuum.io/downloads>`_ from *Continuum Analytics*
is the Python distribution we use to develop **Colour**:
it ships all the scientific dependencies we require and is easily deployed
cross-platform.

Colour is available on *conda* and can be installed as follows:

.. code:: shell

    conda install -c conda-forge colour-science

This *asciicast* demonstrates how to generate a pristine Python *conda*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/125160.js"
        id="asciicast-125160" async data-speed=3>
    </script>

Pypi
----

**Colour** can be easily installed from the
`Python Package Index <https://pypi.python.org/pypi/colour-science/>`_ by
issuing this command in a shell:

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | Because of the non deterministic order in which *pip* installs
        dependencies, `SciPy <http://www.scipy.org/>`_ will require
        `NumPy <http://www.numpy.org/>`_ to be installed first which can be
        performed as follows: `pip install numpy`

.. code:: shell

    pip install colour-science

This *asciicast* demonstrates how to generate a pristine Python *VirtualEnv*
environment for Colour:

.. raw:: html

    <script type="text/javascript"
        src="https://asciinema.org/a/125159.js"
        id="asciicast-125159" async data-speed=3>
    </script>

The optional features dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[optional]'

The figures plotting dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[plotting]'

The tests suite dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[tests]'

The documentation building dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[docs]'

The overall development dependencies are installed as follows:

.. code:: shell

    pip install 'colour-science[development]'

Github
------

Alternatively, you can also install directly from
`Github <http://github.com/colour-science/colour>`_ source repository:

.. code:: shell

    git clone git://github.com/colour-science/colour.git
    cd colour
    pip install .

Vagrant
-------

An easy way to get all the pre-requisites at once is to use our
`colour-vagrant <https://github.com/colour-science/colour-vagrant>`_
environment for `Vagrant <https://www.vagrantup.com/>`_.

Please refer to the dedicated blog post for more details about its deployment:
`PyCharm, Vagrant, Fabric & Anaconda </posts/pycharm-vagrant-fabric-anaconda/>`_
