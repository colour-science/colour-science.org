.. title: Setting Up the Development Environment on macOS
.. slug: setting-up-the-development-environment-on-macos
.. date: 2023-07-25 05:35:44 UTC
.. tags: contributing
.. category:
.. link:
.. description:
.. type: text

This guide describes the process to setup a development environment for
contributing to colour-science projects on macOS. It is by no means prescriptive,
and not every step is required. The guide assumes `Homebrew <https://brew.sh>`__
as the package manager and `Visual Studio Code <https://code.visualstudio.com/>`__
as the IDE / text editor.

Additionally, the installation of complex dependencies such as
`OpenImageIO <https://github.com/OpenImageIO/oiio>`__ and
`PyGraphviz <https://pypi.org/project/pygraphviz>`__ is described.

It was contributed by `@tjdcs <https://github.com/tjdcs>`__ and last updated on
the 2024-01-28.

Homebrew
========

Install `Homebrew <https://brew.sh>`__:

.. code:: shell

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install the required Python versions:

.. code:: shell

    brew install python@3.9 python@3.10 python@3.11 python@3.12

Poetry
======

(Re)Install `Poetry <https://python-poetry.org>`__:

Poetry used to introduce breaking changes to the installer between minor
versions, it is thus recommended to reinstall it.

.. code:: shell

    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    curl -sSL https://install.python-poetry.org | python3 -

graphviz and OpenImageIO
========================

Using Homebrew:

.. code:: shell

    brew install graphviz OpenImageIO

Then append the following exports to your shell dotfile, e.g. ``~/.zshrc``:

.. code:: shell

    export LIBRARY_PATH=$LIBRARY_PATH:$(brew --prefix graphviz)/lib/
    export CPATH=$CPATH:$(brew --prefix graphviz)/include/
    export PYTHONPATH=$PYTHONPATH:$(brew --prefix OpenImageIO)/lib/python3.12/site-packages/OpenImageIO/

Cloning colour's Repository
===========================

First, `fork the colour repository <https://github.com/colour-science/colour/fork>`__,
making sure to set or replace the environment variables in these commands.

.. code:: shell

    cd $DEVELOPMENT_DIRECTORY
    git clone git@github.com:$GITHUB_USER/colour.git
    cd colour

Working with Visual Studio Code from the Terminal
=================================================

The following step is optional, but helpful to store Poetry's virtual environment
into **colour**'s directory.

.. code:: shell

    poetry config virtualenvs.in-project true

Install the poetry environment

.. code:: shell

    poetry env use 3.12
    poetry install --all-extras

Opening Visual Studio Code
==========================

In **colour**'s directory, issue the following command to launch Visual Studio Code:

.. code:: shell

    code .

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | If the code command is not available in your shell environment, open up
        Visual Studio Code from the Applications folder, press ``Cmd + Shift + P``
        to bring up the *Command Palette*, then type
        `Shell Command: Install 'code' command in PATH` and press enter.

Running the Unit Tests / Preflight
==================================

**colour** uses the `invoke <https://pypi.org/project/invoke>`__ framework to
expose several useful preflight commands:

.. code:: shell

    cd $DEVELOPMENT_DIRECTORY/colour
    poetry shell
    invoke formatting && invoke quality && invoke precommit && invoke tests

or if you just want to run the tests, including the doctests:

.. code:: shell

    invoke tests


CTL (Optional)
==============

**colour** provides a wrapper to the AMPAS `Color Transformation Language <https://github.com/ampas/CTL>`__ (CTL)
If you want to be able to fully build and contribute to this part of the
codebase, it needs to be installed. Unfortunately, the version currently
provided by Homebrew does not appear to work on the latest macOS and the relevant
environments, thus, it must be installed from source at the moment:

.. code:: shell

    brew install cmake ilmBase openexr libtiff aces_container

    cd $TMPDIR
    git clone git@github.com:ampas/CTL.git

    cd CTL
    mkdir build && cd build

    cmake .. -J 10
    make
    sudo make install

See Also
========

Please refer to `the contributing guide <https://www.colour-science.org/contributing/>`__
for more information about the contributing process.
