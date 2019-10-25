.. title: The Importance of Terminology and sRGB Uncertainty
.. slug: the-importance-of-terminology-and-srgb-uncertainty
.. date: 2015-12-05 00:17:30 UTC
.. tags: chromaticity diagram, colour, colour science, EOTF, gamut, OETF, primaries, RGB colourspace, sRGB, transfer function, whitepoint
.. category: 
.. link: 
.. description: 
.. type: text

We were meant to write that entry since a while, and a
`great post <https://gamedevdaily.io/the-srgb-learning-curve-773b7f68cf7a#>`__ by
`Tom Forsyth <https://twitter.com/tom_forsyth>`__ from
`Oculus VR <https://www.oculus.com/en-us/>`__ triggered us in doing so.

.. TEASER_END

As I was quickly reading his article, I
`tweeted <https://twitter.com/colour_science/status/671647698546626560>`__
back about the missing description of *sRGB* as being an *RGB* colourspace: a
set of **primaries**, **whitepoint** and **transfer functions** components.

The article first description of *sRGB* is as follows:

    *sRGB is a slight tweaking of the simple gamma 2.2 curve.*

While this depiction of *sRGB* colourspace **Electro-Optical Transfer Function**
(**EOTF**) is exact, it may be confusing for non experts by omitting an explicit
emphasis of the components of an *RGB* colourspace.

For people experienced with colour theory and science, the post title and the
mention of **gamma** indicates that the article will likely only involves the
*sRGB* colourspace **EOTF** and its inverse.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | Charles Poynton's `Gamma FAQ <http://www.poynton.com/notes/colour_and_gamma/GammaFAQ.html>`__
        is an extensive reference on gamma correction.

Tom confirms that intuition a few paragraph later:

    *(the broader sRGB standard also has a bunch of gamut and colour-transform
    specifications, but we’ll ignore those and just focus on the gamma-curve
    part for now, since that is what concerns us for graphics rendering)*

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | The *gamut* defined by *sRGB* colourspace should actually be of a
        concern if one tries to achieve photo-realistic rendering as shown by
        `Steve Agland <http://nbviewer.jupyter.org/gist/sagland/3c791e79353673fd24fa>`__
        and `us <https://www.colour-science.org/posts/about-rendering-engines-colourspaces-agnosticism/>`__.

What is sRGB?
-------------

Terminology in a given scientific domain is key to its understanding, and this
is especially true in colour science. Everybody knows what colour is but yet
only a few can define it correctly, in this regard, we often cite
`Mark D. Fairchild <https://twitter.com/MDFairchild>`__:

    *Why should it be particularly difficult to agree upon consistent
    terminology in the field of color appearance? Perhaps the answer lies in
    the very nature of the subject. Almost everyone knows what color is.
    After all, they have had firsthand experience of it since shortly after
    birth. However, very few can precisely describe their color experiences or
    even precisely define color.* [1]_

*sRGB* is not a bunch of **transfer functions**, it is an actual
`RGB colourspace <https://en.wikipedia.org/wiki/RGB_color_space>`__, specified by
`IEC 61966-2-1:1999 Standard <https://webstore.iec.ch/publication/6169>`__
standard. As per `ISO 22028-1 Standard <http://www.iso.org/iso/catalogue_detail.htm?csnumber=37161>`__,
an *RGB* colourspace is defined by those mandatory 3 components:

- `Primaries`_
- `Whitepoint`_
- `Transfer Functions (OETF and EOTF)`_

The *ISO 22028-1 Standard* definition of an additive *RGB* colourspace is
quoted in its entirety for reference:

    **3.3**

    **additive RGB colour space**

    colorimetric colour space having three colour primaries (generally red,
    green and blue) such that CIE XYZ tristimulus values can be determined
    from the RGB colour space values by forming a weighted combination of the
    CIE XYZ tristimulus values for the individual colour primaries, where the
    weights are proportional to the radio-metrically linear colour space values
    for the corresponding colour primaries

    Note 1 to entry: A simple linear 3 × 3 matrix transformation can be used to
    transform between CIE XYZ tristimulus values and the radio-metrically linear
    colour space values for an additive RGB colour space.

    Note 2 to entry: Additive RGB colour spaces are defined by specifying the
    CIE chromaticity values for a set of additive RGB primaries and a colour
    space white point, together with a colour component transfer function.


Primaries
^^^^^^^^^

The **primaries** *chromaticity coordinates* define the **gamut** (the triangle
of colours) that can be encoded by a given *RGB colourspace*.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | When performing computations allowing for negative values and with
        enough precision, a given *RGB colorspace* can virtually encode any colours.
        Colours exceeding its gamut are simply represented with negative values.

It is important to understand that while commonly represented as triangles on a
*Chromaticity Diagram* (such as the *CIE 1931 Chromaticity Diagram*), *RGB colourspace*
**gamuts** define the boundaries of an actual 3D volume within the
`CIE xyY colourspace <https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space>`__:
The *Chromaticity Diagram* is a 2D projection of the *CIE xyY colourspace* volume
along its *Y* *Luminance* axis.

.. figure:: /images/ACES2065-1_ACEScg_DCI-P3_ITU-R_BT__709_ITU-R_BT__2020_CIE_1931_Chromaticity_Diagram.png

    Various *RGB colourspace* **gamuts** compared in the *CIE 1931 Chromaticity Diagram*.

.. figure:: /images/Colour_-_Analysis_CIE_xyY.gif

    The *CIE 1931 Chromaticity Diagram* in the bottom right view is a 2D
    projection of the *CIE xyY colourspace* in the left view.
    (`Colour - Analysis <https://github.com/colour-science/colour-analysis>`__)

Whitepoint
^^^^^^^^^^

The `whitepoint <https://en.wikipedia.org/wiki/White_point>`__  is defined by the
`CIE <http://eilv.cie.co.at/term/1430>`__ as:

    Achromatic reference stimulus in a chromaticity diagram that corresponds to
    the stimulus that produces an image area that has the perception of white.

Any set of colours lying on the *neutral axis* passing through the **whitepoint**,
no matter their *Luminance*, will be neutral to that *RGB colourspace*.

.. figure:: /images/CIE_xyY_sRGB.png

    *CIE Standard Illuminant D65* is located at the apex of *sRGB* colourspace
    volume.
    (`Colour - Analysis <https://github.com/colour-science/colour-analysis>`__)

An *RGB colourspace* can have
`different whitepoints <https://github.com/colour-science/colour-notebooks/blob/master/notebooks/colorimetry/illuminants.ipynb>`__
depending its context usage, *sRGB colourspace* *IEC 61966-2-1:1999 Standard*
adopts `CIE Standard Illuminant D65 <https://en.wikipedia.org/wiki/Illuminant_D65>`__
as **whitepoint** but an `ICC <https://en.wikipedia.org/wiki/International_Color_Consortium>`__
*sRGB colourspace* profile would likely have been chromatically adapted to
*CIE Standard Illuminant D50*.

.. figure:: /images/CIE_Illuminants_D_Series.png

    Various *CIE Illuminants D Series* *illuminants* in the
    *CIE 1960 UCS Chromaticity Diagram*.

Transfer Functions (OETF and EOTF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The transfer functions perform the mapping between the *linear* light
components (tristimulus values) and a *non-linear* R'G'B' video signal (most
of the time for coding optimisation and bandwidth performance). [2]_

-   The **Opto-Electronic Transfer Function** (**OETF**) maps estimated
    tristimulus values in a scene to a *non-linear* R'G'B' video component signal
    value. Typical **OETFs** are expressed by a power function with an exponent
    between 0.4 and 0.5. They can also be defined as piece-wise functions,
    *SMPTE 240M* or *BT.709* OETFs are such examples.

    .. figure:: /images/ITU-R_BT709_SMPTE_240M_OETFs.png

        Various **Opto-Electronic Transfer Functions**.

-   The **Electro-Optical Transfer Function** (**EOTF**) maps a *non-linear*
    R'G'B' video component signal to a tristimulus value at the display.
    Typical **EOTFs** are expressed by a power function with an exponent
    between 2.2 and 2.6 or a piece-wise function.

    .. figure:: /images/ITU-R_BT1886_sRGB_EOTFs.png

        Various **Electro-Optical Transfer Functions**.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | Jack Holm, technical secretary for IEC/TC 100/TA 2 which developed the
        *IEC 61966-2-1:1999 Standard* is unambiguous about the *sRGB* **EOTF**
        being piece-wise, i.e. not a *Gamma 2.2* approximation and that the
        *IEC 61966-2-1:1999 Standard* does not define an **OETF**.

        .. figure:: https://i.imgur.com/ROXaICc.png

            Message from Jack Holm, addressed the 1st February 2016 to the `Academy ACES Google Group <https://groups.google.com/forum/#!forum/academyaces>`__.

The Importance of Terminology
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the *RGB colourspace* specification components outlined, it should now make
more sense why not being specific and using a clear **terminology** can lead to
confusion and uncertainty: colour science vocabulary is complex.

I often encounter people that don’t have a clear understanding on what
composes an *RGB colourspace*, as a result they don't properly differentiate
**gamut** and **transfer functions**. The cursory **terminology** recurrently
used online is probably the root cause for that.

When one talks about *sRGB*, is he describing the colourspace **primaries** or
its **transfer functions**? Discussing about *sRGB* to *linear* transformation
without emphasis on the **EOTF** component is unsettling: a rendering
engine using linear *sRGB* colourspace input colours and textures, renders with
the *sRGB* colourspace **primaries** and **whitepoint** (assuming no colour
transformations are occurring internally), thus its output is within *sRGB*
colourspace.

When rendering using `BT.709 <https://en.wikipedia.org/wiki/Rec._709>`__
colourspace for HDTV, one is actually adopting *sRGB* colourspace **primaries**
and **whitepoint** with different specific **transfer functions**.

Movie cameras such as those from Canon (Canon EOS 1DC, Canon CX00) use *BT.709*
**primaries** and **whitepoint** but encode their scene linear values with a
custom log curve designated
`C-Log <http://www.usa.canon.com/cusa/professional/standard_display/cinema-firmware-c500>`__.

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | Most camera makers implement their own log curves (ALEXA Log C for ARRI Alexa
        cameras, RED Log Film for RED cameras, etc...) and proprietary
        *RGB colourspaces* specifications (ALEXA Wide Gamut RGB for ARRI Alexa
        cameras, REDcolor or DragonColor for RED cameras, etc...).

Likewise, it is perfectly valid to use the *sRGB* colourspace **transfer
functions** with another set of **primaries** and **whitepoint**. When
working within Adobe Photoshop or The Foundry Mari, some VFX studios use a
proprietary colourspace specification along *sRGB* colourspace **transfer
functions**: those **transfer functions** being commonly implemented in
various DCC packages, the various colour transformation operations between
those packages are simplified.

Conclusion
^^^^^^^^^^

When one talks about *sRGB* alone, it should be safe to assume that he is
referring to the *sRGB* colourspace as per *IEC 61966-2-1:1999 Standard*,
not just cherry picked components. Unfortunately it is not the case thus in order
to lessen the uncertainty and improve the **terminology** used, we suggest that:

-   One remembers that a given *RGB* colourspace is defined by the following
    essential three components:

    - `Primaries`_
    - `Whitepoint`_
    - `Transfer Functions (OETF and EOTF)`_
-   When writing on the *RGB* colourspace topic, one should ideally mention the
    previous point, it will help people getting the grasp on the theory.
-   When discussing about a given *RGB* colourspace component, one should make a
    point of describing which specification's component he is referring to:

        *sRGB is a slight tweaking of the simple gamma 2.2 curve.*

    would be better written as follows:

        *The sRGB transfer function is a slight tweaking of the simple gamma
        2.2 curve.*

    or for completeness:

        *The sRGB electro-optical transfer function (EOTF) is a slight tweaking
        of the simple gamma 2.2 curve.*

-   When describing an *RGB* colourspace not supported by an official specification
    or standard, one should probably use a name that explicitly defines the complete
    specification:

    -   `sRGB-D60-Linear`: an *RGB* colourspace using *sRGB* **primaries**
        chromatically adapted to *CIE Standard Illuminant D60* **whitepoint**
        and linear **transfer functions**.
    -   `Adobe 1998 RGB-D65-Gamma1.8`: an *RGB* colourspace using *Adobe 1998 RGB*
        **primaries**, *CIE Standard Illuminant D65* **whitepoint** and gamma
        1.8 **transfer functions**.

In the near future it will likely become even more critical and relevant as
new *RGB* colourspaces such as `BT.2020 <https://en.wikipedia.org/wiki/Rec._2020>`__
or the `ACES encodings <http://www.oscars.org/science-technology/sci-tech-projects/aces>`__
become mainstream.

Bibliography
^^^^^^^^^^^^

.. [1]  Fairchild, M. D. (2013). Color Appearance Models (3rd ed., pp. 1–10831).
        Wiley. ISBN:B00DAYO8E2
.. [2]  Poynton, C. (2012). Digital Video and HDTV - Algorithms and Interfaces
        - Second Edition (2nd ed.). Morgan Kaufmann. ISBN:9780123919267
