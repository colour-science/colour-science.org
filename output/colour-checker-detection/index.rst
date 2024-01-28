.. title: Colour - Checker Detection
.. slug: colour-checker-detection
.. date: 2019-03-24 10:45:00 UTC
.. tags: colour, colour science, colour - checker detection, colour rendition chart, python
.. category:
.. link:
.. description:
.. type: text

**Colour - Checker Detection** is a `Python <https://www.python.org>`__ package
implementing various colour checker detection algorithms and related utilities.

.. image:: https://raw.githubusercontent.com/colour-science/colour-checker-detection/master/docs/_static/ColourCheckerDetection_001.png

Features
^^^^^^^^

The following colour checker detection algorithms are implemented:

-   Segmentation
-   Machine learning inference via `Ultralytics YOLOv8 <https://github.com/ultralytics/ultralytics>`__

    -   The model is published on `HuggingFace <https://huggingface.co/colour-science/colour-checker-detection-models>`__,
        and was trained on a purposely constructed `dataset <https://huggingface.co/datasets/colour-science/colour-checker-detection-dataset>`__.
    -   The model has only been trained on *ColorChecker Classic 24* images and
        will not work with *ColorChecker Nano* or *ColorChecker SG* images.
    -   Inference is performed by a script licensed under the terms of the
        *GNU Affero General Public License v3.0* as it uses the
        *Ultralytics YOLOv8* API which is incompatible with the
        *BSD-3-Clause*.

API
^^^

The main technical reference for `Colour - Checker Detection <https://github.com/colour-science/colour-checker-detection>`__
is the `API Reference <https://colour-checker-detection.readthedocs.io/en/latest/reference.html>`__.

Examples
^^^^^^^^

-   `Colour - Checker Detection - Examples <https://github.com/colour-science/colour-checker-detection/tree/develop/colour_checker_detection/examples>`__

Downloads
^^^^^^^^^

-   `Colour - Checker Detection Github Repository <https://github.com/colour-science/colour-checker-detection>`__
-   `Colour - Checker Detection - Pypi <https://pypi.org/project/colour-checker-detection>`__
