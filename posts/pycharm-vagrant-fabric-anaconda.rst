.. title: PyCharm, Vagrant, Fabric & Anaconda
.. slug: pycharm-vagrant-fabric-anaconda
.. date: 2014-09-06 02:45:00 AM GMT+12
.. tags: anaconda, fabric, pycharm, vagrant
.. category:
.. link:
.. description:
.. type: text

.. class:: alert alert-dismissible alert-warning

    | **Warning**
    |
    | Our *Vagrant* setup is now using *Ansible* and *Poetry*, please refer to the
        `PyCharm, Vagrant, Ansible & Poetry </posts/pycharm-vagrant-ansible-poetry>`__ post.

Installing the whole development toolchain for **Colour** roughly means
deploying:

-   `python>=2.7 <https://www.python.org/download/releases>`__ and
    `python>=3.6 <https://www.python.org/download/releases>`__
-   `numpy <https://pypi.org/project/numpy>`__
-   `scipy <https://pypi.org/project/scipy>`__
-   `six <https://pypi.org/project/six>`__
-   `coverage <https://pypi.org/project/coverage>`__
-   `flake8 <https://pypi.org/project/flake8>`__
-   `invoke <https://pypi.org/project/invoke>`__
-   `matplotlib <https://pypi.org/project/matplotlib>`__
-   `mock <https://pypi.org/project/mock>`__
-   `nikola <https://pypi.org/project/Nikola>`__
-   `nose <https://pypi.org/project/nose>`__
-   `openimageio <https://github.com/OpenImageIO/oiio>`__
-   `pandas <https://pypi.org/project/pandas>`__
-   `restructuredtext-lint <https://pypi.org/project/restructuredtext-lint>`__
-   `sphinx <https://pypi.org/project/Sphinx>`__
-   `sphinx-rtd-theme <https://pypi.org/project/sphinx-rtd-theme>`__
-   `sphinxcontrib-bibtex <https://pypi.org/project/sphinxcontrib-bibtex>`__
-   `twine <https://pypi.org/project/twine>`__
-   `yapf==0.23.0 <https://pypi.org/project/yapf>`__
-   `apache 2.2 <http://httpd.apache.org>`__
-   ... and too many things I just don't remember!

I decided to see how I could make that setup a bit more portable and easier to
deploy.

That's where `Vagrant <https://www.vagrantup.com>`__ kicks in along
`PyCharm <http://www.jetbrains.com/pycharm>`__  and
`Anaconda <https://store.continuum.io/cshop/anaconda>`__!

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
    repository:

.. code:: shell

    $ git clone git://github.com/colour-science/colour-vagrant.git

-   You should now have a :code:`colour-vagrant` directory nested into the
    :code:`colour-science` one.

    Let's open the :code:`colour-vagrant` directory into *PyCharm*.

Vagrant Installation
--------------------

We will loosely follow
`Jetbrain's PyCharm Documentation <http://www.jetbrains.com/pycharm/quickstart/configuring_for_vm.html>`__.

-   Install `VirtualBox <https://www.virtualbox.org>`__.
-   Install `Vagrant <https://www.vagrantup.com>`__.
-   Install `Fabric <http://www.fabfile.org>`__, this is the provider needed for
    the `colour-vagrant <https://github.com/colour-science/colour-vagrant>`__
    environment. Initially, I was provisioning with `Puppet <http://puppetlabs.com>`__.
    It was cumbersome to use, so I decided to go for `Fabric <http://www.fabfile.org>`__
    and the `vagrant-fabric <https://github.com/wutali/vagrant-fabric>`__
    plugin:

    .. code:: shell

        $ pip install --user fabric

.. class:: alert alert-dismissible alert-warning

    | **Note**
    |
    | `Fabric <http://www.fabfile.org>`__ does
        `not support Python 3 yet <https://github.com/fabric/fabric/issues/1424>`__
        thus if you want to use Python 3 you will need to
        `switch to the fork <https://pypi.org/project/Fabric3>`__.

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

-   Set the :code:`Vagrant Executable` field to your *Vagrant* executable, e.g.
    :code:`/usr/local/bin/vagrant`. This should not be required as
    :code:`vagrant` should be enough, but
    `I encountered issues lately <https://youtrack.jetbrains.com/issue/PY-29806#comment=27-2846352>`__.

-   Set the :code:`Instance Folder` field to your :code:`colour-vagrant`
    directory.

-   Add a new `Vagrant <https://www.vagrantup.com>`__ box to
    `PyCharm <http://www.jetbrains.com/pycharm>`__ in the :code:`Boxes` tab
    and use the following image:
    `bento/ubuntu-16.04 <https://vagrantcloud.com/bento/boxes/ubuntu-16.04/versions/201808.24.0/providers/vmware_desktop.box>`__

-   Add the `vagrant-fabric <https://github.com/wutali/vagrant-fabric>`__
    plugin to `PyCharm <http://www.jetbrains.com/pycharm>`__ in the
    :code:`Plugins` tab.

Your configuration screen should be approximately as follows:

.. image:: /images/Blog_PyCharm_Vagrant_001.png
.. image:: /images/Blog_PyCharm_Vagrant_002.png

Vagrant Up
----------

With everything setup, hit the :code:`PyCharm --> Tools --> Vagrant --> Up`
menu item to spin up the virtual machine.

You can go grab a coffee, the initial provisioning will take roughly
25-30 minutes.

If the provisioning ended smoothly, you should have the following
elements available:

-   **colour** and **colour-science.org** repositories
    cloned into the :code:`colour-science` directory right next to the
    :code:`colour-vagrant` one.

-   Remote Python environments installed into the virtual machine at the
    following location with all the dependencies needed:

.. code:: shell

    $ cd /home/vagrant/miniconda/envs/
    $ ls -l
    total 16
    drwxrwxr-x  4 vagrant vagrant 4096 Apr 29 03:12 ./
    drwxrwxr-x 13 vagrant vagrant 4096 Apr 29 03:02 ../
    drwxrwxr-x 20 vagrant vagrant 4096 Apr 29 03:09 python2.7/
    drwxrwxr-x 20 vagrant vagrant 4096 Apr 29 03:30 python3.5/

-  The **colour-science.org** website served from the virtual machine at
   the following address: `http://localhost:8080/ <http://localhost:8080>`__

PyCharm Environment Configuration
---------------------------------

-   Add the various remote Python interpreters to
    `PyCharm <http://www.jetbrains.com/pycharm>`__ the
    `Configure a remote interpreter using Vagrant <https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-virtual-boxes.html>`__ guide:

    -   /home/vagrant/miniconda/envs/python2.7/bin/python
    -   /home/vagrant/miniconda/envs/python3.5/bin/python

-   Add the paths mappings from the *macOS* host to the virtual
    machine in the :code:`Defaults` configurations, in my case the mappings
    are as follows:

    ``/Users/KelSolaar/Documents/Development/colour-science = /colour-science``

Your Run/Debug configuration screen should be approximately looking like that:

.. image:: /images/Blog_PyCharm_Configurations_001.png
.. image:: /images/Blog_PyCharm_Configurations_002.png

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
    $ ipython notebook --pylab=inline --ip=0.0.0.0

Then you can access it on the *macOS* host at the following url:
`http://localhost:8888/ <http://localhost:8888>`__

Remote Python Environments & Interpreters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can activate the remote Python environments in the virtual machine by
issuing those commands:

For **python2.7**:

.. code:: shell

    $ source activate python2.7

For **python3.5**:

.. code:: shell

    $ source activate python3.5
