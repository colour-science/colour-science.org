.. title: PyCharm, Vagrant, Fabric & Anaconda
.. slug: pycharm-vagrant-fabric-anaconda
.. date: 2014-09-06 02:45:00 AM GMT+12
.. tags: anaconda, fabric, pycharm, vagrant
.. category:
.. link:
.. description:
.. type: text

Installing the whole development toolchain for **Colour** roughly means
deploying:

-   `Python 2.7 <https://www.python.org/download/releases/>`_ and
    `Python 3.5 <https://www.python.org/download/releases/>`_
-   `NumPy <http://www.numpy.org/>`_
-   `Matplotlib <http://matplotlib.org/>`_
-   `SciPy <http://www.scipy.org/>`_
-   `IPython <http://ipython.org/notebook.html>`_
-   `Nose <https://nose.readthedocs.io/en/latest>`_
-   `Coverage <https://pypi.python.org/pypi/coverage>`_
-   `Flake8 <https://pypi.python.org/pypi/flake8>`_
-   `Sphinx <https://sphinx-doc.org>`_
-   `Nikola <https://getnikola.com/>`_
-   `Apache 2.2 <http://httpd.apache.org>`_
-   `OpenImageIO <http://openimageio.org>`_
-   ... and too many things I just don't remember!

I decided to see how I could make that setup a bit more portable and easier to
deploy.

That's where `Vagrant <https://www.vagrantup.com/>`_ kicks in along
`PyCharm <http://www.jetbrains.com/pycharm/>`_  and
`Anaconda <https://store.continuum.io/cshop/anaconda/>`_!

The following guide assume that you have that you have *PyCharm* installed and
are using *macOs*, although it should pretty much be platform agnostic.

.. TEASER_END

Development Workspace Creation
------------------------------

-   On your local filesystem, in your development workspace, create a
    directory :code:`colour-science` and :code:`cd` into it:

.. code:: shell

    mkdir colour-science
    cd colour-science

-   Clone the `colour-vagrant <https://github.com/colour-science/colour-vagrant>`_
    repository:

.. code:: shell

    git clone git://github.com/colour-science/colour-vagrant.git

-   You should now have a :code:`colour-vagrant` directory nested into the
    :code:`colour-science` one.

    Let's open the :code:`colour-vagrant` directory into *PyCharm*.

Vagrant Installation
--------------------

We will loosely follow
`Jetbrain's PyCharm Documentation <http://www.jetbrains.com/pycharm/quickstart/configuring_for_vm.html>`_.

-   Install `VirtualBox <https://www.virtualbox.org/>`_.
-   Install `Vagrant <https://www.vagrantup.com/>`_.
-   Install `Fabric <http://www.fabfile.org/>`_, this is the provider needed for
    the `colour-vagrant <https://github.com/colour-science/colour-vagrant>`_
    environment. Initially, I was provisioning with `Puppet <http://puppetlabs.com/>`_.
    It was cumbersome to use, so I decided to go for `Fabric <http://www.fabfile.org/>`_
    and the `vagrant-fabric <https://github.com/wutali/vagrant-fabric>`_
    plugin:

    .. code:: shell

        pip install fabric

.. class:: alert alert-dismissible alert-warning

    | **Note**
    |
    | `Fabric <http://www.fabfile.org/>`_ does
        `not support Python 3 yet <https://github.com/fabric/fabric/issues/1424>`_
        thus if you want to use Python 3 you will need to
        `switch to the fork <https://pypi.org/project/Fabric3/>`_.

-   Install `XQuartz <http://xquartz.macosforge.org/>`_: This is the X11 display
    server for *macOs*. The virtual machine will export the display to it
    so that you can see the figures from `Matplotlib <http://matplotlib.org/>`_.

-   *VirtualBox* directories syncing performance degrades quickly with large
    number of files.

    As a result the directories syncing is done with *NFS*.

    You will however be asked for your *macOs* password at each virtual
    machine spin up because *Vagrant* needs to modify configuration files on
    the *macOs* host.

    In order to avoid that and following the
    `Vagrant Documentation <https://docs.vagrantup.com/v2/synced-folders/nfs.html>`_,
    you can edit your *macOs* :code:`/etc/sudoers` file and append the
    following content:

    ::

        Cmnd_Alias VAGRANT_EXPORTS_ADD = /usr/bin/tee -a /etc/exports
        Cmnd_Alias VAGRANT_NFSD = /sbin/nfsd restart
        Cmnd_Alias VAGRANT_EXPORTS_REMOVE = /usr/bin/sed -E -e /*/ d -ibak /etc/exports
        %admin ALL=(root) NOPASSWD: VAGRANT_EXPORTS_ADD, VAGRANT_NFSD, VAGRANT_EXPORTS_REMOVE

PyCharm Vagrant Configuration
-----------------------------

The canonical way is to use *Vagrant* from the command line as described in
`Vagrant Documentation <https://docs.vagrantup.com/v2/getting-started/>`__, but
here we will leverage the *PyCharm* integration.

-   Set the :code:`Vagrant Executable` field to your *Vagrant* executable, e.g.
    :code:`/usr/local/bin/vagrant`. This should not be needed as
    :code:`vagrant` should be enough, but
    `I encountered issues lately <https://youtrack.jetbrains.com/issue/PY-29806#comment=27-2846352>`_.

-   Set the :code:`Instance Folder` field to your :code:`colour-vagrant`
    directory.

-   Add a new `Vagrant <https://www.vagrantup.com/>`_ box to
    `PyCharm <http://www.jetbrains.com/pycharm/>`_ in the :code:`Boxes` tab
    and use the following image:
    `bento/ubuntu-16.04 <https://vagrantcloud.com/bento/ubuntu-16.04>`_

-   Add the `vagrant-fabric <https://github.com/wutali/vagrant-fabric>`_
    plugin to `PyCharm <http://www.jetbrains.com/pycharm/>`_ in the
    :code:`Plugins` tab.

Your configuration screen should be approximately as follows:

.. image:: /images/Blog_PyCharm_Vagrant_001.png
.. image:: /images/Blog_PyCharm_Vagrant_002.png

Vagrant Up
----------

With everything setup, hit the :code:`PyCharm ---> Tools ---> Vagrant ---> Up`
menu item to spin up the virtual machine.

You can go grab a coffee, the initial provisioning will take roughly
25-30 minutes.

If the provisioning ended smoothly, you should have the following
elements available:

-  **colour**, **colour-notebooks** and **colour-science.org** repositories
   cloned into the :code:`colour-science` directory right next to the
   :code:`colour-vagrant` one.

-  Remote Python environments installed into the virtual machine at the
   following location with all the dependencies needed:

.. code:: shell

    vagrant@vagrant:~$ cd /home/vagrant/miniconda/envs/
    vagrant@vagrant:~/miniconda/envs$ ll
    total 16
    drwxrwxr-x  4 vagrant vagrant 4096 Apr 29 03:12 ./
    drwxrwxr-x 13 vagrant vagrant 4096 Apr 29 03:02 ../
    drwxrwxr-x 20 vagrant vagrant 4096 Apr 29 03:09 python2.7/
    drwxrwxr-x 20 vagrant vagrant 4096 Apr 29 03:30 python3.5/

-  The **colour-science.org** website served from the virtual machine at
   the following address: `http://localhost:8080/ <http://localhost:8080/>`_

PyCharm Environment Configuration
---------------------------------

-  Add the various remote Python interpreters to
   `PyCharm <http://www.jetbrains.com/pycharm/>`_ following the
   quickstart guide: `Remote interpreter via virtual box:
   2 <http://www.jetbrains.com/pycharm/quickstart/configuring_interpreter.html>`_

   The remote Python interpreters paths are as follows:

   -  /home/vagrant/miniconda/envs/python2.7/bin/python
   -  /home/vagrant/miniconda/envs/python3.5/bin/python

-  Add the paths mappings from the *macOs* host to the virtual
   machine in the :code:`Defaults` configurations, in my case the mappings
   are as follows:

   ``/Users/KelSolaar/Documents/Developement/colour-science = /colour-science``

Your Run/Debug configuration screen should be approximately looking like that:

.. image:: /images/Blog_PyCharm_Configurations_001.png
.. image:: /images/Blog_PyCharm_Configurations_002.png

Usage
-----

SSH Connection & Display
^^^^^^^^^^^^^^^^^^^^^^^^

Accessing the virtual machine is done by using
:code:`PyCharm ---> Tools Start SSH session...` menu item.

However if you want to be able to export the display and see the figures you
will have to manually :code:`ssh` into the virtual machine:

.. code:: shell

    ssh -X vagrant@192.168.32.64

Password is :code:`vagrant`.

You will also need to add the virtual machine to the X11 hosts by issuing the
following command on the *macOs* host:

.. code:: shell

    xhost + 192.168.32.64

Jupyter Notebooks
^^^^^^^^^^^^^^^^^

The `Jupyter Notebooks <http://ipython.org/notebook.html>`_ server is started
as follows:

.. code:: shell

    cd /colour-science/colour-notebooks/notebooks
    ipython notebook --pylab=inline --ip=0.0.0.0

Then you can access it on the *macOs* host at the following url:
`http://localhost:8888/ <http://localhost:8888/>`_

Remote Python Environments & Interpreters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can activate the remote Python environments in the virtual machine by
issuing those commands:

For **python2.7**:

.. code:: shell

    source activate python2.7

For **python3.5**:

.. code:: shell

    source activate python3.5
