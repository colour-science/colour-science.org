.. title: Setting Up the Development Environment on macOS
.. slug: setting-up-the-development-environment-on-macos
.. date: 2023-07-25 05:35:44 UTC
.. tags: contributing
.. category:
.. link:
.. description:
.. type: text

This guide covers the macOS setup for contributing to **Colour**.
It uses `Homebrew <https://brew.sh>`__ and includes optional steps for
Visual Studio Code, Graphviz and CTL. It was originally contributed by
`@tjdcs <https://github.com/tjdcs>`__.

Homebrew
========

If you need Homebrew, follow the `official installation instructions
<https://brew.sh>`__.

uv
==

Install `uv <https://docs.astral.sh/uv/>`__:

.. code:: shell

    brew install uv

The project setup below uses Python 3.13, which uv can install automatically.

Cloning Colour's Repository
===========================

`Fork the Colour repository <https://github.com/colour-science/colour/fork>`__,
then replace ``YOUR-GITHUB-USERNAME`` with your GitHub username:

.. code:: shell

    git clone https://github.com/YOUR-GITHUB-USERNAME/colour.git
    cd colour
    git switch develop

Working with Visual Studio Code from the Terminal
=================================================

Create the development environment:

.. code:: shell

    uv sync --python 3.13 --all-extras
    uv run prek install

uv installs OpenImageIO into the project's virtual environment as part of
the optional dependencies.

Opening Visual Studio Code
==========================

From the ``colour`` directory:

.. code:: shell

    code .

If ``code`` is unavailable, open the Command Palette in
`Visual Studio Code <https://code.visualstudio.com/>`__ and run
``Shell Command: Install 'code' command in PATH``. Select the
``.venv/bin/python`` interpreter for the project.

Running the Unit Tests / Preflight
==================================

Run the tests and doctests with:

.. code:: shell

    uv run invoke tests

To run the full preflight, including formatting, static checks, hooks,
tests and examples:

.. code:: shell

    uv run invoke preflight

.. _graphviz-and-openimageio:

Graphviz (Optional)
===================

Install Graphviz if you need to render conversion graphs:

.. code:: shell

    brew install graphviz

CTL (Optional)
==============

Colour's `Color Transformation Language <https://github.com/aces-aswf/CTL>`__
wrapper needs the ``ctlrender`` command. Install the
`Homebrew CTL formula <https://formulae.brew.sh/formula/ctl>`__ if you are
working on that functionality:

.. code:: shell

    brew install ctl

See Also
========

The `contributing guide </contributing/>`__ covers updating your fork,
creating a branch and opening a pull request.
