.. title: Colour 0.4.2 is available!
.. slug: colour-042-is-available
.. date: 2022-12-04 09:01:51 UTC
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

We are pleased to announce that `Colour 0.4.2 <https://github.com/colour-science/colour/releases/tag/v0.4.2>`__
has been released earlier this week!

.. TEASER_END

This release implements support for `Python 3.11 <https://www.python.org/downloads/release/python-3110/>`__.
It includes the remaining contributions of the
`GSoC 2021 <https://github.com/colour-science/GSoC/blob/master/2020/GSoC-2021-Project-Ideas.md>`__
work from Cédric (`@villirion <https://github.com/villirion>`__).

New RGB colourspaces, transfer functions, colour models and colour appearance
models have been added. Various performance improvements have been implemented.

We would like to especially thanks Tucker Downs (`@tjdcs <https://github.com/tjdcs>`__)
for his recent contributions.

With this release, the minimum Python version is `3.9 <https://www.python.org/downloads/release/python-390/>`__
and the following scientific packages minimum versions are required:

-   `numpy >= 1.20 <https://pypi.org/project/numpy/>`__
-   `scipy >= 1.7 <https://pypi.org/project/scipy/>`__
-   `matplotlib >= 3.4 <https://pypi.org/project/matplotlib/>`__
-   `networkx >= 2.6 <https://pypi.org/project/networkx/>`__
-   `pandas >= 1.3 <https://pypi.org/project/pandas/>`__

The highlights of this release are as follows:

-   *Jiang et al. (2013)* camera RGB sensitivities recovery.

-   New colour appearance models:

    -   *Hellwig and Fairchild (2022)* colour appearance model.
    -   *CIECAM16* colour appearance model.

-   New colour models:

    -   *Munish Ragoo and Farup (2021) Optimised IPT* colourspace.

-   New RGB colourspaces and transfer functions:

    -   *Leica L-Log* log encodings.
    -   *ARRI Wide Gamut 4* colourspace and *ARRI LogC4* log encodings.
    -   *Recommendation ITU-T H.273* code points for video signal type identification.

-   `colour.temperature.uv_to_CCT_Ohno2013` definition is ~100x faster.
-   `colour.temperature.CCT_to_uv_Ohno2013` definition is ~425x faster.

Please take a look at the
`releases <https://github.com/colour-science/colour/releases/tag/v0.4.2>`__
page more information.