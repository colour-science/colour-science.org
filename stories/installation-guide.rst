.. title: Installation Guide
.. slug: installation-guide
.. date: 2015-11-24 09:38:23 UTC
.. tags:
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

-  `Python >= 2.7 <https://www.python.org/download/releases/>`_ or
   `Python >= 3.5 <https://www.python.org/download/releases/>`_
-  `NumPy >= 0.16 <http://www.numpy.org/>`_
-  `SciPy >= 1.8 <http://www.scipy.org/>`_

Optional Figures Plotting Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Matplotlib <http://matplotlib.org/>`_

Testing Suite Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Coverage <https://pypi.python.org/pypi/coverage>`_
-  `Flake8 <https://pypi.python.org/pypi/flake8>`_
-  `Mock <https://pypi.python.org/pypi/mock>`_
-  `Nose <https://nose.readthedocs.io/en/latest>`_

Documentation Building Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Sphinx <https://sphinx-doc.org>`_

Continuum Analytics Anaconda
----------------------------

Since a few years, `Anaconda <https://www.continuum.io/downloads>`_ from
*Continuum Analytics* is the Python distribution we use to develop **Colour**:
it ships all the scientific dependencies we require and is easily deployed
cross-platform.

Colour is available on *conda* and can be installed as follows:

.. code:: shell

    conda install -c conda-forge colour-science

This *asciicast* demonstrates how to generate a pristine Python *conda*
environment for Colour:

.. raw:: html

    <script type="text/javascript" src="https://asciinema.org/a/125160.js" id="asciicast-125160" async data-speed=3></script>

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

    <script type="text/javascript" src="https://asciinema.org/a/125159.js" id="asciicast-125159" async data-speed=3></script>

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
