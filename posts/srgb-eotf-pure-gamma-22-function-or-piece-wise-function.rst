.. title: sRGB EOTF: Pure Gamma 2.2 Function or Piece-Wise Function?
.. slug: srgb-eotf-pure-gamma-22-or-piece-wise-function
.. date: 2019-10-25 20:54:39 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. has_math: true

A topic that caused a great deal of
`passionate <https://www.liftgammagain.com/forum/index.php?threads/dealing-with-srgb.13239/>`__
`discussions <https://twitter.com/troy_s/status/1170094480080265217>`__ is that
of the *sRGB* **Electro-Optical Transfer Function** (**EOTF**): Should it be
the *pure Gamma 2.2 function* or the *piece-wise function* defined in
*IEC 61966-2-1:1999 Standard*?

.. TEASER_END

To put is another way: Should a display calibrated to *sRGB* adopt the
*pure Gamma 2.2 function* or the *piece-wise function*?

.. class:: alert alert-dismissible alert-warning

    | *Warning*
    |
    | When using the term *Gamma* at
        `colour-science.org <https://colour-science.org/>`__,
        we are always referring to a pure power function whose exponent is
        known as *Gamma*.

.. class:: alert alert-dismissible alert-info

    | *Note*
    |
    | *IEC 61966-2-1:1999 Standard* takes a radical stance on the term *Gamma*
        in the *Ambiguity in the Definition of the Term "Gamma"* section:
    |
    | *Historically, both the photographic and television industries claim
        integral use of the term "gamma" for different effects. Hurter and
        Driffield first used the term in the 1890's in describing the
        straight-line portion of the density vs. log exposure curves that
        describe photographic sensitometry. The photographic sensitometry
        field has used several interrelated terms to describe similar effects,
        including; gamma, slope, gradient, and contrast. Both Languimier in the
        1910's and Oliver in the 1940's defined "gamma" for the television
        industry (and thus the computer graphics industry) as the exponential
        value in both simple and complex power functions that describe the
        relationship between gun voltage and intensity (or luminance). In fact,
        even within the television industry, there are multiple, conflicting
        definitions of "gamma." These include differences in describing
        physical aspects (such as gun "gamma" and phosphor "gamma"). These also
        include differences in equations for the same physical aspect
        (there are currently at least three commonly used equations in the
        computer graphics industry to describe the relationship between gun
        voltage and intensity, all of which provide significantly different
        results). After significant insightful feedback from many industries,
        this standard has chosen to explicitly avoid the use of the term
        "gamma." Furthermore, it appears that the usefulness as an unambiguous,
        constructive standard terminology is impossible and its continued use
        is detrimental to cross standard and unambiguous communication.*

.. figure:: /images/Gamma-2.2_sRGB_CCTFs.png

    A *Gamma 2.2 function* approximates the *piece-wise function* defined in
    *IEC 61966-2-1:1999 Standard*.

*IEC 61966-2-1:1999 Standard* lacks of the clarity that would gives the
definitive answer to the *EOTF* question. The quest takes on a muddy path when
the standard states the following in **2.1 Reference Display Conditions**:

    *Relative to this methodology, the reference display is characterised by the
    equation below where* :math:`V\prime{sRGB}` *is the input data signal and*
    :math:`V{sRGB}` *is the output normalized lumiance.*

    :math:`V{sRGB} = (V\prime{sRGB} + 0.0)^{2.2}`

While it is effectively common to find displays adopting the *Gamma 2.2*
function as an **EOTF**, many, such as
`EIZO </images/Lift-Gamma-Gain_EIZO-Colour-Navigator-7.png>`__ and
`NEC </images/Lift-Gamma-Gain_NEC-Spectral-View-2.png>`__ are shipping with the
*IEC 61966-2-1:1999 Standard* *piece-wise function*.

Fortunately, Jack Holm, technical secretary for IEC/TC 100/TA 2 which developed
the *IEC 61966-2-1:1999 Standard* is unambiguous about the *sRGB* **EOTF**
being the *piece-wise function*:

.. figure:: https://i.imgur.com/ROXaICc.png

    Message from Jack Holm, addressed the 1st February 2016 to the
    `Academy ACES Google Group <https://groups.google.com/forum/#!forum/academyaces>`__.

It should then be no surprise that the `ACES <https://www.oscars.org/science-technology/sci-tech-projects/aces>`__
`sRGB ODT <https://github.com/ampas/aces-dev/blob/76ea982a988d278dd12b563602771f46a5da3b83/transforms/ctl/odt/sRGB/ODT.Academy.sRGB_100nits_dim.ctl#L34>`__
also uses the *piece-wise function*. To finish, let us quote
`Charles Poynton <https://twitter.com/momaku/status/1170180565015900160>`_ for
good measure:

    *It took me 4 years to decide that the sRGB linear “toe” needs to be part
    of reference. CRTs were pure power function (GOGO if you like) all the way
    down to zero. No LCD shipped in the last 19 years has exhibited that
    behaviour externally. They all have a linear segment. QED.*

Conclusion
^^^^^^^^^^

If you are calibrating your display to the *sRGB* *IEC 61966-2-1:1999 Standard*,
your calibration target should be the *piece-wise function*. If you are
producing a display compliant with the *sRGB* *IEC 61966-2-1:1999 Standard* it
should adopt the *piece-wise function*.
