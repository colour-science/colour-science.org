.. title: Colour 0.4.3 is available!
.. slug: colour-043-is-available
.. date: 2023-08-26 23:51:27 UTC+01:00
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

The colour-science Developers are pleased to announce the release of `Colour 0.4.3 <https://github.com/colour-science/colour/releases/tag/v0.4.3>`__!

.. TEASER_END

We worked on many optimisations around colour quality metrics that should result in overall performance increase, thanks again to Tucker Downs (`@tjdcs <https://github.com/tjdcs>`__) for the heavy lifting!

@charliermarsh's `ruff <https://github.com/charliermarsh/ruff>`__ is now used as a replacement for:

- `flake8 <https://pypi.org/project/flake8>`__
- `pydocstyle <https://pypi.org/project/flake8>`__
- `pyupgrade <https://pypi.org/project/pyupgrade>`__

We also replaced `mypy <https://mypy.readthedocs.io>`__ with `pyright <https://github.com/microsoft/pyright>`__ for performance reasons. We took that opportunity to simplify our type annotations.

The `colour.XYZ_to_RGB` and `colour.RGB_to_XYZ` definition signatures have been changed to be easier to use, please update any code using them. See `#1127 <https://github.com/colour-science/colour/issues/1127>`__ for more information.

With this release, the following scientific packages minimum versions are required:

-   `numpy >= 1.22 <https://pypi.org/project/numpy>`__
-   `scipy >= 1.8 <https://pypi.org/project/scipy>`__
-   `matplotlib >= 3.5 <https://pypi.org/project/matplotlib>`__
-   `networkx >= 2.7 <https://pypi.org/project/networkx>`__
-   `pandas >= 1.4 <https://pypi.org/project/pandas>`__

The highlights of this release are as follows:

-   The *Colour Fidelity Index (2017)*, i.e. `colour.quality.colour_fidelity_index_CIE2017` definition, and *TM 30-18*, i.e. `colour.quality.colour_fidelity_index_ANSIIESTM3018` definition, metrics performance has been improved by x100 thanks to overall optimizations, e.g. `colour.temperature.uv_to_CCT_Ohno2013` definition is x5 faster.
-   `TE226 V2 <https://www.image-engineering.de/content/products/charts/te226/downloads/TE226_D_data_sheet.pdf>`__ colour checker reference values.

-   New colour models:

    -   *Kirk (2019)* *Yrg* colourspace.

-   New RGB colourspaces and encodings:

    -   *Fujifilm F-Log2* encodings.
    -   *PLASA ANSI E1.54* colourspace.

-    *CSS Color 3* keywords
-   New plotting definition for the *Daylight Locus* along with `Mireds <https://en.wikipedia.org/wiki/Mired>`__ plotting support.

Please take a look at the
`releases <https://github.com/colour-science/colour/releases/tag/v0.4.3>`__
page more information.