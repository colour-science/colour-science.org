.. title: Colour 0.3.5 is available!
.. slug: colour-035-is-available
.. date: 2015-05-07 01:01:00 AM GMT+12
.. tags:
.. category:
.. link:
.. description:
.. type: text

After months of work, we are pleased to announce that
`Colour 0.3.5 <https://github.com/colour-science/colour/releases/tag/v0.3.5>`_
is finally available. This release is a major milestone toward a stable API.

The focus has been vectorisation of most of the API code. The average
speed increase is a **x235** factor for over a hundred core definitions
(details are available in this `Google Docs Spreadsheet <https://docs.google.com/spreadsheets/d/10O344GaDbZaS9dNLIhP-uSPIgJXEMgz0MKEPPECtTy0/edit?usp=sharing>`_).

The direct benefit is that the API is now well suited to work on images with
acceptable computation times. Favoring flexibility over high level
optimisations and speed, we have also maintained almost complete backward
compatibility.

Another key feature is our recent derivation of
`RED colourspaces <http://colour-science.org/blog_red_colourspaces_derivation.php>`_.

Feel free to take a look at the `releases page <https://github.com/colour-science/colour/releases/tag/v0.3.5>`_
for complete details.
