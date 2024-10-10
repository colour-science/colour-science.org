.. title: NumFOCUS, Colour 0.3.14 and Colour - Datasets 0.1.0!
.. slug: numfocus-colour-0314-and-colour-datasets-010
.. date: 2019-10-27 08:39:18 UTC
.. tags:
.. category: colour, colour science, release, colour - datasets, numfocus
.. link:
.. description:
.. type: text

We are delighted to announce that **Colour** has joined the
`NumFOCUS <https://numfocus.org>`__  affiliated projects and that
`Colour 0.3.14 <https://github.com/colour-science/colour/releases/tag/v0.3.14>`__
has been released over the weekend along with
`Colour - Datasets 0.1.0 <https://github.com/colour-science/colour-datasets/releases/tag/v0.1.0>`__,
a new `Python <https://www.python.org>`__ package dedicated to colour science
datasets management.

.. TEASER_END

NumFOCUS
--------

**Colour** is now an affiliated project of `NumFOCUS <https://numfocus.org>`__,
a 501(c)(3) nonprofit in the United States. This will strengthen the project
and helps it grow and reach maturity.

.. image:: /images/Colour-NumFOCUS.png

Colour 0.3.14
-------------

**Colour 0.3.14** has been released over the weekend, please visit the
`releases page <https://github.com/colour-science/colour/releases/tag/v0.3.14>`__
for complete details or follow the highlights here.

We would like to thanks all the contributors whether they are contributing code
or participating to discussions on `Gitter <https://gitter.im/colour-science/colour>`__,
in the `issues <https://github.com/colour-science/colour/issues>`__, on Slack
or via email.

With this release we are getting close to have a beta candidate in the coming
months.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | The future beta candidate will likely be the last version to support
        Python 2.x.

Hacktoberfest - 2019
====================

We had a few new contributors for the 2019 edition of the
`Digital Ocean <https://hacktoberfest.digitalocean.com>`__
`Hacktoberfest <https://github.com/colour-science/colour/issues/507>`__.

Thanks to:

-   `@Chinmayrane16 <https://github.com/Chinmayrane16>`__
-   `@evalevanto <https://github.com/evalevanto>`__
-   `@feralpoosum <https://github.com/feralpoosum>`__
-   `@BPearlstine <https://github.com/BPearlstine>`__
-   `@pavithraes <https://github.com/pavithraes>`__

for their contributions! This was a good opportunity for us to revise and
update both the `Contributing <https://www.colour-science.org/contributing>`__
and `Installation <https://www.colour-science.org/installation-guide>`__
guides.

Automatic Colour Conversion Graph
=================================

*Colour* now implements an automatic colour conversion graph based on
`NetworkX <https://networkx.github.io>`__ and enabling easier colour
conversions:

.. code-block:: python

    sd = colour.COLOURCHECKERS_SDS["ColorChecker N Ohta"]["dark skin"]
    convert(sd, "Spectral Distribution", "sRGB", verbose={"mode": "Short"})

.. code:: text

    ===============================================================================
    *                                                                             *
    *   [ Conversion Path ]                                                       *
    *                                                                             *
    *   "sd_to_XYZ" --> "XYZ_to_sRGB"                                             *
    *                                                                             *
    ===============================================================================
    array([ 0.45675795,  0.30986982,  0.24861924])

.. image:: https://colour.readthedocs.io/en/develop/_static/Examples_Colour_Automatic_Conversion_Graph.png

Image Input and Output
======================

`Imageio <http://imageio.github.io>`__ is now a requirement for reading and
writing images, it will be used if `OpenImageIO <https://github.com/OpenImageIO/oiio>`__
is not available. If you wish to read *OpenEXR* files or develop *Colour*, you
will need to install the FreeImage plugin as follows:

.. code:: shell

    $ python -c "import imageio;imageio.plugins.freeimage.download()"

Support for `OpenImageIO 2.x <https://github.com/OpenImageIO/oiio/releases/tag/Release-2.0.3>`__
has also been implemented.

Name and Signature Changes
==========================

Various colour component transfer functions objects have been either renamed or
their signature changed, most notably the *sRGB* transfer functions and the
`colour.oetf <https://colour.readthedocs.io/en/develop/generated/colour.oetf.html#colour.oetf>`__
definition.

All the *reverse* words have been replaced with *inverse* in object names, file
names and, docstrings.

Coverage
========

Coverage was `raised to 100% <https://coveralls.io/github/colour-science/colour>`__.
It does not mean that all the possible code paths are covered but it certainly
strengthen the API.

Dependency Management
=====================

We have adopted `Poetry <https://poetry.eustace.io>`__ to manage the
development dependencies, the ``setup.py`` file has been replaced with a
`standardized <https://www.python.org/dev/peps/pep-0518>`__ ``pyproject.toml``
file.

Continuous Integration
======================

`Travis-ci <https://travis-ci.com>`__ and
`Azure Pipelines <https://azure.microsoft.com/en-us/services/devops/pipelines>`__
have been replaced with `Github Actions <https://github.com/colour-science/colour/actions>`__.

Documentation
=============

The `README <https://github.com/colour-science/colour/blob/develop/README.rst>`__
and the `Manual <https://colour.readthedocs.io/en/develop>`__ have been
slightly reorganised to create a better separation between the tutorials, API
reference and, the new
`How-To Guide <https://colab.research.google.com/drive/1NRcdXSCshivkwoU2nieCvC3y14fx1X4X#offline=true&sandboxMode=true>`__.

Colour - Datasets
-----------------

`Colour - Datasets 0.1.0 <https://github.com/colour-science/colour-datasets/releases/tag/v0.1.0>`__
is a new `Python <https://www.python.org>`__ package dedicated to colour
science datasets management.

The existing datasets are hosted in
`Zenodo <https://zenodo.org>`__ under the
`Colour Science - Datasets <https://zenodo.org/communities/colour-science-datasets>`__
community:

.. code-block:: python

    import colour_datasets

    print(colour_datasets.datasets())

.. code-block:: text

    colour-science-datasets
    =======================

    Datasets : 16
    Synced   : 1
    URL      : https://zenodo.org/communities/colour-science-datasets/

    Datasets
    --------

    [ ] 3269926 : Agfa IT8.7/2 Set
    [ ] 3245883 : Camera Spectral Sensitivity Database
    [ ] 3367463 : Constant Hue Loci Data
    [ ] 3362536 : Constant Perceived-Hue Data
    [ ] 3270903 : Corresponding-Colour Datasets
    [ ] 3269920 : Forest Colors
    [x] 3245875 : Labsphere SRS-99-020
    [ ] 3269924 : Lumber Spectra
    [ ] 3269918 : Munsell Colors Glossy (All) (Spectrofotometer Measured)
    [ ] 3269916 : Munsell Colors Glossy (Spectrofotometer Measured)
    [ ] 3269914 : Munsell Colors Matt (AOTF Measured)
    [ ] 3269912 : Munsell Colors Matt (Spectrofotometer Measured)
    [ ] 3245895 : New Color Specifications for ColorChecker SG and Classic Charts
    [ ] 3252742 : Observer Function Database
    [ ] 3269922 : Paper Spectra
    [ ] 3372171 : RAW to ACES Utility Data

**Colour - Datasets** was created to overcome issues encountered frequently
when trying to access or use colour science datasets:

-   No straightforward ingestion path for dataset content.
-   No simple loading mechanism for dataset content.
-   Unavailability of the dataset, e.g., download url is down, dataset content is passed directly from hand to hand.
-   No information regarding the definitive origination of the dataset.

**Colour - Datasets** offers all the above: it allows users to ingest and load
colour science datasets with a single function call. The datasets information
is hosted on `Zenodo <https://zenodo.org>`__ where the record for a dataset typically contain:

-   An urls.txt file describing the urls to source the dataset files from.
-   A copy of those files in the eventuality where the source files are not
    available or the content has changed without notice. This actually happened
    to the *Camera Spectral Sensitivity Database* dataset during the project
    incubation.
-   Information about the authors, content and licensing.

Other Projects
--------------

`Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing/releases/tag/v0.1.5>`__
and `Colour - HDRI <https://github.com/colour-science/colour-hdri/releases/tag/v0.1.6>`__
have been updated according to `Colour 0.3.14 <https://github.com/colour-science/colour/releases/tag/v0.3.14>`__
changes.

`Colour - Checker Detection <https://github.com/colour-science/colour-checker-detection>`__
will follow in the coming days.
