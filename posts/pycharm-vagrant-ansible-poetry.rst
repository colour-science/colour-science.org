.. title: PyCharm, Vagrant, Ansible & Poetry
.. slug: pycharm-vagrant-ansible-poetry
.. date: 2019-11-09 02:46:40 UTC
.. tags: pycharm, vagrant, ansible, poetry
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | This post is an update to the
        `PyCharm, Vagrant, Fabric & Anaconda </posts/pycharm-vagrant-fabric-anaconda>`__ post.

Installing the whole development toolchain for **Colour** roughly means
deploying:

-   `python>=3.6 <https://www.python.org/download/releases>`__
-   `imageio <http://imageio.github.io>`__
-   `scipy <https://pypi.org/project/scipy>`__
-   `six <https://pypi.org/project/six>`__
-   `networkx <https://pypi.org/project/networkx>`__
-   `openimageio <https://github.com/OpenImageIO/oiio>`__
-   `pandas <https://pypi.org/project/pandas>`__
-   `matplotlib <https://pypi.org/project/matplotlib>`__
-   `graphviz <https://www.graphviz.org>`__
-   `pygraphviz <https://pypi.org/project/pygraphviz>`__
-   `backports.functools_lru_cache <https://pypi.org/project/backports.functools-lru-cache>`__
-   `biblib-simple <https://pypi.org/project/biblib-simple>`__
-   `coverage <https://pypi.org/project/coverage>`__
-   `coveralls <https://pypi.org/project/coveralls>`__
-   `flake8 <https://pypi.org/project/flake8>`__
-   `invoke <https://pypi.org/project/invoke>`__
-   `jupyter <https://pypi.org/project/jupyter>`__
-   `mock <https://pypi.org/project/mock>`__
-   `nbformat>=4 <https://pypi.org/project/nbformat>`__
-   `nose <https://pypi.org/project/nose>`__
-   `pre-commit <https://pypi.org/project/pre-commit>`__
-   `pytest <https://pypi.org/project/pytest>`__
-   `restructuredtext-lint <https://pypi.org/project/restructuredtext-lint>`__
-   `sphinx <https://pypi.org/project/Sphinx>`__
-   `sphinx-rtd-theme <https://pypi.org/project/sphinx-rtd-theme>`__
-   `sphinxcontrib-bibtex <https://pypi.org/project/sphinxcontrib-bibtex>`__
-   `twine <https://pypi.org/project/twine>`__
-   `yapf==0.23.0 <https://pypi.org/project/yapf>`__
-   ... and too many things I just don't remember!

I decided to see how I could make that setup a bit more portable and easier to
deploy.

That's where `Vagrant <https://www.vagrantup.com>`__ kicks in along
`PyCharm <http://www.jetbrains.com/pycharm>`__, `Ansible <https://www.ansible.com>`__
and `Poetry <https://poetry.eustace.io>`__!

The following guide assume that you have that you have *PyCharm* installed and
are using *macOS*, although it should pretty much be platform agnostic.

.. TEASER_END

Development Workspace Creation
------------------------------

-   On your local filesystem, in your development workspace, create a
    directory :code:`colour-science` and :code:`cd` into it:

.. code:: shell

    $ mkdir colour-science
    $ cd colour-science

-   Clone the `colour-vagrant <https://github.com/colour-science/colour-vagrant>`__
    repository and initialise the submodules:

.. code:: shell

    $ git clone git://github.com/colour-science/colour-vagrant.git
    $ cd colour-vagrant
    $ git submodule update --init --recursive

-   You should now have a :code:`colour-vagrant` directory nested into the
    :code:`colour-science` one.

    Let's open the :code:`colour-vagrant` directory into *PyCharm*.

Vagrant Installation
--------------------

We will loosely follow
`Jetbrain's PyCharm Documentation <http://www.jetbrains.com/pycharm/quickstart/configuring_for_vm.html>`__.

-   Install `VirtualBox <https://www.virtualbox.org>`__.
-   Install `Vagrant <https://www.vagrantup.com>`__.
-   Install `XQuartz <http://xquartz.macosforge.org>`__: This is the X11 display
    server for *macOS*. The virtual machine will export the display to it
    so that you can see the figures from `Matplotlib <http://matplotlib.org>`__.

-   *VirtualBox* directories syncing performance degrades quickly with large
    number of files.

    As a result the directories syncing is done with *NFS*.

    You will however be asked for your *macOS* password at each virtual
    machine spin up because *Vagrant* needs to modify configuration files on
    the *macOS* host.

    In order to avoid that and following the
    `Vagrant Documentation <https://docs.vagrantup.com/v2/synced-folders/nfs.html>`__,
    you can edit your *macOS* :code:`/etc/sudoers` file and append the
    following content:

    ::

        Cmnd_Alias VAGRANT_EXPORTS_ADD = /usr/bin/tee -a /etc/exports
        Cmnd_Alias VAGRANT_NFSD = /sbin/nfsd restart
        Cmnd_Alias VAGRANT_EXPORTS_REMOVE = /usr/bin/sed -E -e /*/ d -ibak /etc/exports
        %admin ALL=(root) NOPASSWD: VAGRANT_EXPORTS_ADD, VAGRANT_NFSD, VAGRANT_EXPORTS_REMOVE

PyCharm Vagrant Configuration
-----------------------------

The canonical way is to use *Vagrant* from the command line as described in
`Vagrant Documentation <https://docs.vagrantup.com/v2/getting-started>`__, but
here we will leverage the *PyCharm* integration.

-   Set the :code:`Vagrant Executable` field to your *Vagrant* executable, e.g.,
    :code:`/usr/local/bin/vagrant`. This should not be required as
    :code:`vagrant` should be enough, but
    `I encountered issues lately <https://youtrack.jetbrains.com/issue/PY-29806#comment=27-2846352>`__.

-   Set the :code:`Instance Folder` field to your :code:`colour-vagrant`
    directory.

-   Add a new `Vagrant <https://www.vagrantup.com>`__ box to
    `PyCharm <http://www.jetbrains.com/pycharm>`__ in the :code:`Boxes` tab
    and use the following image:
    `bento/ubuntu-18.04 <https://app.vagrantup.com/bento/boxes/ubuntu-18.04/versions/201910.20.0>`__

Your configuration screen should be approximately as follows:

.. image:: /images/Blog_PyCharm_Vagrant_003.png

Vagrant Up
----------

With everything setup, hit the :code:`PyCharm --> Tools --> Vagrant --> Up`
menu item to spin up the virtual machine.

You can go grab a coffee, the initial provisioning will take roughly 45 minutes.

If the provisioning ended smoothly, you should have the following
elements available:

-   The following repositories cloned into the :code:`colour-science` directory
    right next to the :code:`colour-vagrant` one:

    -   `Awesome Colour <https://github.com/colour-science/awesome-colour>`__
    -   `Colour <https://github.com/colour-science/colour>`__
    -   `Colour - Checker Detection <https://github.com/colour-science/colour-checker-detection>`__
    -   `Colour - Analysis - Three.js <https://github.com/colour-science/colour-analysis-three.js>`__
    -   `Colour - Datasets <https://github.com/colour-science/colour-datasets>`__
    -   `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`__
    -   `Colour - Dash <https://github.com/colour-science/colour-dash>`__
    -   `Colour - HDRI <https://github.com/colour-science/colour-hdri>`__
    -   `colour-science.org <https://github.com/colour-science/colour-science.org>`__
    -   `Colour - Branding <https://github.com/colour-science/colour-branding>`__
    -   `Colour - Analysis <https://github.com/colour-science/colour-analysis>`__
    -   `Colour - Nuke <https://github.com/colour-science/colour-nuke>`__
    -   `Colour - Ocean <https://github.com/colour-science/colour-ocean>`__
    -   `Colour - Playground <https://github.com/colour-science/colour-playground>`__
    -   `Colour - Spectroscope <https://github.com/colour-science/colour-spectroscope>`__
    -   `Colour - Webhook <https://github.com/colour-science/colour-webhook>`__

-  Remote Python environments installed into the virtual machine at the
   following location with all the dependencies needed:

.. code:: shell

    $ cd /home/vagrant/.cache/pypoetry/virtualenvs
    $ ls -l
    total 40
    drwxrwxr-x 6 vagrant vagrant 4096 Nov  3 09:45 awesome-colour-xc1lGgeX-py3.6
    drwxrwxr-x 8 vagrant vagrant 4096 Nov  3 09:58 colour-analysis-ztt4I_b6-py3.6
    drwxrwxr-x 7 vagrant vagrant 4096 Nov  3 09:55 colour-checker-detection-LJan8R0H-py3.6
    drwxrwxr-x 8 vagrant vagrant 4096 Nov  3 10:07 colour-dash-yRMdyS1F-py3.6
    drwxrwxr-x 7 vagrant vagrant 4096 Nov  3 10:01 colour-datasets-68eTMDT3-py3.6
    drwxrwxr-x 8 vagrant vagrant 4096 Nov  3 10:05 colour-demosaicing-Me5Z4P5l-py3.6
    drwxrwxr-x 8 vagrant vagrant 4096 Nov  3 10:11 colour-hdri--Cpkjfr--py3.6
    drwxrwxr-x 8 vagrant vagrant 4096 Nov  3 09:52 colour-O_tqvl_6-py3.6
    drwxrwxr-x 6 vagrant vagrant 4096 Nov  3 10:12 colour-science.org-k8ouBR-B-py3.6
    -rw-rw-r-- 1 vagrant vagrant  520 Nov  3 10:12 envs.toml

PyCharm Environment Configuration
---------------------------------

-   Add the various remote Python interpreters you intend to use to
    `PyCharm <http://www.jetbrains.com/pycharm>`__ the
    `Configure a remote interpreter using Vagrant <https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-virtual-boxes.html>`__ guide:

    -   /home/vagrant/.cache/pypoetry/virtualenvs/colour-O_tqvl_6-py3.6/bin/python
    -   /home/vagrant/.cache/pypoetry/virtualenvs/colour-demosaicing-Me5Z4P5l-py3.6/bin/python
    -   ...

-   Add the paths mappings from the *macOS* host to the virtual
    machine in the :code:`Defaults` configurations, in my case the mappings
    are as follows:

    ``/Users/KelSolaar/Documents/Development/colour-science = /colour-science``

Your Run/Debug configuration screen should be approximately looking like that:

.. image:: /images/Blog_PyCharm_Configurations_003.png
.. image:: /images/Blog_PyCharm_Configurations_004.png

Usage
-----

SSH Connection & Display
^^^^^^^^^^^^^^^^^^^^^^^^

Accessing the virtual machine is done by using
:code:`PyCharm --> Tools Start SSH session...` menu item.

However if you want to be able to export the display and see the figures you
will have to manually :code:`ssh` into the virtual machine:

.. code:: shell

    $ ssh -X vagrant@192.168.32.64

Password is :code:`vagrant`.

You will also need to add the virtual machine to the X11 hosts by issuing the
following command on the *macOS* host:

.. code:: shell

    $ xhost + 192.168.32.64

Jupyter Notebooks
^^^^^^^^^^^^^^^^^

The `Jupyter Notebooks <http://ipython.org/notebook.html>`__ server is started
as follows:

.. code:: shell

    $ cd /colour-science
    $ jupyter notebook --pylab=inline --ip=0.0.0.0

Then you can access it on the *macOS* host at the following url:
`http://localhost:8888/ <http://localhost:8888>`__

Remote Python Environments & Interpreters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can activate the remote Python environments in the virtual machine by
issuing those commands:

For **Colour**:

.. code:: shell

    $ colour
    Using virtualenv: /home/vagrant/.cache/pypoetry/virtualenvs/colour-O_tqvl_6-py3.6

For **Colour - Demosaicing**:

.. code:: shell

    $ colour-demosaicing
    Using virtualenv: /home/vagrant/.cache/pypoetry/virtualenvs/colour-demosaicing-Me5Z4P5l-py3.6

A full list is available as follows:

.. code:: shell

    $ alias | grep colour-science
    alias awesome-colour='cd /colour-science/awesome-colour && poem'
    alias colour='cd /colour-science/colour && poem'
    alias colour-analysis-three.js='cd /colour-science/colour-analysis-three.js && poem'
    alias colour-checker-detection='cd /colour-science/colour-checker-detection && poem'
    alias colour-dash='cd /colour-science/colour-dash && poem'
    alias colour-datasets='cd /colour-science/colour-datasets && poem'
    alias colour-demosaicing='cd /colour-science/colour-demosaicing && poem'
    alias colour-hdri='cd /colour-science/colour-hdri && poem'
    alias colour-science.org='cd /colour-science/colour-science.org && poem'
