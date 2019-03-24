.. title: Colour 0.3.12 is available!
.. slug: colour-0312-is-available
.. date: 2019-03-24 03:47:21 UTC
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

After over a year of work, `Colour 0.3.12 <https://github.com/colour-science/colour/releases/tag/v0.3.12>`_
is finally released!

.. TEASER_END

Colour 0.3.12
-------------

This release is another important 700+ commits step on
`The Road to Stable <https://www.colour-science.org/posts/the-road-to-stable/>`_!

First and foremost, a huge thanks to all the contributors, whether they are
directly contributing with code or through public or private discussions.

This release was severely delayed because of the involvement of some of us in
the authoring of the upcoming `Cinematic Color <http://cinematiccolor.org>`_
update. `Colour <https://github.com/colour-science/colour/>`_ is used to produce
an important amount of figures in this work and it was important to improve the
plotting capabilities.

The highlights of this release are:

Plotting Package Overhaul
=========================

The `colour.plotting` sub-package was extensively overhauled. It is less
opinionated and more flexible. The plotting definitions have been renamed and
start with *plot_*, they return the current `figure` and `axes`. The
`Cinematic Color 2 - Figures Google Colab <https://colab.research.google.com/drive/1bmVU8fI1Rv3GLXK8kVDovc2K2roGjW9G#scrollTo=Uu08qHeDc11C>`_
document is a good example highlighting the greatest and latest changes and
capabilities.

Default to CIE Standard Illuminant D Series D65
===============================================

The *CIE Standard Illuminant D Series D65* was made the default illuminant in
places where *CIE Illuminant D Series D50* was used as the default argument.

A few reasons for this choice, first *D65* is a *Standard* CIE illuminant
(along with *A*), second *Colour* is used mainly in computer graphics thus it
makes sense to adopt *D65* where it is ubiquitous, and, finally, it brings
consistency across the API while preventing some errors from users with less
expertise in the field.

Domain-Range Scales
===================

The colour science field adopts many input domains and output ranges. Those are
challenging when designing an API. Picking a unique domain-range scale over an
other has caused surprise and grief to practitioners of different industries in
other software.

[Colour](https://github.com/colour-science/colour/) has always used the
domain-range scales of the publications it implements while recognizing the
need for a unique domain-range scale. The API can be switched to use a soft
normalised scale to domain-range [0, 1] using the
`colour.set_domain_range_scale` definition and the `colour.domain_range_scale`
context manager. More information about
`Domain-Range Scales <https://colour.readthedocs.io/en/develop/basics.html#domain-range-scales>`_
is available in the `documentation <https://colour.readthedocs.io/>`_.

Look-Up-Tables IO
-----------------

With this release, `Colour <https://github.com/colour-science/colour/>`_ is now
able to read and write Look-Up-Tables (LUTs) of various dimensions, i.e. LUT1D,
LUT3x1D, LUT3D and LUT Sequences.

Polynomial Colour Correction
----------------------------

Polynomial colour correction was added, it is a useful tool to correct for
non-linearity of data, for example, film stocks colours. With great powers come
great responsibilities and polynomials will eventually alter significantly
colour data that is not present in the original fitting set.

Windows and macOs CI
--------------------

Support for Azure Pipelines was added by @MichaelMauderer giving for the first
time continuous integration on macOS and Windows, a few Windows related issues
were addressed.

Contrast Sensitivity Function
-----------------------------

The *Barten (1999)* contrast sensitivity function was implemented and can be
used to estimate ideal code values as a function of viewing conditions.

Miscellaneous
-------------

The *power* word and abbreviation has been removed from all the spectral
distribution related objects. Likewise, the word *spectral* has been removed
from all the related objects and replaced with *sd*.

The built documentation has been removed from the
`PyPi package <https://pypi.org/project/colour-science/>`_ to reduce the size
of the downloads.

Please refer to the `releases page <https://github.com/colour-science/colour/releases/tag/v0.3.12>`_
for complete details.
