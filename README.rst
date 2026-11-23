colour-science.org
==================

Introduction
------------

Website code for https://www.colour-science.org/

Building the website
--------------------

Install the Python dependencies with ``uv sync``, make Dart Sass and Node.js
20 or newer available on your PATH, and install the frontend dependencies
with ``npm ci``.
Run ``uv run nikola build`` to render the Mako templates and compile both
stylesheets into ``output/``, which is the deployment directory. Build in
place and preserve historical documentation in that directory. Include the
updated generated files when committing a website release. Serve the result
locally with ``uv run nikola serve``.

Use ``uv run invoke clean`` to reset the build cache while retaining
``output/``.

The shared templates and Tailwind stylesheet are in
``themes/colour-science/templates/`` and
``themes/colour-science/tailwind/site.css``. The existing Sass stylesheet
supplies Bootstrap compatibility for older site content and widgets.

Code of Conduct
---------------

The *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,
is available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct>`__ page.

Contact & Social
----------------

The *Colour Developers* can be reached via different means:

- `Email <mailto:colour-developers@colour-science.org>`__
- `Facebook <https://www.facebook.com/python.colour.science>`__
- `Gitter <https://gitter.im/colour-science/colour>`__
- `X <https://x.com/colour_science>`__
- `Bluesky <https://bsky.app/profile/colour-science.bsky.social>`__

About
-----

| **colour-science.org** by Colour Developers
| Copyright 2013 Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__
| This software is released under terms of BSD-3-Clause: https://opensource.org/licenses/BSD-3-Clause
| `https://github.com/colour-science/colour-science.org <https://github.com/colour-science/colour-science.org>`__
