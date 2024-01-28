.. title: Development Environment on MacOS
.. slug: dev-env-macos
.. date: 2023-07-25 05:35:44 UTC
.. tags: contributing
.. category:
.. link:
.. description:
.. type: text

This is a helpful guide for working on colour-science projects in MacOS. It's by
no means prescriptive, and not every step is required. But if you want a
reasonable, `VS Code <https://code.visualstudio.com/>`__ based development environment this guide may be helpful.
Additionally, this guide installs some of the more obtuse dependencies like
OpenImageIO and graphviz. 

It was contributed by `@tjdcs <https://github.com/tjdcs>`__ and last updated on 2023/07/25


Installation
============

Install Homebrew:

.. code:: shell
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install python versions. 

.. code:: shell

    brew install python@3.9 python@3.10 python@3.11

(Re)Install poetry

Poetry has a nasty habit of having breaking changes to the installer between
minor versions, so we force uninstall and re-install.

.. code:: shell

    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    curl -sSL https://install.python-poetry.org | python3 -


Install graphviz and OpenImageIO
================================

First:

.. code:: shell

    brew install graphviz OpenImageIO

Then add the following to your shell config, usually ~/.zshrc

.. code:: shell

    export LIBRARY_PATH=$LIBRARY_PATH:$(brew --prefix graphviz)/lib/
    export CPATH=$CPATH:$(brew --prefix graphviz)/include/
    export PYTHONPATH=$PYTHONPATH:$(brew --prefix OpenImageIO)/lib/python3.11/site-packages/OpenImageIO/


Clone colour-science
====================

First `fork the colour repository <https://github.com/colour-science/colour/fork>`__

Be sure to set or replace the environment variables in these commands. 
.. code:: shell
    
    cd $DEVELOPMENT_DIR
    git clone git@github.com:$GITHUB_USER/colour.git
    cd colour


Working in VSCode / Terminal
============================

It's optional,  but helpful to put the poetry environment in the local
directory.

.. code:: shell

    poetry config virtualenvs.in-project true


Install the poetry environment


.. code:: shell

    poetry env use 3.11
    poetry install --all-extras


Finally
=======

Open up VS Code and get to work!

.. code:: shell
    
    code .

P.S. if you don't have the code command installed into your shell environment,
open up VS Code manually and then press cmd-shift-p to bring up the command
pallet. Then type "install code command" and press enter. Cheers!

Running Tests / Pre-PR
======================

colour-science uses the invoke framework to build several useful preflight
commands:

.. code:: shell

    cd $DEVELOPMENT_DIR/colour-science
    poetry shell
    invoke formatting  && invoke quality && invoke precommit && invoke tests

or if you just want to run the tests, including doc-tests

.. code:: shell
    
    invoke tests


More Information
================

Refer to the rest of `the contributing guide. <https://www.colour-science.org/contributing/>`__


Install CTL Tools (Optional)
============================

The AMPAS Color Transform List Tools are used in some examples and
documentation. If you want to be able to fully build and contrubute to any part
of the colour-science codebase, this is helpful. The version that is currently
provided by homebrew does not appear to work on the latest MacOS and relevent
environments and it should be installed from source. Thankfully, the builder is
very reliable. 

.. code:: shell

    brew install cmake ilmBase openexr libtiff aces_container 

    cd $TMPDIR
    mkdir CTL_build

    git clone git@github.com:ampas/CTL.git

    cd CTL

    mkdir build && cd build
    cmake .. -J 10
    make
    sudo make install
