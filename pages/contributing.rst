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

-   Reporting a defect, proposing a new feature, an enhancement or
    commenting existing issues on the `Issue
    Tracker <https://github.com/colour-science/colour/issues>`__.
-   Contributing new code by implementing new features or adding
    examples. For some ideas you can take a look at the issues with the
    `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`__ and
    `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`__
    labels or the
    `v9.9.9 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+milestone%3Av9.9.9>`__
    milestone.
-   Maintaining the existing code base, improving the code style and quality,
    improving the coverage, updating the documentation, fixing bugs, addressing
    TODOs, etc... Issues with the
    `Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`__
    or
    `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`__
    labels are a good place to start.
-   Improving siblings packages:

    -   `Colour - Datasets </colour-datasets/>`__
    -   `Colour - Demosaicing </colour-demosaicing/>`__
    -   `Colour - HDRI </colour-hdri/>`__
    -   `Colour - Checker Detection </colour-checker-detection/>`__
    -   `Colour - Maya </colour-maya/>`__
    -   `Colour - Nuke </colour-nuke/>`__
    -   `Colour - Spectroscope </colour-spectroscope/>`__

-   Participating in discussions on the `Mailing List <colour-science@googlegroups.com>`__.

**Github** hosts a `First Contributions <https://github.com/firstcontributions/first-contributions>`__
repository with good information for new comers.

Reporting Issues
----------------

The three major issue types one can report on the issue tracker are the
following:

-   `Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`__
-   `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`__
-   `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`__

We currently use a large set of labels to categorise issues:

-   `Defect <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADefect>`__:
    Used for any kind of defect reported.

    -    `Critical <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ACritical>`__:
         Used for issues either rendering the software unusable, causing loss of
         data, or preventing people to work. These issues need to be fixed
         immediately.
    -    `Major <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AMajor>`__:
         Used for issues which have significant consequences on the ability of
         people to work but do not lead to the whole API being unusable.
    -    `Normal <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ANormal>`__:
         Used for issues affecting one piece of functionality. Those are usually
         self-contained and don't impact the overall functionality of the API.
    -    `Minor <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AMinor>`__:
         Used for cosmetic issues that don't prevent the API to run properly.

-   `Enhancement <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AEnhancement>`__:
    Used for an enhancement of an existing feature, can also be used for new
    feature suggestion, although
    `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`__
    label should be preferred.
-   `Feature <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AFeature>`__:
    Used for a new feature, functionality suggestion.

    -    `P1 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP1>`__:
         Used for the highest priority.
    -    `P2 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP2>`__:
         Used for average priority.
    -    `P3 <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AP3>`__:
         Used for the lowest priority.

-   `API <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AAPI>`__:
    Used for issues related to the API.
-   `Discarded <https://github.com/colour-science/colour/issues?q=is%3Aclose+is%3Aissue+label%3ADiscarded>`__:
    Used for a discarded / canceled issue.
-   `Discussion <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADiscussion>`__:
    Used to discuss any subject, those issues often turn into features or
    enhancement.
-   `Distribution <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADistribution>`__:
    Used to discuss distribution and packaging of the API.
-   `Documentation <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADocumentation>`__:
    Used for issues related to the documentation.
-   `Duplicate <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADuplicate>`__:
    Used for a duplicate issue.
-   `Examples <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3AExamples>`__:
    Used for issues related to the examples.
-   `Postponed <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3APostponed>`__:
    Used for an issue postponed for a future milestone.
-   `Task <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ATask>`__:
    Used for a task not directly related to pure programming.
-   `Good First Issue <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Good+First+Issue">`__:
    Used for an issue appropriate for a first time contribution.
-   `Help Wanted <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Help+Wanted">`__:
    Used for an issue appropriate for a first time contribution but likely harder than a
    `Good First Issue <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Good+First+Issue">`__ one.
-   `Hacktoberfest <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3A"Hacktoberfest">`__:
    Used for an issue relevant to `Digital Ocean's Hacktoberfest <https://hacktoberfest.digitalocean.com>`__.

Defects
^^^^^^^

You encountered a problem while using **Colour**, please consider reporting it
on the `Issue Tracker <https://github.com/colour-science/colour/issues>`__.

The first thing to do, is to check if there are any existing issues describing
your problem, if there is one, you are welcome commenting into it and provide
more details. However, please avoid creating duplicates, they add noise to the
issue tracker and we will have to label them as
`Duplicate <https://github.com/colour-science/colour/issues?q=is%3Aopen+is%3Aissue+label%3ADuplicate>`__
and close them.

When reporting a defect please provide the output of the following command if
possible, and if it makes sense to do so:

.. code:: shell

    $ python -c "import colour;colour.utilities.describe_environment()"

The typical output is something along those lines:

::

    ===============================================================================
    *                                                                             *
    *   Interpreter :                                                             *
    *       python : 3.7.4 (default, Sep  7 2019, 18:27:02)                       *
    *                [Clang 10.0.1 (clang-1001.0.46.4)]                           *
    *                                                                             *
    *   colour-science.org :                                                      *
    *       colour : v0.3.13-236-g476410d4                                        *
    *                                                                             *
    *   Runtime :                                                                 *
    *       numpy : 1.16.5                                                        *
    *       scipy : 1.2.2                                                         *
    *       pandas : 0.24.2                                                       *
    *       matplotlib : 2.2.4                                                    *
    *       OpenImageIO : 2.0.9                                                   *
    *                                                                             *
    ===============================================================================

If you are reporting an exception, please provide the complete traceback, it
will help us tremendously understand what happened.

Features & Enhancements
^^^^^^^^^^^^^^^^^^^^^^^

If you would like a new feature to be supported or an enhancement of an
existing feature, don't hesitate to link any resources or references you feel
like would help its implementation: publications, wikipedia article, etc...

If there is an implementation existing in another language, we will be most
likely be able to port it although the licence must be compatible with the
`New BSD License <https://opensource.org/licenses/BSD-3-Clause>`__ terms.

We are also running `Matlab <http://www.mathworks.fr/products/matlab/>`__, so
don't hesitate to provide snippets for it if you have functions you would like
to be ported.

Contributing Code
-----------------

Assuming you have something to work on, you will have to get the code and
follow the guidelines.

Development for Colour
^^^^^^^^^^^^^^^^^^^^^^

Here is a succinct overview of the steps you will most likely go through:

Step 1
******

`Fork <https://github.com/colour-science/colour/fork>`__ the
`Colour <https://github.com/colour-science/colour>`__ repository.

Step 2
******

Clone the repository locally to your workspace:

.. code:: shell

    $ git clone git@github.com:$USER/colour.git

Step 3
******

Navigate to the *colour* directory:

.. code:: shell

    $ cd colour

Step 4
******

Assuming `Python>=3.5 <https://www.python.org/download/releases/>`__ is
available on your system, the development dependencies are installed with
`Poetry <https://poetry.eustace.io>`__ as follows:

.. code:: shell

    $ poetry install --extras "optional plotting"

.. class:: alert alert-dismissible alert-warning

    | **Warning**
    |
    | As of this writing, we are still supporting `Python 2.7 <https://www.python.org/download/releases/>`__ which might produce issues when resolving
        dependencies with a `Python 3.8 <https://www.python.org/download/releases/>`__
        interpreter. We are indeed effectively patching the
        `pyproject.toml <https://github.com/colour-science/colour/blob/develop/pyproject.toml>`__
        file on `Github Actions <https://github.com/colour-science/colour/actions>`__:

        .. code:: shell

                $ sed -i.bak 's/python = "~2.7 || ^3.5"/python = "^3.6"/g' pyproject.toml
                $ sed -i.bak 's/matplotlib = { version = "\*"/matplotlib = { version = "^3.1"/g' pyproject.toml
                $ git diff --unified=1
                diff --git a/pyproject.toml b/pyproject.toml
                index 93088d8c..c2b282cf 100644
                --- a/pyproject.toml
                +++ b/pyproject.toml
                @@ -46,3 +46,3 @@ classifiers = [
                 [tool.poetry.dependencies]
                -python = "~2.7 || ^3.5"
                +python = "^3.6"
                 imageio = "*"
                @@ -58,3 +58,3 @@ invoke = { version = "*", optional = true }  # Development dependency.
                 jupyter = { version = "*", optional = true }  # Development dependency.
                -matplotlib = { version = "*", optional = true }
                +matplotlib = { version = "^3.1", optional = true }
                 mock = { version = "*", optional = true }  # Development dependency.

If `Graphviz <https://www.graphviz.org/>`__ is available on your system, you
might issue the following commands instead of the aforementioned ones:

.. code:: shell

    $ git clone git://github.com/colour-science/colour.git
    $ cd colour
    $ poetry install --extras "graphviz optional plotting"

.. class:: alert alert-dismissible alert-warning

    | **Warning**
    |
    | Various **Colour** unit tests require being able to perform IO with
        `OpenEXR <https://www.openexr.com/>`__ images. You will need to install
        the *FreeImage* plugin for `Imageio <http://imageio.github.io/>`__ as
        follows: `python -c "import imageio;imageio.plugins.freeimage.download()"`

If you are in a hurry and not willing to prepend each command with `poetry run`,
it is possible to put the following function in your `.bash_profile`:

.. code:: shell

    function poem() {
        if [[ -n "$@" ]]; then
            poetry env use "$@"
        else
            poetry env use 3
        fi;

        if [ -f "pyproject.toml" ]; then
            source $(poetry env info -p)/bin/activate
        else
            echo "The current directory has no associated \"poetry\" capability!"
        fi;
    }

Then issuing `poem` will activate the appropriate virtual environment for your
clone.

Step 5
******

Install the `pre-commit <https://pre-commit.com/>`__ hooks:

.. code:: shell

    $ poetry run pre-commit install

Step 6
******

Connect your clone to the original *upstream* repository by adding it as a
remote:

.. code:: shell

    $ git remote add upstream git@github.com:colour-science/colour

Step 7
******

You should now have two remotes:

.. code:: shell

    $ git remote -v
    origin  https://github.com/$USER/colour (fetch)
    origin  https://github.com/$USER/colour (push)
    upstream  https://github.com/colour-science/colour (fetch)
    upstream  https://github.com/colour-science/colour (push)

Step 8
******

Pull the latest changes from *upstream*:

.. code:: shell

    $ git checkout develop
    $ git pull upstream develop

Step 9
******

Create a branch for your contribution:

The core developers are using the
`git flow branching model <http://nvie.com/posts/a-successful-git-branching-model/>`__
for most of the development tasks and since the branch name appears in the
commit message and for consistency, please use the following branch
prefixes:

-   Feature branch prefix: **feature/**
-   Release branch prefix: **release/**
-   Hotfix branch prefix: **hotfix/**

As an example, working to implement `Mie Scattering <https://en.wikipedia.org/wiki/Mie_scattering>`__
support:

.. code:: shell

    $ git checkout -b feature/mie_scattering

Step 10
*******

Check if the unit tests and doctests are running properly:

.. code:: shell

    $ poetry run invoke tests

or alternatively:

.. code:: shell

    $ source $(poetry env info -p)/bin/activate
    $ invoke tests

Step 11
*******

Commit your changes:

.. code:: shell

    $ git add mie_scattering.py
    $ git commit -m 'Implement "Mie Scattering" support.'

.. class:: alert alert-dismissible alert-info

    | **Note**
    |
    | The *pre-commit* hooks will run before committing, notably
        `Flake8 <https://pypi.org/project/flake8/>`__ and
        `YAPF <https://github.com/google/yapf>`__ thus depending their status,
        you might not be able to commit until you have fixed the issues they
        reported.

Step 12
*******

Push your changes to *origin*, i.e. your own fork:

.. code:: shell

    $ git push origin feature/mie_scattering

Step 13
*******

Visit your repository fork on `Github <https://github.com/$USER/colour>`__.
Your branch should have a green *Pull Request* button, this will open a
*pull request* and let us know that we have some code to review :)

Step 14
*******

Check that the `continuous integration <https://github.com/colour-science/colour/actions>`__
suite succeeded.

Code Reviews
------------

Your *pull request* will be reviewed by the maintainers and any other developer
interested by the project.

Every single developer has his code reviewed, this is a natural process helping
to raise the codebase quality around a friendly and constructive discussion.
Comments will be made on various aspects such as the documentation and
references, the code style and its implementation. Those can be discouraging,
although they are not meant to criticize but aim at improving the quality of
your submission. We all learn from that process and the project ultimately
benefits from them.

Guidelines
----------

Most of the conventions used in **Colour** are the same than
`NumPy <http://www.numpy.org/>`__, `SciPy <http://www.scipy.org/>`__ and
`scikit-image <http://scikit-image.org/>`__.

Overview
^^^^^^^^

We follow the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`__
and especially the *Python Language Rules* although with the main exception
being the docstrings / documentation formatted with
`Numpy Docstrings Style <https://github.com/numpy/numpy/blob/master/doc/example.py>`__.

The code has to be `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`__
compliant although but before anything else, it needs to be consistent with the
Colour Science litterature:

For example, the base **CIE** colourspace is **CIE XYZ** with upper case
notation. It can be converted to chromaticity coordinates **xy** with lower
case notation. If we were to fully abide by the
`PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`__ recommendations, we
would have written a conversion definition as follows:

.. code:: python

    def xyz_to_xy(xyz):
        x, y, z = np.ravel(xyz)
        x, y = x / (x + y + z), y / (x + y + z)
        return x, y

Abstracting the fact that the above definition is totally undocumented, it can
be confusing to understand when we are referencing big **X** tristimulus value
or little **x** chromaticity coordinate.

For those cases, and there are legions of them in Colour Science, we have
decided to go for clarity and consistency with the literature for the object
names:

.. code:: python

    def XYZ_to_xy(XYZ):
        X, Y, Z = np.ravel(XYZ)
        x, y = X / (X + Y + Z), Y / (X + Y + Z)
        return x, y

When the reference is using upper case named variables, we try to follow
the same convention, it is unfortunately not
`PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`__ compliant but has the
benefit of a much easier comparison between the implementation and the
reference.

We suggest that contributors follow the same rule.

Python Language Rules
^^^^^^^^^^^^^^^^^^^^^

-   All the code must be covered by unit tests and doctests.
-   All the code must be documented to the same standard than
    `NumPy <http://www.numpy.org/>`__, `SciPy <http://www.scipy.org/>`__
    and `scikit-image <http://scikit-image.org/>`__.
-   All the code must be checked with the static analysis tool of your choice,
    e.g. `PyCharm <http://www.jetbrains.com/pycharm/>`__ ,
    `Flake8 <https://pypi.org/project/flake8>`__, or
    `Codacy <https://www.codacy.com/>`__.
-   No *pull request* should be merged without being reviewed and ensuring that
    the `Github Actions <https://github.com/colour-science/colour/actions>`__
    continuous integration suite succeeded.
-   Examples should be provided for new features.

Python Style Rules
^^^^^^^^^^^^^^^^^^

-   Ensure consistency with Colour Science literature first.
-   Ensure `PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`__ compliance.
-   Try using a close to *LaTeX* syntax for variables names so that they are
    easier to compare to the reference.

    For instance, a variable defined \\(D\_{uv}\\) in a paper would be defined
    as *D\_uv* in the code, \\(L^\*\\) as *Lstar* and \\(X\_{ab}^{\\prime}\\)
    as *Xp\_ab*.
-   Try using uppercase for author names in definitions:

.. code:: python

    def CCT_to_xy_Kang2002(CCT):

-   Please use *British English* words instead of *American English* ones as
    the **CIE** does, the most important of all being **colour** instead of
    **color**. You can consult the `CIE Termlist <http://eilv.cie.co.at/>`__ if
    any doubts.
-   Import `NumPy <http://www.numpy.org/>`__ as follows:

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
        rounded to 15 digits if computed with the API (spectral
        distributions, chromaticity coordinates, etc...).
    -   Unit tests and doctests input numbers are kept as is if they are from
        a reference or rounded to 8 digits if computed with the API.
    -   Unit tests output numbers are rounded to 8 digits.
    -   Doctests output numbers trimmed with **ellipsis** to 7 digits.

-   We recommend a set of values for use with examples and unit tests.
    A `Gist <https://gist.github.com/KelSolaar/2ca5f4107a8ae05ec57a55a9ae2f3a13>`__
    is available with the generating code.

    Priority should be given for CIE Standard Illuminant D Series D65 computed
    values:

.. code:: text

    Recommended Values for Use in Colour Examples and Unit Tests

    Illuminants "xy"

    D65 : array([0.31270000, 0.32900000])
    D50 : array([0.34570000, 0.35850000])
    A : array([0.44757000, 0.40745000])
    E : array([0.33333333, 0.33333333])
    F2 : array([0.37208000, 0.37529000])
    CC I : array([0.34570000, 0.35850000])


    Illuminants "XYZ"

    D65 : array([0.95045593, 1.00000000, 1.08905775])
    D50 : array([0.96429568, 1.00000000, 0.82510460])
    A : array([1.09846607, 1.00000000, 0.35582280])
    F2 : array([0.99144661, 1.00000000, 0.67315942])
    E : array([1.00000000, 1.00000000, 1.00000000])
    CC I : array([0.96429568, 1.00000000, 0.82510460])


    ColorChecker 2005 "XYZ" Adapted to "D65"

    red : array([0.20654008, 0.12197225, 0.05136952])
    green : array([0.14222010, 0.23042768, 0.10495772])
    blue : array([0.07818780, 0.06157201, 0.28099326])
    cyan : array([0.14525849, 0.19799077, 0.40724370])
    yellow : array([0.55676530, 0.58671628, 0.09785344])
    magenta : array([0.30795495, 0.20024152, 0.31071274])
    neutral 5 (.70 D) : array([0.18182171, 0.19153665, 0.21009620])


    ColorChecker 2005 "XYZ" Adapted to "D50"

    red : array([0.21638819, 0.12570000, 0.03847493])
    green : array([0.14985004, 0.23180000, 0.07900179])
    blue : array([0.06857861, 0.05750000, 0.21375591])
    cyan : array([0.13605127, 0.19300000, 0.30938736])
    yellow : array([0.59342537, 0.59810000, 0.07188823])
    magenta : array([0.31084193, 0.20090000, 0.23565391])
    neutral 5 (.70 D) : array([0.18438363, 0.19150000, 0.15918203])


    ColorChecker 2005 "XYZ" Adapted to "A"

    red : array([0.25330530, 0.13765139, 0.01543307])
    green : array([0.18673833, 0.23111171, 0.03285972])
    blue : array([0.05610693, 0.04992541, 0.09429057])
    cyan : array([0.13623492, 0.18062024, 0.13553082])
    yellow : array([0.73088905, 0.62177441, 0.02548927])
    magenta : array([0.34280970, 0.20770559, 0.10214220])
    neutral 5 (.70 D) : array([0.20988974, 0.19141324, 0.06866269])


    ColorChecker 2005 "XYZ" Adapted to "E"

    red : array([0.21781186, 0.12541048, 0.04697113])
    green : array([0.15434689, 0.22960951, 0.09620221])
    blue : array([0.07683480, 0.06006092, 0.25833845])
    cyan : array([0.14893167, 0.19487065, 0.37427698])
    yellow : array([0.59874058, 0.59196415, 0.08899633])
    magenta : array([0.31991986, 0.20277158, 0.28536138])
    neutral 5 (.70 D) : array([0.19126715, 0.19151544, 0.19291812])


    ColorChecker 2005 "XYZ" Adapted to "F2"

    red : array([0.22545552, 0.12877805, 0.03103172])
    green : array([0.15832594, 0.23204226, 0.06406107])
    blue : array([0.06385467, 0.05509729, 0.17506386])
    cyan : array([0.13364947, 0.18951306, 0.25307753])
    yellow : array([0.62718558, 0.60525456, 0.05690008])
    magenta : array([0.31720246, 0.20226568, 0.19243480])
    neutral 5 (.70 D) : array([0.18952683, 0.19147512, 0.12987334])


    Luminance "XYZ" Adapted to "D65"

    red : 12.19722535
    green : 23.04276781
    blue : 6.15720079
    cyan : 19.79907683
    yellow : 58.67162787
    magenta : 20.02415243
    neutral 5 (.70 D) : 19.15366501


    Luminance "XYZ" Adapted to "D50"

    red : 12.57000000
    green : 23.18000000
    blue : 5.75000000
    cyan : 19.30000000
    yellow : 59.81000000
    magenta : 20.09000000
    neutral 5 (.70 D) : 19.15000000


    Luminance "XYZ" Adapted to "A"

    red : 13.76513858
    green : 23.11117127
    blue : 4.99254109
    cyan : 18.06202404
    yellow : 62.17744084
    magenta : 20.77055938
    neutral 5 (.70 D) : 19.14132354


    Luminance "XYZ" Adapted to "E"

    red : 12.54104823
    green : 22.96095053
    blue : 6.00609174
    cyan : 19.48706483
    yellow : 59.19641488
    magenta : 20.27715822
    neutral 5 (.70 D) : 19.15154358


    Luminance "XYZ" Adapted to "F2"

    red : 12.87780528
    green : 23.20422641
    blue : 5.50972884
    cyan : 18.95130571
    yellow : 60.52545632
    magenta : 20.22656850
    neutral 5 (.70 D) : 19.14751195


    ColorChecker 2005 "sRGB - Linear" under "D65"

    red : array([0.45620519, 0.03081071, 0.04091952])
    green : array([0.05433312, 0.29879493, 0.07185472])
    blue : array([0.01862364, 0.05140184, 0.28880425])
    cyan : array([-0.03667845, 0.24755074, 0.39815738])
    yellow : array([0.85356364, 0.56517342, 0.01475279])
    magenta : array([0.53522616, 0.09013008, 0.30472718])
    neutral 5 (.70 D) : array([0.19002735, 0.19183638, 0.19312568])


    ColorChecker 2005 "sRGB - OETF" under "D65"

    red : array([0.70573936, 0.19248268, 0.22354168])
    green : array([0.25847007, 0.58276101, 0.29718877])
    blue : array([0.14565317, 0.25130933, 0.57378757])
    cyan : array([-0.47388561, 0.53467479, 0.66380090])
    yellow : array([0.93264474, 0.77675390, 0.12708884])
    magenta : array([0.75809823, 0.33206288, 0.58800664])
    neutral 5 (.70 D) : array([0.47315229, 0.47524148, 0.47672343])


    ColorChecker 2005 "Munsell Value"

    red : 4.08244375
    green : 5.39132685
    blue : 2.97619312
    cyan : 5.06675596
    yellow : 8.04387670
    magenta : 5.10225899
    neutral 5 (.70 D) : 4.98656896


    ColorChecker 2005 "ASTM D1535-08e1 Luminance"

    red : 12.23634268
    green : 22.89399987
    blue : 6.29022535
    cyan : 19.86282567
    yellow : 58.37987916
    magenta : 20.18160934
    neutral 5 (.70 D) : 19.15426585

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
-   The code formatting is performed using
    `Yapf <https://github.com/google/yapf>`__. You can invoke it recursively on
    a directory as follows:

.. code:: shell

    $ poetry run yapf -ri colour/my_feature

or alternatively:

.. code:: shell

    $ source $(poetry env info -p)/bin/activate
    $ yapf -ri colour/my_feature

-   Inline comments must have two spaces.
-   Ensure that you have blank line at the end of the files.
-   Ensure that trailing whitespaces are stripped.
-   Prefix unused variable with an underscore:

.. code:: python

    _L, a, b = tsplit(Lab)

Citations
^^^^^^^^^

It's likely that the code you contribute will be based upon references, we are
using a slightly modified `APA 7th Edition <http://www.apastyle.org/>`__
citation style `available for download </others/american-psychological-association-7th-edition-colour-science.csl>`__
and generating citations as follows:

::

    Davis, W., & Ohno, Y. (2010). Color quality scale. Optical Engineering, 49(3), 033602. doi:10.1117/1.3360335

::

    Wyszecki, G., & Stiles, W. S. (2000). Table I(6.5.3) Whiteness Formulae (Whiteness Measure Denoted by W). In Color Science: Concepts and Methods, Quantitative Data and Formulae (pp. 837–839). Wiley. ISBN:978-0-471-39918-6

::

    Lindbloom, B. (2014). RGB Working Space Information. Retrieved April 11, 2014, from http://www.brucelindbloom.com/WorkingSpaceInfo.html

We are storing all our citations in a database maintained by
`Zotero <https://www.zotero.org/>`__ and it is recommended that you are given
a citation key by us.

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

    This implementation allows for a more precise correlated colour temperature
    calculation by using a two solutions hybrid approach.

    Closes #32.

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
branch, please inform the `Colour Developers <mailto:colour-developers@colour-science.org>`__
in order to avoid commit losses or a merging disaster.

Releasing Colour
----------------

The following stages help maintainers navigate through the release of a new
version of **Colour**, some automation is provided by `Invoke <http://www.pyinvoke.org/>`__:

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
                                <label class="strikethrough">Check open issues
                                    on the current
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
                <dt>Zenodo - Stage 1</dt>
                <dd>
                    <ul style="list-style-type: none;">
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Reserve the
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
                            <dt>Rebuild a clean Virtual Environment</dt>
                            <dd>
                                <ul style="list-style-type: none;">
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough"> Remove the current virtual environment:
                                            </label>
                                        </div>
                                        <pre class="code shell">$ poetry env info -p | xargs rm -r</pre>
                                    </li>
                                    <li>
                                        <div class="checkbox">
                                            <input type="checkbox" value="" />
                                            <label class="strikethrough"> Create a pristine virtual environment:
                                            </label>
                                        </div>
                                        <pre class="code shell">$ rm poetry.lock && poem && poetry install --extras "graphviz optional plotting"</pre>
                                    </li>
                                </ul>
                            </dd>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>formatting</em> task with
                                    <a class="reference external" href="https://github.com/google/yapf">Yapf</a>,
                                    it is very slow on <em>Colour</em> and is
                                    currently not run by default:
                                </label>
                            </div>
                            <pre class="code shell">$ invoke formatting --yapf</pre>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>examples</em> task with <em>figures</em>:
                                    They need to be visually assessed for
                                    correctness.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke examples --plots</pre>
                        </li>
                        <li>
                            <div class="checkbox">
                                <input type="checkbox" value="" />
                                <label class="strikethrough">Run the
                                    <em>build</em> task: It cleans the project,
                                    runs the unit tests, etc...
                                </label>
                            </div>
                            <pre class="code shell">$ invoke build</pre>
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
                                    <em>virtualise</em> task: It deploys the
                                    project to a virtual environment and run the
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
                                        <li>
                                            <div class="checkbox">
                                                <input type="checkbox" value="" />
                                                <label class="strikethrough">
                                                    <a class="reference external" href="https://github.com/colour-science/colour/blob/develop/pyproject.toml">pyproject.toml</a>
                                                </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="checkbox">
                                                <input type="checkbox" value="" />
                                                <label class="strikethrough">
                                                    <a class="reference external" href="https://github.com/colour-science/colour/blob/develop/colour/setup.py">setup.py</a>
                                                </label>
                                            </div>
                                        </li>
                                    </ul>
                                    <p>A typical commit message for version
                                    raise is as follows:</p>
                                    <pre class="literal-block">Raise package version to 0.3.15.</pre>
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
                                    <em>tag</em> task: It should prompt for
                                    tagging the repository accordingly to the
                                    defined version using
                                    <a class="reference external" href="https://danielkummer.github.io/git-flow-cheatsheet/">git-flow</a>.
                                </label>
                            </div>
                            <pre class="code shell">$ invoke tag</pre>
                            <p>A typical tag message for a <em>Colour</em>
                            version is as follows:</p>
                            <pre class="literal-block">Create Colour v0.3.15 version.</pre>
                            In the eventuality where the tag creation failed, it might be created manually as follows:
                            <pre class="code shell">$ git tag -a -m "Create Colour v0.3.15 version." v0.3.15</pre>
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
                                    <a class="reference external" href="https://pypi.org/project/colour-science">Pypi</a> with
                                    <a class="reference external" href="https://pypi.org/project/twine">Twine</a>.
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
                                <label class="strikethrough">Upload the Pypi
                                    package and create new version in
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
                                    attribute must be updated and can be
                                    computed with the
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
                                    <a class="reference external" href="https://colour-science.discourse.group/c/releases/">colour-science - Discourse</a>
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