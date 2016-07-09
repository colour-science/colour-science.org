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

-  `Python 2.7 <https://www.python.org/download/releases/>`_ or
   `Python 3.5 <https://www.python.org/download/releases/>`_
-  `NumPy <http://www.numpy.org/>`_
-  `SciPy <http://www.scipy.org/>`_

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

Pypi
----

**Colour** can be easily installed from the
`Python Package Index <https://pypi.python.org/pypi/colour-science/>`_ by
issuing this command in a shell:

.. code:: shell

    pip install colour-science

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
