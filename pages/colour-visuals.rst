.. title: Colour - Visuals
.. slug: colour-visuals
.. date: 2023-10-23 00:00:00 UTC
.. tags: colour, colour science, colour - visuals, webgpu
.. category: 
.. link: 
.. description: 
.. type: text

**Colour - Visuals** is a `Python <https://www.python.org>`__ package
implementing various `WebGPU-based <https://github.com/gpuweb/gpuweb>`__
visuals on top of `pygfx <https://github.com/pygfx/pygfx>`__ for colour science
applications.

.. image:: https://raw.githubusercontent.com/colour-science/colour-visuals/master/docs/_static/Visuals_001.png

Features
--------

Most of the objects are available from the ``colour_visuals`` namespace:

.. code-block:: python

    >>> import colour_visuals

API
^^^

The main technical reference for `Colour - Visuals <https://github.com/colour-science/colour-visuals>`__
is the `API Reference <https://colour-visuals.readthedocs.io/en/latest/reference.html>`__.

.. code-block:: python

    >>> import colour_visuals
    >>> import numpy as np
    >>> import pygfx as gfx
    >>> from wgpu.gui.auto import WgpuCanvas, run

    >>> canvas = WgpuCanvas(size=(960, 540))
    >>> renderer = gfx.renderers.WgpuRenderer(canvas)
    >>> camera = gfx.PerspectiveCamera(50, 16 / 9)
    >>> controller = gfx.OrbitController(camera)
    >>> controller.register_events(renderer)

    >>> scene = gfx.Scene()
    >>> scene.add(
    ...     gfx.Background(
    ...         None, gfx.BackgroundMaterial(np.array([0.18, 0.18, 0.18]))
    ...     )
    ... )

    >>> visuals = [
    ...     colour_visuals.VisualGrid(size=2),
    ...     colour_visuals.VisualChromaticityDiagramCIE1931(
    ...         kwargs_visual_chromaticity_diagram={"opacity": 0.25}
    ...     ),
    ...     colour_visuals.VisualRGBColourspace2D("ACEScg"),
    ...     colour_visuals.VisualRGBColourspace2D(
    ...         "Display P3", colours=np.array([0.5, 0.5, 0.5])
    ...     ),
    ...     colour_visuals.VisualRGBColourspace3D(
    ...         "Display P3", opacity=0.5, wireframe=True
    ...     ),
    ...     colour_visuals.VisualRGBScatter3D(
    ...         np.random.random([24, 32, 3]), "ACEScg"
    ...     ),
    ... ]

    >>> group = gfx.Group()
    >>> for visual in visuals:
    ...     group.add(visual)
    ...
    >>> scene.add(group)

    >>> camera.local.position = np.array([-0.25, -0.5, 2])
    >>> camera.show_pos(np.array([1 / 3, 1 / 3, 0.4]))

    >>> canvas.request_draw(lambda: renderer.render(scene, camera))
    >>> run()

..  image:: https://raw.githubusercontent.com/colour-science/colour-visuals/master/docs/_static/Visuals_002.png

Downloads
^^^^^^^^^

-   `Colour - Visuals Github Repository <https://github.com/colour-science/colour-visuals>`__
-   `Colour - Visuals - Pypi <https://pypi.org/project/colour-visuals>`__
