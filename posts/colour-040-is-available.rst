.. title: Colour 0.4.0 is available!
.. slug: colour-040-is-available
.. date: 2022-02-20 08:22:06 UTC
.. tags: colour, colour science, release
.. category:
.. link:
.. description:
.. type: text

We are pleased to announce that after over a year of work,
`Colour 0.4.0 <https://github.com/colour-science/colour/releases/tag/v0.4.0>`__
has been released!

.. TEASER_END

This release integrates most of the
`GSoC 2021 <https://github.com/colour-science/GSoC/blob/master/2020/GSoC-2021-Project-Ideas.md>`__
work from Cédric (`@villirion <https://github.com/villirion>`__), all the code
from Geetansh (`@SGeetansh <https://github.com/SGeetansh>`__) and the remaining
`GSoC 2020 <https://github.com/colour-science/GSoC/blob/master/2020/GSoC-2020-Project-Ideas.md>`__
code from Nishant (`@SGeetansh <https://github.com/njwardhan>`__). We would
like to thank them again for their excellent contributions!

We are finally dropping `Python 2.7 <https://www.python.org/downloads/release/python-270>`__
support and the minimal version is now `Python
3.8 <https://www.python.org/downloads/release/python-380>`__ as per
`https://scientific-python.org/ <https://scientific-python.org/specs/spec-0000>`__.

The following minimal dependency versions are also required:

-   `imageio >= 2, < 3 <https://imageio.github.io>`__
-   `numpy >= 1.19, < 2 <https://pypi.org/project/numpy>`__
-   `scipy >= 1.5, < 2 <https://pypi.org/project/scipy>`__
-   `typing-extensions >= 4, < 5 <https://pypi.org/project/typing-extensions>`__

.. figure:: /images/Blog_Chromaticity_Diagram_CIE1976UCS_Advanced_Customisation.png

The highlights of this release are as follows:

-   **Colour** can on iOS and iPadOS with `Pyto <https://pyto.app>`__.
-   The import of ``colour`` is now 3.6 times faster.
-   Typing annotations have been added and the codebase is checked with
    `Mypy <https://pypi.org/project/mypy>`__.
-   The documentation has been updated and uses the
    `pydata-sphinx-theme <https://pypi.org/project/pydata-sphinx-theme>`__
    and has better compliance with
    `PEP257 <https://www.python.org/dev/peps/pep-0257>`__.
-   The code formatter is now
    `Black <https://pypi.org/project/black>`__.
-   Many Python 3 features such as *f-Strings* or the ``dataclass`` decorator
    have been adopted.
-   The plotting API has been improved to be more consistent when setting the colours of some figures, e.g. spectral or planckian locus.
-   New colour appearance models:

    -   *Zhai and Luo (2018)* chromatic adaptation model.
    -   *Kim, Weyrich and Kautz (2009)* colour appearance model.
    -   *ZCAM* colour appearance model.
    -   *Helmholtz-Kohlrausch* effect estimation.

-   New colour models:

    -   *Oklab* colour model.
    -   *Hanbury (2003)* *IHLS* (Improved HLS) colourspace.
    -   *DIN99b*, *DIN99c*, and *DIN99d* refined formulas.
    -   *ProLab* colourspace.
    -   *Sarifuddin and Missaoui (2005)* *HCL* colourspace.

-   New RGB colourspaces and transfer functions:

    -   *Nikon* *N-Gamut* colourspace and the *N-Log* log encoding.
    -   *Blackmagic Wide Gamut* colourspace and the associated
        *Blackmagic Film Generation 5* OETF.
    -   *DaVinci Intermediate* OETF.
    -   *RED Log3G10* encoding and decoding curves with linear extension.

-   Other notable features:

    -   *R’G’B’* to *Y’CbCr* matrices computation.
    -   Gamut ring/section plotting.
    -   *Rösch-MacAdam* colour solid hue lines.
    -   *Huang et al. (2015)* power-functions.
    -   *LUT 1D*, *LUT 3x1D* and *LUT 3D* inversion.
    -   *UPRTek* and *Sekonic* spectral data parsers.
    -   *SPImtx* LUT input and output.
    -   Support for the `OpenColorIO <https://opencolorio.org>`__ processor.

       -    Note that the optional dependency is not specified in the
            `pyproject.toml`, see AcademySoftwareFoundation/OpenColorIO#1573
            for more information.

Thanks again to all the contributors to this release!

-   `@aforsythe <https://github.com/aforsythe>`__
-   `@fredsavoir <https://github.com/fredsavoir>`__
-   `@ilia3101 <https://github.com/ilia3101>`__
-   `@jedypod <https://github.com/jedypod>`__
-   `@JGoldstone <https://github.com/JGoldstone>`__
-   `@Nick-Shaw <https://github.com/Nick-Shaw>`__
-   `@njwardhan <https://github.com/njwardhan>`__
-   `@Paul-Sims <https://github.com/Paul-Sims>`__
-   `@ramparvathaneni <https://github.com/ramparvathaneni>`__
-   `@romanovar <https://github.com/romanovar>`__
-   `@Saransh <https://github.com/Saransh>`__
-   `@SGeetansh <https://github.com/SGeetansh>`__
-   `@sobotka <https://github.com/sobotka>`__
-   `@villirion <https://github.com/villirion>`__
-   `@zachlewis <https://github.com/zachlewis>`__

Please take a look at the
`releases <https://github.com/colour-science/colour/releases/tag/v0.4.0>`__
page more information.
