.. title: Support for Common LUT Format in Colour available!
.. slug: support-for-clf-in-colour-available
.. date: 2025-04-16 13:47:44 UTC+01:00
.. tags: colour, colour science, release, clf, colour clf io
.. category:
.. link:
.. description:
.. type: text

We are happy to announce the release of `Colour - CLF IO <https://github.com/colour-science/colour-clf-io>`__.

This extension package for **Colour** implements reading and writing files in the **Common LUT Format (CLF)**, as well as
using Colour to execute  workflows defined in CLF.

.. TEASER_END

What is CLF?
------------

One common way of transforming and communicating colours are Look-Up tables (LUTs) that provide a one-to-one mapping
between an input and output colour. In recent years, a new format for storing and exchanging LUTs has emerged:
the **Common LUT Format (CLF)**. This format provides (1) a flexible way to describe colour transformations through LUTs,
(2) supports describing more complex colour transformations through combinations of LUTs and mathematical functions,
and (3) provides standard ways to provide metadata and comments to the colour transformations. This makes it an ideal
format for storing and exchanging annotated colour transformations. The format itself is well described by a
`standard released as part of the Academy Color Encoding System <https://docs.acescentral.com/specifications/clf/>`__.

**CLF** is an XML-based format that describes a transformation of input colours to output colours. It contains a
*ProcessList* that consists of *ProcessNodes* that describes a certain transformation, for example, the application
of a LUT, or some other mathematical transformation. Each *ProcessNodes* is described in the standard and has a
number of parameters that specify its behaviour. The overall transformation is thus described through the sequential
application of all *ProcessNodes* in the *ProcessList*. Furthermore, CLF provides facilities for storing metadata
about the *ProcessList* and each *ProcessNode*, e.g., comments, descriptions of the expected input and output. This
metadata allows **CLF** to contain rich information and descriptions of the colour transformation described within it.

Features
--------
The `Colour - CLF IO <https://github.com/colour-science/colour-clf-io>`__ package allows

- Reading **CLF** 3.0 files to a Python representation.
- Writing **CLF** files from the Python representation. Supporting both **CLF** 3.0 and the upcoming SMPTE ST 2136-1 standard.
- Executing **CLF** workflows and applying them to colours or images.

More Information
----------------
Visit the `Colour - CLF IO <https://github.com/colour-science/colour-clf-io>`__ repository for more information,
usage examples and tutorials.

Funding
-------
We would like to thank `NumFOCUS <https://numfocus.org>`__
for funding the work on this package through the
`The Small Development Grants program  <https://numfocus.org/programs/small-development-grants>`__.
