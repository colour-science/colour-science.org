.. title: Our First 1000 Stars on Github!
.. slug: our-first-1000-stars-on-github
.. date: 2020-09-28 09:39:40 UTC+01:00
.. tags: colour, colour science, github
.. category: 
.. link: 
.. description: 
.. type: text

Earlier this week, `Colour <https://github.com/colour-science/colour>`__
received its 1000th star ⭐ and we are proud of the achievement!

We would not be here without the help of our users, `sponsors <https://github.com/colour-science/colour/blob/develop/SPONSORS.rst>`__, `contributors <https://github.com/colour-science/colour/blob/develop/CONTRIBUTORS.rst>`__ and
`NumFOCUS <https://numfocus.org/>`__, so thank you all!

.. TEASER_END

.. image:: /images/1000_Stars.png
    :target: https://star-history.t9t.io/#colour-science/colour

The development started six years ago, in April 2014 and today we reached an
important and exciting milestone.

.. code:: shell

    commit 90bc42b9fedfc7291c7023247eab14b41d5c29af
    Author: Thomas Mansencal <***@***.com>
    Date:   Sat Apr 5 14:07:48 2014 +0200

        Initial commit.

        Signed-off-by: Thomas Mansencal <***@***.com>

Colour science is often a topic that people avoid until they have no choice but
dive into it. As `I <https://github.com/KelSolaar>`__ was trying to address
the lack of quality HDR imagery for Image Based Lighting on the web, I quickly
fell into one of the deepest rabbit hole one could encounter. The truth is,
I'm still falling into it at light speed, and it is seemingly bottomless! :)

Michael joined shortly after, and from that point, the project started to take
off.

.. code:: text

    commit 8b7b974eead55c458fe71a94055eaf21b8bb5a19
    Author: Michael Mauderer <***@***.de>
    Date:   Sun Aug 10 17:54:31 2014 +0100

        Added new CAMs, tests for CAMs and fixed a bug in CIECAM02

Early, Michael and I created an invite only `Slack <https://colour-science.slack.com/>`__
workspace to coordinate the development. A year and half passed with mostly the
two of us working on **Colour**, at which point `Nick <https://github.com/nick-shaw/>`__
joined us along with `Kevin <https://github.com/KevinJW>`__:

.. code:: text

    commit fc0794acbeff210b749c3e8532f91472c0226eae
    Author: Nick-Shaw <***@***.com>
    Date:   Thu Apr 21 21:10:12 2016 +0100

        Implement RGB to Y'CbCr transforms.

.. code:: text

    commit 17345945618869b58275822fd23c46dae89af93b
    Author: Kevin Wheatley <***@***.com>
    Date:   Mon Jan 16 17:10:20 2017 +0000

        Update path usage to be correct when running vm from Windows

    Signed-off-by: Kevin Wheatley <***@***.com>

More people from the VFX industry joined the Slack workspace, turning it into
a friendly virtual bar to talk about light, colour, rendering, and everything
around those topics. Many discussions not only contributed to shape Colour and
its dependent packages but they also rippled into other Open Source projects.

Six years cruising full steam, and we have some highlights the team has
accomplished to cherry-pick from:

-   Five actively maintained Python packages:

    -   `Colour <https://github.com/colour-science/colour>`__, 3350 commits
    -   `Colour - Datasets <https://github.com/colour-science/colour-datasets>`__, 120 commits
    -   `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`__, 220 commits
    -   `Colour - HDRI <https://github.com/colour-science/colour-hdri>`__, 380 commits
    -   `Colour - Checker Detection <https://github.com/colour-science/colour-checker-detection>`__, 100 commits

-   Two actively maintained websites:

    -   `colour-science.org <https://www.colour-science.org/>`__
    -   `awesome-colour.org <http://awesome-colour.org/>`__
-   A decently maintained `Twitter account <https://twitter.com/colour_science>`__
-   Affiliated project of `NumFOCUS <https://numfocus.org/>`__
-   `First successful Google Summer of Code <https://i.imgur.com/PDwex2j.png>`__ 🎊
-   A `collective <https://opencollective.com/colour-science>`__ to openly
    track our expenses
-   Active participation to other Open Source projects:

    -   `Academy ACES <https://www.oscars.org/science-technology/sci-tech-projects/aces>`__

        -   `aces-dev <https://github.com/ampas/aces-dev>`__
        -   `ACES - Retrospective and Enhancements <https://github.com/colour-science/aces-retrospective-and-enhancements>`__
        -   `rawtoaces <https://github.com/ampas/rawtoaces>`__
        -   `Gamut Mapping Virtual Working Group <https://github.com/colour-science/aces-vwg-gamut-mapping-2020>`__

    -   Cinematic Color 2
    -   OpenColorIO

        -   `OpenColorIO-Configs <https://github.com/colour-science/OpenColorIO-Configs>`__
        -   `OpenColorIO-Config-ACES <https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES>`__

-   Dozens of `other colour science related repositories <https://github.com/colour-science>`__
-   Growing number of `contributors <https://www.colour-science.org/contributors/>`__
-   Cited by a `growing number of publications <https://www.colour-science.org/cited-by/>`__
-   A few `thousands of monthly downloads <https://pypistats.org/packages/colour-science>`__
-   Trended for a few days in 2018 on Github 🚀
-   Used by a growing number of companies, studios, universities, and
    people from those:

    -   **Google**

    .. code:: text

            Hey Thomas, Michael,

            Thanks for your work on Colour. It's fantastic, and has already helped us improve color correctness in our processing pipeline at YouTube (with more improvements coming soon, and hopefully fixes for open-source video pipelines too).

            If you're ever in SF, I'll buy you a round!

            Thanks,
            S***

    -   `Animal Logic <https://www.animallogic.com/>`__
    -   `Framestore <https://www.framestore.com/>`__
    -   `HdM Stuttgart <https://www.hdm-stuttgart.de/>`__

    .. raw:: html

        <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Thank you for sharing my PhD. After 15 years of MATLAB only I will be teaching my first course based on Python and using <a href="https://twitter.com/colour_science?ref_src=twsrc%5Etfw">@colour_science</a> this spring. Thank you for your great work.</p>&mdash; Jan Fröhlich (@Jan_Froehlich) <a href="https://twitter.com/Jan_Froehlich/status/1224940672391708672?ref_src=twsrc%5Etfw">February 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    -   `Illumination Mac Guff <https://www.illuminationmacguff.com/>`__
    -   `Merck Group <https://www.merckgroup.com/>`__
    -   `Method Studios <https://www.methodstudios.com/>`__
    -   `Sony Pictures Imageworks <https://www.imageworks.com/>`__
    -   `The Moving Picture Company <https://www.moving-picture.com/>`__
    -   `University of St Andrews <https://www.st-andrews.ac.uk/>`__
    -   `Weta Digital <https://www.wetafx.co.nz/>`__
    -   and much more...

What's next? First, merging the remaining `GSoC <https://summerofcode.withgoogle.com/>`__
code, especially the GPU backend if possible before releasing 0.3.16. Then, we
will work toward dropping Python 2 support and walk through the final steps for
the 1.0.0 release!

Feel free to join us on `Discourse <https://colour-science.discourse.group/>`__,
and contact us on `Gitter <https://gitter.im/colour-science/colour>`__ or by
`email <mailto:colour-developers@colour-science.org>`__.

Thomas, Michael, Nick, and the Colour Developers
