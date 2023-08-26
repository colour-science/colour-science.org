.. title: Colour 0.3.8 is available!
.. slug: colour-038-is-available
.. date: 2016-07-09 11:33:29 UTC+01:00
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

`Colour 0.3.8 <https://github.com/colour-science/colour/releases/tag/v0.3.8>`__
is available!

.. TEASER_END

More than 7 months in the making, this release introduces substantial backward
incompatible changes:

-   Spectral computations are adopting practise ASTM E2022–11 and ASTM E308–15
    methods to compute tristimulus values from spectral data.
-   D50 and D65 illuminants chromaticity coordinates have been rounded to 4
    decimals to conform better with what most RGB colourspace specifications
    adopt.
-   The RGB colourspace transfer functions implementation has been overhauled in
    order to be easily extended in the future.
-   `SciPy <https://www.scipy.org>`__ is now a requirement.

Please carefully refer to the
`releases page <https://github.com/colour-science/colour/releases/tag/v0.3.8>`__
*Changes* section.

Highlights of this release are:

-   Spectral to tristimulus values computations using ASTM E2022–11 and ASTM E308–15
    methods.
-   Dominant and complementary wavelengths along colour and excitation purity
    computations.
-   Support for YCbCr and YcCbcCrc colour encodings.
-   Support for Hunter Lab and Hunter Rdab colour scales.
-   Support for BT.1886 EOTF and ST 2084 OETF / EOTF.
-   Support for RIMM, ROMM and ERIMM colour encodings.

A `Jupyter Notebook <https://github.com/colour-science/colour-ramblings/blob/master/colour_0_3_8_computational_changes.ipynb>`__
is available to illustrate the expected computational differences. They should
remain orders of magnitude under visual discrimination threshold however they
will likely create computational discrepancies.

`Colour - Demosaicing </colour-demosaicing>`__ and `Colour - HDRI </colour-hdri>`__
packages have been updated accordingly.

Michael and I would like to thanks all the contributors for that release
whether they contribute to the code or participate in discussions.

-   David Bourgeois
-   Luke Canavan
-   Sean Cooper
-   Nick Shaw
-   Ron024
-   Kevin Wheatley

Visit the `releases page <https://github.com/colour-science/colour/releases/tag/v0.3.8>`__
for complete details.

