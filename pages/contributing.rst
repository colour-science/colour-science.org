.. title: Contributing
.. slug: contributing
.. date: 2015-11-25 05:35:44 UTC
.. tags: contributing
.. category:
.. link:
.. description:
.. type: text

**Colour** is open source and we happily welcome contributions. This guide will
give you an overview on how to contribute.

There are many ways to help:

-   Reporting a defect, proposing a new feature or enhancement or
    commenting existing issues on the `Issue
    Tracker <https://github.com/colour-science/colour/issues>`_
-   Contributing new code by implementing new features or adding
    examples, for some ideas you can take a look at the issues with the
    `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`_,
    `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`_
    and
    `Ready <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AReady>`_
    labels or the
    `v9.9.9 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+milestone%3Av9.9.9>`_
    milestone.
-   Maintaining the existing code base, improving the code style and quality,
    improving the coverage, updating the documentation, fixing bugs, addressing
    TODOs, etc... Issues with the
    `Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`_
    or
    `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`_
    labels are a good place to start.
-   Improving the
    `Jupyter Notebooks <http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/blob/master/notebooks/colour.ipynb>`_,
    we aim to provide a good scientific support to the API and there is still a
    lot to do.
-   Improving siblings packages:

    -   `Colour - Demosaicing </colour-demosaicing/>`_
    -   `Colour - HDRI </colour-hdri/>`_
    -   `Colour - Maya </colour-maya/>`_
    -   `Colour - Nuke </colour-nuke/>`_
    -   `Colour - Spectroscope </colour-spectroscope/>`_

-   Participating in discussions on the `Mailing List <colour-science@googlegroups.com>`_.

Reporting Issues
----------------

The three major issue types one can report on the issue tracker are the
following:
`Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`_,
`Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`_
and
`Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`_.

We currently use a large set of labels to categorise issues:

-   `Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`_:
    Used for any kind of defect reported.

    -    `Critical <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ACritical>`_:
         Used for issues either rendering the software unusable, causing loss of
         data, or preventing people to work. These issues need to be fixed
         immediately.
    -    `Major <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AMajor>`_:
         Used for issues which have significant consequences on the ability of
         people to work but do not lead to the whole API being unusable.
    -    `Normal <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ANormal>`_:
         Used for issues affecting one piece of functionality. Those are usually
         self-contained and don't impact the overall functionality of the API.
    -    `Minor <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AMinor>`_:
         Used for cosmetic issues that don't prevent the API to run properly.

-   `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`_:
    Used for an enhancement of an existing feature, can also be used for new
    feature suggestion, although
    `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`_
    label should be preferred.
-   `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`_:
    Used for a new feature, functionality suggestion.

    -    `P1 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP1>`_:
         Used for the highest priority.
    -    `P2 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP2>`_:
         Used for average priority.
    -    `P3 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP3>`_:
         Used for the lowest priority.

-   `API <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AAPI>`_:
    Used for issues related to the API.
-   `Discarded <https://github.com/colour-science/colour/issues?q=is%3Aclose+is%3Aissue+label%3ADiscarded>`_:
    Used for a discarded / canceled issue.
-   `Discussion <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADiscussion>`_:
    Used to discuss any subject, those issues often turn into features or
    enhancement.
-   `Distribution <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADistribution>`_:
    Used to discuss distribution and packaging of the API.
-   `Documentation <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADocumentation>`_:
    Used for issues related to the documentation.
-   `Duplicate <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADuplicate>`_:
    Used for a duplicate issue.
-   `Examples <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AExamples>`_:
    Used for issues related to the examples.
-   `In Progress <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AIn%20Progress>`_:
    Used for an issue started and ongoing with very long development time.
-   `Postponed <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3APostponed>`_:
    Used for an issue postponed for a future milestone.
-   `Ready <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AReady>`_:
    Used for an issue ready to be addressed.
-   `Task <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ATask>`_:
    Used for a task not directly related to pure programming.
-   `Good First Issue <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Good+First+Issue">`_:
    Used for an issue appropriate for a first time contribution.
-   `Help Wanted <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Help+Wanted">`_:
    Used for an issue appropriate for a first time contribution but likely harder than a
    `Good First Issue <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Good+First+Issue">`_ one.

Defects
^^^^^^^

You encountered a problem while using **Colour**, please consider reporting it
on the `Issue Tracker <https://github.com/colour-science/colour/issues>`_.

The first thing to do, is to check if there are any existing issues describing
your problem, if there is one, you are welcome commenting into it and provide
more details. However, please avoid creating duplicates, they add noise to the
issue tracker and we will have to label them as
`Duplicate <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADuplicate>`_
and close them.

When reporting a defect please provide the following details if possible and
makes sense to do so:

-   **Colour** version.
-   `Python <https://www.python.org/>`_ version.
-   `NumPy <http://www.numpy.org/>`_ and `SciPy <http://www.scipy.org/>`_
    versions.

If you are reporting an exception, please provide the complete traceback, it
will tremendously help us understand what happened.

Features & Enhancements
^^^^^^^^^^^^^^^^^^^^^^^

If you would like a new feature to be supported or an enhancement of an
existing feature, don't hesitate to link any resources or references you feel
like would help its implementation: publications, wikipedia article, etc...

If there is an implementation existing in another language, we will be most
likely be able to port it although the licence must be compatible with the
`New BSD License <http://opensource.org/licenses/BSD-3-Clause>`_ terms.

We are also running `Matlab <http://www.mathworks.fr/products/matlab/>`_, so
don't hesitate to provide snippets for it if you have functions you would like
to be ported.

Contributing Code
-----------------

Assuming you have something to work on, you will have to get the code and
follow the guidelines.

Development for Colour
^^^^^^^^^^^^^^^^^^^^^^

Here is a succinct overview of the steps you will most likely go through:

1.  `Fork <https://github.com/colour-science/colour/fork>`_ the
    `Colour <https://github.com/colour-science/colour>`_ repository.
2.  Activate `Travis-CI <http://travis-ci.org/>`_ for your *fork* so that the
    tests suite is run when you push your changes.
3.  Clone the repository locally to your workspace:

.. code:: shell

    git clone git@github.com:$USER/colour.git

4.  Connect your clone to the original *upstream* repository by adding it as a
    remote:

.. code:: shell

    git remote add upstream git@github.com:colour-science/colour

5.  You should now have two remotes:

.. code:: shell

    git remote -v
    origin  https://github.com/$USER/colour (fetch)
    origin  https://github.com/$USER/colour (push)
    upstream  https://github.com/colour-science/colour (fetch)
    upstream  https://github.com/colour-science/colour (push)

6.  Pull the latest changes from *upstream*:

.. code:: shell

    git checkout master
    git pull upstream master

7.  Create a branch for your contribution:

.. code:: shell

    git checkout -b feature/mie_scattering

    The core developers are using the
    `git flow branching model <http://nvie.com/posts/a-successful-git-branching-model/>`_
    for most of the development tasks and since the branch name appears in the
    commit message and for consistency, please use the following branch
    prefixes:

    -   Feature branch prefix: **feature/**
    -   Release branch prefix: **release/**
    -   Hotfix branch prefix: **hotfix/**

8.  Check if the unit tests and doctests are running properly.
9.  `flake8 <https://pypi.python.org/pypi/flake8>`_ is currently set to error if
    anything incorrect is found, thus we advice that you run it before
    committing and pushing your code to *origin*, your own fork.
10. Commit your changes:

.. code:: shell

    git add mie_scattering.py
    git commit -m 'Implement "Mie Scattering" support.'

11. Push your changes back to *origin*, your own fork:

.. code:: shell

    git push origin feature/mie_scattering

12. Ensure that the test suite is all right on `Travis-CI <http://travis-ci.org/>`_.
13. Visit your repository fork on `Github <http://github.com/>`_. Your branch
    should have a green *Pull Request* button, this will open a *pull request*
    and let us know that we have some code to review :)

Code Reviews
------------

Your *pull request* will be reviewed by the maintainers and any other developer
interested in the project.

Every single developer has his code reviewed, this is a natural process helping
to raise the codebase quality while having a friendly discussion. Comments will
be made on various aspects such as the documentation and references, the code
style and its implementation. Those can be discouraging, although they are not
meant to criticize but aim at improving the quality of your submission. We all
learn from that process and the project ultimately benefits from them.

Guidelines
----------

Most of the conventions used in **Colour** are the same than
`NumPy <http://www.numpy.org/>`_, `SciPy <http://www.scipy.org/>`_ and
`scikit-image <http://scikit-image.org/>`_.

Overview
^^^^^^^^

We follow the `Google Python Style Guide <https://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_
and especially the *Python Language Rules* although with the main exception
being the docstrings / documentation formatted with `Numpy Docstrings Style <https://github.com/numpy/numpy/blob/master/doc/example.py>`_.

The code has to be `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`_
compliant although but before anything else, it needs to be consistent with the
Colour Science litterature:

For example, the base **CIE** colourspace is **CIE XYZ** with upper case
notation. It can be converted to chromaticity coordinates **xy** with lower
case notation. If we were to follow the `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`_
recommendations, we would have written a conversion definition as follows:

.. code:: python

    def xyz_to_xy(xyz):
        x, y, z = np.ravel(xyz)
        x, y = x / (x + y + z), y / (x + y + z)
        return x, y

Abstracting the fact the above definition is totally undocumented, it can be
confusing to understand when we are referencing big **X** tristimulus value or
little **x** chromaticity coordinate.

For those cases, and there are legions of them in Colour Science, we have
decided to go for clarity and consistency with the literature for the object
names:

.. code:: python

    def XYZ_to_xy(XYZ):
        X, Y, Z = np.ravel(XYZ)
        x, y = X / (X + Y + Z), Y / (X + Y + Z)
        return x, y

When the reference is using upper case named variables, we try to follow
the same convention, it is unfortunately not `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`_
compliant but has the benefit of a much easier comparison between the
implementation and the reference.

We suggest that contributors follow the same rule.

Python Language Rules
^^^^^^^^^^^^^^^^^^^^^

-   All the code must be covered by unit tests and doctests.
-   All the code must be documented to the same standard than
    `NumPy <http://www.numpy.org/>`_, `SciPy <http://www.scipy.org/>`_
    and `scikit-image <http://scikit-image.org/>`_.
-   All the code must be checked with the static analysis tool of your choice
    (we use `PyCharm <http://www.jetbrains.com/pycharm/>`_ extensively),
    `flake8 <https://pypi.python.org/pypi/flake8>`_,  `Landscape <https://landscape.io/>`_
    and `Scrutinizer <https://scrutinizer-ci.com/>`_
-   No *pull request* should be merged without being reviewed and ensuring that
    the tests suite pass in `Travis-CI <http://travis-ci.org/>`_.
-   Examples should be provided for new features.

Python Style Rules
^^^^^^^^^^^^^^^^^^

-   Ensure consistency with Colour Science literature first.
-   Ensure `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`_ compliance.
-   Try using a close to *Latex* syntax for variables names so that they are
    easier to compare to the reference.

    For instance, a variable defined \\(D\_{uv}\\) in a paper would be defined
    as *D\_uv* in the code, \\(L^\*\\) as *Lstar* and \\(X\_{ab}^{\\prime}\\) as
    *Xp\_ab*.
-   Try using uppercase for author names in definitions:

.. code:: python

    def CCT_to_xy_Kang2002(CCT):

-   Please use *British English* words instead of *American English* ones as
    the **CIE** does, the most important of all being **colour** instead of
    **color**. You can consult the `CIE Termlist <http://eilv.cie.co.at/>`_ if
    any doubts.
-   Import `NumPy <http://www.numpy.org/>`_ as follows:

.. code:: python

    import numpy as np

-   Doctests may need **ellipsis**, don't rely on global **nose** settings and
    specify it using the dedicated pragma as follows:

.. code:: python

    >>> Lab = np.array([100.00000000, -7.41787844, -15.85742105])
    >>> Lab_to_LCHab(Lab)  # doctest: +ELLIPSIS
    array([ 100.        ,   17.5066479...,  244.9304684...])

-   Numbers in the API are usually rounded as follows:

    -   Dataset numbers are kept as is if they are from a known reference or
        rounded to 15 digits if computed with the API (spectral power
        distributions, chromaticity coordinates, etc...).
    -   Unit tests and doctests input numbers are kept as is if they are from
        a reference or rounded to 8 digits if computed with the API.
    -   Unit tests output numbers are rounded to 8 digits.
    -   Doctests output numbers trimmed with **ellipsis** to 7 digits.
-   Some commonly used dataset elements have aliases like **'cie\_2\_1931'**
    for **'CIE 1931 2 Degree Standard Observer'**. Those are provided for
    convenience and are reserved for external usage, please use the long form
    for consistency across the API.
-   In the same way as above, some computation methods are using a title case
    like **'Ohno 2013'**, while the mapping object holding them is case
    insensitive, please use the title case form for consistency across the API.
-   Some very big lines sometimes cannot be wrapped (doctests, html links), you
    can use the **# noqa** pragma in those cases, although do it in last resort,
    we have already too much of them.
-   Avoid **/** to wrap lines, prefer using the parenthesis **()**.
-   The code formatting is performed using `Yapf <https://github.com/google/yapf>`_. You can invoke it recursively on a directory as follows:

.. code:: shell

          find . -type f -name '*.py' -exec yapf -i {} \;

-   Inline comments must have two spaces.
-   Ensure that you have blank line at the end of the files.
-   Ensure that trailing whitespaces are stripped.
-   Prefix unused variable with an underscore:

.. code:: python

    _L, a, b = tsplit(Lab)

Citations
^^^^^^^^^

It's likely that the code you contribute will be based upon references, we are
using the `APA 6th Edition <http://www.apastyle.org/>`_ citation style:

::

    Davis, W., & Ohno, Y. (2010). Color quality scale. Optical Engineering, 49(3), 33602–33616. doi:10.1117/1.3360335

::

    Wyszecki, G., & Stiles, W. S. (2000). Table I(6.5.3) Whiteness Formulae (Whiteness Measure Denoted by W). In Color Science: Concepts and Methods, Quantitative Data and Formulae (pp. 837–839). Wiley. ISBN:978-0471399186

::

    Lindbloom, B. (2014). RGB Working Space Information. Retrieved April 11, 2014, from http://www.brucelindbloom.com/WorkingSpaceInfo.html

We are storing all our citations in a database maintained by
`Mendeley <http://www.mendeley.com/>`_.

Commits
^^^^^^^

A good committing strategy implies that separated commits should be done for
any particular changes: One should not commit multiple bugs fixes or large
change sets at once.

This unnecessarily increase complexity for any code merge or rollbacks needs
and prevent a grainier control over the version control. One exception to this
rule is for the initial design steps when creating a new sub-package or
feature (please consider squashing the commits), but once the said sub-package
is in production, a regular committing strategy should be applied.

Commit messages need to use imperative syntax, the first commit line must be a
quick description of the modification content finished by a punctuation mark
and can be followed by a detailed description separated by one line break. If
the commit fixes a particular issue in the issue tracker, it's advised to state
it in the commit message using the following syntax: **Closes #32.**

::

    Yes:
    Implement "Yoshi Ohno" correlated colour temperature calculation.

    Closes #32.
    This implementation allows for a more precise correlated colour temperature
    calculation by using a two solutions hybrid approach.

::

    No:
    Coded new cool cct method

Feature Branches & History
^^^^^^^^^^^^^^^^^^^^^^^^^^

History should never be re-written, although while working on your local
**feature** branch, you may want to provide a cleaner commits history before
submitting a *pull request*. It is perfectly fine to modify your local branch
as you wish.

However, if you need to change history on a public and used **feature**
branch, please inform the `Colour developers <mailto:colour-science@googlegroups.com>`_
in order to avoid commit losses or a merging disaster.

Releasing Colour
----------------

The following stages help maintainers navigate through the release of a new
version of **Colour**, some automation is provided by `Invoke <http://www.pyinvoke.org/>`_:

.. raw:: html

    <ul>
        <li>
            <dl>
                <dt>Github</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Review the
                                    <a class="reference external" href="https://github.com/colour-science/colour/releases">releases</a>
                                    page</label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Check open issues on current
                                    <a class="reference external" href="https://github.com/colour-science/colour/milestones">milestone</a>
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Colour - Notebooks</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the Jupyter notebooks in
                                    <a class="reference external" href="https://github.com/colour-science/colour-notebooks">colour-notebooks</a>
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Zenodo - Stage 1</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Reserve
                                    <a class="reference external" href="https://zenodo.org/record/376790">Zenodo DOI
                                    </a>
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Colour - Stage 1</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Check
                                    <a class="reference external" href="https://app.codacy.com/app/colour-science/colour/dashboard">codacy</a>
                                </label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>formatting</em> task with
                                    <a class="reference external" href="https://github.com/google/yapf">Yapf</a>, it is very slow on
                                    <em>Colour</em> and is currently not run by default.

                                </label>
                            </div>
                            <pre class="code shell">$ invoke formatting --yapf</pre>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>examples</em> task with
                                    <em>figures</em>: They currently need to be visually assessed for correctness.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke examples --plots</pre>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>preflight</em> task: It runs various unit tests, code formatting, code quality tasks and
                                    also run the examples.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke preflight</pre>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>

        <li>
            <dl>
                <dt>Pypi - Stage 1</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>virtualise</em> task: It builds the project, deploy it to a virtual environment and run the
                                    unit tests.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke virtualise</pre>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Colour - Stage 2</dt>
                <dd>
                    <ul>
                        <li>
                            <dl>
                                <dt>Raise Package Version</dt>
                                <dd>
                                    <ul style="list-style-type: none;">
                                        <li>
                                            <div class="checkbox">
                                                <input type="checkbox" value="" />
                                                <label class="strikethrough">
                                                    <a class="reference external" href="https://github.com/colour-science/colour/blob/develop/colour/__init__.py">__init__.py</a>
                                                </label>
                                            </div>
                                        </li>
                                    </ul>
                                    <p>A typical commit message for version raise is as follows:</p>
                                    <pre class="literal-block">Raise package version to 0.3.9.</pre>
                                </dd>
                            </dl>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <dl>
                                <dt>Update Zenodo DOI</dt>
                                <dd>
                                    <ul style="list-style-type: none;">
                                        <li>
                                            <div class="checkbox">
                                                <input type="checkbox" value="" />
                                                <label class="strikethrough">
                                                    <a class="reference external" href="https://github.com/colour-science/colour/blob/develop/README.rst">README.rst</a>
                                                </label>
                                            </div>
                                        </li>
                                    </ul>
                                </dd>
                            </dl>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Git</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>tag</em> task: It will prompt for tagging the repository accordingly to defined version using
                                    <a class="reference external" href="https://danielkummer.github.io/git-flow-cheatsheet/">git-flow</a>.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke tag</pre>
                            <p>A typical tag message for a <em>Colour</em> version is as follows:</p>
                            <pre class="literal-block">Create Colour v0.3.11 version.</pre>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Pypi - Stage 2</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>release</em>
                                    task: It releases the project to
                                    <a class="reference external" href="https://pypi.python.org/pypi/colour-science">Pypi</a> with
                                    <a class="reference external" href="https://pypi.python.org/pypi/twine">Twine</a>.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke release</pre>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Zenodo - Stage 2</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Upload Pypi package and create new version in
                                    <a class="reference external" href="https://zenodo.org/record/376790">Zenodo</a>
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Conda-Forge</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Create new
                                    <a class="reference external" href="https://github.com/conda-forge/colour-science-feedstock/blob/master/recipe/meta.yaml#L2">conda-forge</a>
                                    version. The
                                    <a class="reference external" href="https://github.com/conda-forge/colour-science-feedstock/blob/master/recipe/meta.yaml#L3">sha256</a>
                                    attribute must be updated and can be computed with the
                                    <em>sha256</em> task:
                                </label>
                            </div>
                            <pre class="code shell">$ invoke sha256</pre>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>colour-science.org</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <dl>
                            <dt>Update Release Links</dt>
                            <dd>
                                <ul style="list-style-type: none;">
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough">
                                                <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/conf.py">conf.py</a>
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough">
                                                <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/pages/index.rst">index.rst</a>
                                            </label>
                                        </div>
                                    </li>
                                </ul>
                            </dd>
                        </dl>
                    </ul>
                    <ul style="list-style-type: none;">
                        <dl>
                            <dt>Update Documentation Links</dt>
                            <dd>
                                <ul style="list-style-type: none;">
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough">
                                                <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/pages/api-reference.rst">api-reference.rst</a>
                                            </label>
                                        </div>
                                    </li>
                                </ul>
                            </dd>
                        </dl>
                    </ul>
                    <ul>
                        <dl>
                            <dt>Update Zenodo Badge</dt>
                            <dd>
                                <ul style="list-style-type: none;">
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough">
                                                <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/conf.py">conf.py</a>
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough">
                                                <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/pages/api-status-and-badges.rst">api-status-and-badges.rst</a>
                                            </label>
                                        </div>
                                    </li>
                                </ul>
                            </dd>
                        </dl>
                    </ul>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run
                                    <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/pages/tutorial.ipynb">tutorial.ipynb</a>
                                    Jupyter notebook
                                </label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Update
                                    <a class="reference external" href="https://github.com/colour-science/colour-science.org/blob/master/pages/features.rst">features.rst</a>
                                    page
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
        <li>
            <dl>
                <dt>Propaganda & Announcement</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">
                                    <a class="reference external" href="https://groups.google.com/forum/#!forum/colour-science/">colour-science - Google Groups</a>
                                </label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">3D-Pro</label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">
                                    <a class="reference external" href="https://buffer.com/">Buffer (Facebook/Linkedin/Twitter)
                                    </a>
                                </label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">
                                    <a class="reference external" href="https://news.ycombinator.com/">Hacker News
                                    </a>
                                </label>
                            </div>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">
                                    <a class="reference external" href="https://www.reddit.com/r/Python/">Reddit</a>
                                </label>
                            </div>
                        </li>
                    </ul>
                </dd>
            </dl>
        </li>
    </ul>