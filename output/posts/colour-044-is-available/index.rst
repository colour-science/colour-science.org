.. title: Colour 0.4.4 is available!
.. slug: colour-044-is-available
.. date: 2023-12-17 04:26:42 UTC
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

The colour-science Developers are pleased to announce the release of
`Colour 0.4.4 <https://github.com/colour-science/colour/releases/tag/v0.4.4>`__!

.. TEASER_END

This release implements support for `Python 3.12 <https://docs.python.org/3/whatsnew/3.12.html>`__

`colour-visuals <https://github.com/colour-science/colour-visuals>`__ was made
public: It is a new repository implementing various WebGPU-based visuals on top
of **Colour** and `pygfx <https://github.com/pygfx/pygfx>`__.

.. image:: https://raw.githubusercontent.com/colour-science/colour-visuals/develop/docs/_static/Visuals_001.png

The highlights of this release are as follows:

-   We have solved the clash with https://github.com/vaab/colour by loading a
    known subset of the objects given by vaab/colour-0.1.5 into our namespace
    if the `COLOUR_SCIENCE__COLOUR__IMPORT_VAAB_COLOUR=True` environment
    variable is defined.
-   Support for Apple Log Profile

Please take a look at the `releases <https://github.com/colour-science/colour/releases/tag/v0.4.4>`__
page more information.
