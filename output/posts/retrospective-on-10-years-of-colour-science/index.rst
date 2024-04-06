.. title: Retrospective on 10 Years of colour-science
.. slug: retrospective-on-10-years-of-colour-science
.. date: 2024-04-05 22:52:29 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Today is the 10th anniversary of `Colour <https://github.com/colour-science/colour>`__ and `colour-science <https://github.com/colour-science>`__!

.. code:: text

    (colour-science-py3.12) Eris:colour kelsolaar$ git log --reverse
    commit 90bc42b9fedfc7291c7023247eab14b41d5c29af
    Author: Thomas Mansencal <thomas.mansencal@gmail.com>
    Date:   Sat Apr 5 14:07:48 2014 +0200

        Initial commit.

        Signed-off-by: Thomas Mansencal <thomas.mansencal@gmail.com>

It is time for a decade of work retrospective.

.. TEASER_END

We would like to start by thanking all the contributors whether they write code, improve the documentation, create issues or start discussions.

Over the past 10 years, we built a strong community of people loving colour science. There have been many passionate discussions about this complex scientific domain.
To this day, we still do not have full understanding of how human vision works, so we are excited about the future.

`Colour <https://github.com/colour-science/colour>`__ has become one of the most comprehensive open source colour science library, irrespective of the programming language.

`colour-science <https://github.com/colour-science>`__ now has almost 50 repositories, the main ones are as follows:

.. raw:: html

    <table class="table">
    <thead>
      <tr>
        <th scope="col">Repository</th>
        <th scope="col">LoC (Python)</th>
        <th scope="col">Commits</th>
        <th scope="col">Stars</th>
        <th scope="col">Forks</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour">colour</a></td>
        <td scope="row">207000</td>
        <td scope="row">4970</td>
        <td scope="row">1936</td>
        <td scope="row">85</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-checker-detection">colour-checker-detection</a></td>
        <td scope="row">3900</td>
        <td scope="row">362</td>
        <td scope="row">202</td>
        <td scope="row">28</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-datasets">colour-datasets</a></td>
        <td scope="row">12000</td>
        <td scope="row">358</td>
        <td scope="row">52</td>
        <td scope="row">11</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-demosaicing">colour-demosaicing</a></td>
        <td scope="row">1500</td>
        <td scope="row">457<br></td>
        <td scope="row">260</td>
        <td scope="row">57</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-hdri">colour-hdri</a></td>
        <td scope="row">8500</td>
        <td scope="row">661</td>
        <td scope="row">126</td>
        <td scope="row">18</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-specio">colour-specio</a></td>
        <td scope="row">1450</td>
        <td scope="row">74</td>
        <td scope="row">3</td>
        <td scope="row">1</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-visuals">colour-visuals</a></td>
        <td scope="row">4600</td>
        <td scope="row">40</td>
        <td scope="row">29</td>
        <td scope="row">1</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/colour-science.org">colour-science.org</a></td>
        <td scope="row">N/A</td>
        <td scope="row">523</td>
        <td scope="row">10</td>
        <td scope="row">3</td>
      </tr>
      <tr>
        <td scope="row"><a href="https://github.com/colour-science/awesome-colour">awesome-colour</a></td>
        <td scope="row">N/A</td>
        <td scope="row">114</td>
        <td scope="row">251</td>
        <td scope="row">19</td>
      </tr>
    </tbody>
    </table>

To update what we `wrote 4 years ago <../our-first-1000-stars-on-github/index.html>`__, here are the highlights at this date:

-   Seven actively maintained Python packages:

    -   `Colour <https://github.com/colour-science/colour>`__
    -   `Colour - Checker Detection <https://github.com/colour-science/colour-checker-detection>`__
    -   `Colour - Datasets <https://github.com/colour-science/colour-datasets>`__
    -   `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`__
    -   `Colour - HDRI <https://github.com/colour-science/colour-hdri>`__
    -   `Colour - Specio <https://github.com/colour-science/colour-specio>`__
    -   `Colour - Visuals <https://github.com/colour-science/colour-visuals>`__

-   Two actively maintained websites:

    -   `colour-science.org <https://www.colour-science.org>`__
    -   `awesome-colour.org <http://awesome-colour.org>`__
-   An active `Twitter account <https://twitter.com/colour_science>`__
-   Affiliated project of `NumFOCUS <https://numfocus.org>`__
-   `First successful Google Summer of Code <https://i.imgur.com/PDwex2j.png>`__
-   A `collective <https://opencollective.com/colour-science>`__ to track our expenses
-   Active participation to other Open Source projects:

    -   `Academy ACES <https://www.oscars.org/science-technology/sci-tech-projects/aces>`__

        -   `aces-dev <https://github.com/ampas/aces-dev>`__
        -   `ACES - Retrospective and Enhancements <https://github.com/colour-science/aces-retrospective-and-enhancements>`__
        -   `rawtoaces <https://github.com/AcademySoftwareFoundation/rawtoaces>`__
        -   `Gamut Mapping Virtual Working Group <https://github.com/colour-science/aces-vwg-gamut-mapping-2020>`__
        -   `Output Transforms Virtual Working Group <https://community.acescentral.com/c/aces-development-acesnext/vwg-output-transforms/68>`__
        -   `Input Transforms Working Group <https://community.acescentral.com/c/aces-development-acesnext/vwg-input-transforms/82>`__
        -   `IDT Calculator <https://github.com/ampas/idt-calculator>`__

    -   OpenColorIO

        -   `OpenColorIO <https://github.com/AcademySoftwareFoundation/OpenColorIO>`__
        -   `OpenColorIO-Configs <https://github.com/colour-science/OpenColorIO-Configs>`__
        -   `OpenColorIO-Config-ACES <https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES>`__

-   Dozens of `other colour science related repositories <https://github.com/colour-science>`__
-   Growing number of `contributors <https://www.colour-science.org/contributors>`__
-   Cited by a `growing number of publications <https://www.colour-science.org/cited-by>`__
-   `Dozen of thousands of monthly downloads <https://pypistats.org/packages/colour-science>`__
-   Trended for a few days in 2018 on Github
-   Two `GSoC participation <https://github.com/colour-science/GSoC>`__
-   Used by an ever growing number of companies, studios and universities:

    -   **Google**

    .. code:: text

            Hey Thomas, Michael,

            Thanks for your work on Colour. It's fantastic, and has already helped us improve color correctness in our processing pipeline at YouTube (with more improvements coming soon, and hopefully fixes for open-source video pipelines too).

            If you're ever in SF, I'll buy you a round!

            Thanks,
            S***

    -   `Animal Logic <https://www.animallogic.com>`__
    -   `Epic Games <https://github.com/EpicGames/UnrealEngine/blob/072300df18a94f18077ca20a14224b5d99fee872/Engine/Source/Runtime/ColorManagement/Private/Tests/ColorManagementTests.cpp#L83>`__
    -   `Framestore <https://www.framestore.com>`__
    -   `HdM Stuttgart <https://www.hdm-stuttgart.de>`__

    .. raw:: html

        <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Thank you for sharing my PhD. After 15 years of MATLAB only I will be teaching my first course based on Python and using <a href="https://twitter.com/colour_science?ref_src=twsrc%5Etfw">@colour_science</a> this spring. Thank you for your great work.</p>&mdash; Jan Fröhlich (@Jan_Froehlich) <a href="https://twitter.com/Jan_Froehlich/status/1224940672391708672?ref_src=twsrc%5Etfw">February 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

    -   `Illumination Mac Guff <https://www.illuminationmacguff.com>`__
    -   `ILM <https://www.ilm.com>`__
    -   `Merck Group <https://www.merckgroup.com>`__
    -   `Netflix <https://www.netflix.com/browse>`__
    -   `Method Studios <https://www.methodstudios.com>`__
    -   `Sony Pictures Imageworks <https://www.imageworks.com>`__
    -   `The Moving Picture Company <https://www.moving-picture.com>`__
    -   `University of St Andrews <https://www.st-andrews.ac.uk>`__
    -   `Wētā FX <https://www.wetafx.co.nz>`__
    -   and much more...

What is the future of **Colour**? We thought we could merge the GPU backend four years ago and ultimately decided against. The main issue is that it was very much vendor locked because of `Cupy <https://cupy.dev>`__.
In a hindsight, this was a good decision as there has been some exciting new development with the `Python Array API Standard <https://data-apis.org/array-api/latest/index.html>`__. We haven't started work yet to support it, but we have certainly `discussed about it <https://github.com/colour-science/colour/issues/1244>`__.

We also thought that 1.0.0 would be released, but this did not happened! We instead continued to improve the API and a stable release will only be possible after adoption of the Python Array API standard.

With all the written, we are hoping to continue for at least another decade. Feel free to join us on `Github Discussions <https://github.com/colour-science/colour/discussions>`__, contact us on `Gitter <https://gitter.im/colour-science/colour>`__ or by `email <mailto:colour-developers@colour-science.org>`__.

**The Colour Developers**
