.. title: Colour 0.3.9, Colour - HDRI 0.1.2 and ACES!
.. slug: colour-039-colour-hdri-012-aces
.. date: 2017-03-12 05:29:15 UTC
.. tags: aces, colour, colour science, colour - hdri, release
.. category: 
.. link: 
.. description: 
.. type: text

`colour-science.org <https://www.colour-science.org>`__ has been quiet for a while
however, it does not mean nothing happened. `Colour 0.3.9 <https://github.com/colour-science/colour/releases/tag/v0.3.9>`__
and `Colour - HDRI 0.1.2 <https://github.com/colour-science/colour-hdri/releases/tag/v0.1.2>`__
were released today and last week, concluding a major collaborative effort, the ACES
community addressed an important feedback paper to the Academy leadership.

.. TEASER_END

Colour 0.3.9
------------

This release introduces some significant spectral computations performance
improvements and various new objects:

-   Spectral code optimisations resulting in increased computations performance:

    -   `colour.SpectralPowerDistribution` and `colour.TriSpectralPowerDistribution`
        classes are now **6.5** times faster.
    -   `colour.colour_quality_scale` definition is now **10.5** times faster.
    -   `colour.colour_rendering_index` definition is now **13.1** times faster.
    -   `colour.uv_to_CCT_Ohno2013` definition is now **15.7** times faster.

-   Correlated colour temperature to chromaticity coordinates uv computation
    accordingly to Krystek (1985) method.
-   Support for Luo et al. (2006) CIECAM02 based uniform colourspaces and colour differences.
-   Support for Dolby ICTCP colourspace.
-   Support for Canon Log 2 and Canon Log 3 log curves.
-   `colour.RGB_Colourspace` class can now either use instantiation time
    transformations matrices or derived ones. Consequently, the following RGB
    colourspaces Normalised Primary Matrices were replaced with the literature
    ones: *ACES Primaries 0*, *Adobe RGB (1998)*, *ALEXA Wide Gamut RGB*, *CIE RGB*,
    *ROMM RGB*, *sRGB*, *V-Gamut*. It introduces small computation discrepancies compared to Colour 0.3.8.
-   Implement support for Canon Log 2 and Canon Log 3 log curves.
-   Implement support for RedWideGamut RGB colourspace and Log3G10, Log3G12 log curves.
-   Implement support for ACEScct colourspace and ACEScct log curves.

Colour can now be installed from `conda-forge <https://conda-forge.github.io/>`__:

.. code:: shell

    conda install -c conda-forge colour-science

Visit the `Colour's releases page <https://github.com/colour-science/colour/releases/tag/v0.3.9>`__
for complete details.

Colour - HDRI 0.1.2
-------------------

This release introduces some new capabilities:

-   Support for Adobe DNG SDK colour processing for improved white balancing.
-   Custom CIE LCHab highlights recovery definition.

Visit the `Colour - HDRI's releases page <https://github.com/colour-science/colour-hdri/releases/tag/v0.1.2>`__
for complete details.

ACES
----

Various members of the ACES community addressed a retrospective and enhancements
document about ACES to the Academy leadership. It describes improvements that
the system could implement to increase its adaptability and reach. It is the
result of months of collaborative writing, years of discussions between expert
users and summarizes decades of cumulated experience using the system.

Authors
*******

-   **Sean Cooper**, *Sony Pictures Imageworks*
-   **Thomas Mansencal**, *Wingnut Films Production Ltd.*
-   **Kevin Wheatley**, *Framestore*

Contributors
************

-   **Remi Achard**, *Eclair*
-   **Steve Agland**, *Animal Logic*
-   **Haarm-Pieter Duiker**, *Duiker Research*
-   **Alex Fry**, *Animal Logic*
-   **Brian Karis**, *Epic Games*
-   **Sebastien Lagarde**, *Unity Technologies*
-   **Robert Molholm**, *Industrial Light and Magic*
-   **Michael Parsons**, *The Moving Picture Company*
-   **Nick Shaw**, *Antler Post*

Reviewers
*********
-   **Lars Borg**, *Adobe*
-   **Alasdair Coull**, *Wingnut Films Production Ltd.*
-   **Marie Fetiveau**, *Rodeo FX*
-   **Lucien Fostier**, *Image Engine Design*
-   **Alex Fry**, *Electronic Arts*
-   **Thomas Hourdel**, *Unity Technologies*
-   **Anders Langlands**, *Weta Digital*
-   **Jasmin Patry**, *Sucker Punch*
-   **Troy James Sobotka**, *Freelancer*

The document can be found at this URL: https://doi.org/10.5281/zenodo.345624
and the LaTex code is hosted on `Github <https://github.com/colour-science/aces-retrospective-and-enhancements>`__.
