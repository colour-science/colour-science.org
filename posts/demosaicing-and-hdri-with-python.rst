.. title: Demosaicing and High Dynamic Range Imaging with Python
.. slug: demosaicing-and-hdri-with-python
.. date: 2015-12-18 06:15:31 UTC
.. tags: colour, colour science, colour - demosaicing, colour - hdri, release
.. category:
.. link:
.. description:
.. type: text

We have released two complementary image processing  `Python <https://www.python.org>`__
packages:

-   `Colour - Demosaicing </colour-demosaicing>`__ which implements various CFA
    (Colour Filter Array) demosaicing algorithms and related utilities.
-   `Colour - HDRI </colour-hdri>`__ which implements various HDRI
    processing algorithms.

.. TEASER_END

.. image:: https://raw.githubusercontent.com/colour-science/colour-hdri/master/docs/_static/Radiance_001.png

`Colour <https://github.com/colour-science/colour>`__ has its roots in a company
being created to deliver high quality images for the VFX industry with an
emphasis on colour processing correctness, dynamic range and resolution.

While most of the pipeline was providing good guidance over the authoring process,
the radiance image generation was entirely delegated to third-party applications.
Because of the lack of precise control over the processing and the missing
automation, it was an area we needed to revisit.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | The company is unfortunately stalled since a few years. On the bright
        side it gave birth to **Colour**.

The two new packages we have released today are the early outcome of my most
recent exploration of High Dynamic Range Imaging. It was an opportunity to assess
the viability of generating radiance images directly with the Python scientific
toolchain and compare various approaches.

A key aspect of that effort was to find out if there is a true benefit at
creating the radiance image prior to CFA (Colour Filter Array) demosaicing,
unfortunately, we don't have yet
`a definite answer <https://github.com/colour-science/colour-hdri/blob/develop/colour_hdri/examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb>`__.

Both packages provide examples notebooks:

-   `Colour - Demosaicing - Examples <https://github.com/colour-science/colour-demosaicing/tree/develop/colour_demosaicing/examples>`__
-   `Colour - HDRI - Examples <https://github.com/colour-science/colour-hdri/tree/develop/colour_hdri/examples>`__

Some of the notebooks rely on third-party libraries or applications to run such as

-   `Adobe DNG Converter <https://www.adobe.com/support/downloads/product.jsp?product=106&platform=Mac>`__
-   `dcraw <https://www.cybercom.net/~dcoffin/dcraw>`__
-   `ExifTool <http://www.sno.phy.queensu.ca/~phil/exiftool>`__
-   `rawpy <https://github.com/neothemachine/rawpy>`__

They are not mandatory and the data they provide can be acquired in various
different ways. We don't advocate an approach or another.

That work wouldn't have been possible without the excellent
`Advanced High Dynamic Range Imaging Book <http://www.advancedhdrbook.com>`__
and the tremendous amount of publications we gathered (over 30 publications
related to demosaicing and 20 publications for HDRI).

Finally, we recommend that you read `Posterior Sparisty-Directed Demosaicking <http://campus.udayton.edu/~ISSL/index.php/research/denoising-demosaicking>`__
and `Robust Patch-Based HDR Reconstruction of Dynamic Scenes <http://cvc.ucsb.edu/graphics/Papers/Sen2012_PatchHDR>`__
publications which are probably the state of the art although patented to various
degrees.

We take that opportunity to wish you a great 2016 year!
