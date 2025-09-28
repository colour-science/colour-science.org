.. title: Support for Color Exchange Format in Colour available!
.. slug: support-for-cxf-in-colour-available
.. date: 2025-09-24 10:50:00 UTC+01:00
.. tags: colour, colour science, release, cxf, colour cxf
.. category:
.. link:
.. description:
.. type: text

We are happy to announce the release of `Colour - CxF <https://github.com/colour-science/colour-cxf>`__.
This extension package for Colour implements reading and writing files in the Color Exchange Format (CxF).

.. TEASER_END

What is CxF?
------------

CxF is a XML-based file format that provides a flexible way to store and exchange color data across different systems.
It supports multiple color formats including RGB, CIELab, and spectral measurements, while providing standard ways to
include metadata and descriptions about the color information.

Features
--------
The Colour - CxF package allows

- Reading CxF documents from strings or files to a Python representation.
- Writing CxF documents from the Python representation to XML strings and files.
- Creating CxF objects programmatically for custom color data workflows.

Getting started
---------------

Install *Colour - CxF* via pip

.. code-block:: bash
    pip install colour-cxf

or via uv

.. code-block::
    bashuv add colour-cfx

Then use it to read CxF data

.. code-block:: python
    import colour_cxf

    # Reading from a string
    xml_string = """<?xml version="1.0" encoding="UTF-8"?>
    <cc:CxF xmlns:cc="http://colorexchangeformat.com/CxF3-core" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <cc:FileInformation>
            <cc:Creator>Colour Developers</cc:Creator>
            <cc:Description>Simple CxF Example</cc:Description>
        </cc:FileInformation>
    </cc:CxF>"""

    # Parse the XML string
    cxf = colour_cxf.read_cxf(xml_string.encode("utf-8"))

# Access file information
print(f"Creator: {cxf.file_information.creator}")
print(f"Description: {cxf.file_information.description}")

```


More Information
----------------
Visit the `Colour - CxF <https://github.com/colour-science/colour-cxf>`__ repository for more information,
usage examples and tutorials.

Funding
-------
We would like to thank `NumFOCUS <https://numfocus.org>`__
for funding the work on this package through the
`The Small Development Grants program  <https://numfocus.org/programs/small-development-grants>`__.
