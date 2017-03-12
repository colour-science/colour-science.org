.. title: Colour 0.3.9, Colour - HDRI 0.1.2 and ACES - Retrospective and Enhancements!
.. slug: colour-039-colour-hdri-012-aces-retrospective-and-enhancements
.. date: 2017-03-12 05:29:15 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

The website has been quiet recently but it does not mean nothing happened!

`Colour 0.3.9 <https://github.com/colour-science/colour/releases/tag/v0.3.9>`_
has been released, `Colour - HDRI 0.1.2 <https://github.com/colour-science/colour-hdri/releases/tag/v0.1.2>`_
was also released and the ACES community has addressed an important feedback paper
to the Academy.

.. TEASER_END

`Colour 0.3.9 <https://github.com/colour-science/colour/releases/tag/v0.3.9>`_
has been released!

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
    colourspaces Normalised Primary Matrices were replaced with the litterature
    ones: *ACES Primaries 0*, *Adobe RGB (1998)*, *ALEXA Wide Gamut RGB*, *CIE RGB*,
    *ROMM RGB*, *sRGB*, *V-Gamut*. This introduces small computation discrepancies
    compared to Colour 0.3.8.
-   Implement support for Canon Log 2 and Canon Log 3 log curves.
-   Implement support for RedWideGamut RGB colourspace and Log3G10, Log3G12 log curves.
-   Implement support for ACEScct colourspace and ACEScct log curves.

Visit the `releases page <https://github.com/colour-science/colour/releases/tag/v0.3.9>`_
for complete details.
