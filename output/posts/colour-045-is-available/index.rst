.. title: Colour 0.4.5 is available!
.. slug: colour-045-is-available
.. date: 2024-10-10 09:24:11 UTC+01:00
.. tags: colour, colour science, release
.. category: 
.. link: 
.. description: 
.. type: text

The colour-science Developers are pleased to announce the release of
`Colour 0.4.5 <https://github.com/colour-science/colour/releases/tag/v0.4.5>`__!

.. TEASER_END

This release implements support for `Python 3.13 <https://docs.python.org/3/whatsnew/3.13.html>`__ and `Numpy 2 <https://numpy.org/devdocs/release/2.0.0-notes.html>`__.

The highlights of this release are as follows:

- `pygraphviz <https://pygraphviz.github.io>`__ was replaced with `pydot <https://github.com/pydot/pydot>`__ so that installation is easier.
- We switched from `Poetry <https://python-poetry.org`__ to `uv <https://docs.astral.sh/uv>`__ and `hatch <http://hatch.pypa.io>`__ for managing the development environment and build our wheels.

    - *uv* is so good that it literally only requires `uv run --with colour-science my_script.py` to run a script using **Colour**.

- Our `environment variables <https://colour.readthedocs.io/en/develop/advanced.html#environment>`__ can now be loaded from a `JEnv` file:

.. code:: json

    {
      "COLOUR_SCIENCE__COLOUR__SHOW_WARNINGS_WITH_TRACEBACK": "True"
    }

- Support for `pathlib <https://docs.python.org/3/library/pathlib.html>`__ in IO definitions
- Support for *vK20* chromatic adaptation transform
- Support for polar conversions to all relevant models
- Port-based nodes and graphs for processing graphs

.. code:: python

    class NodeAdd(PortNode):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.description = "Perform the addition of the two input port values."

            self.add_input_port("a")
            self.add_input_port("b")
            self.add_output_port("output")

        def process(self):
            a = self.get_input("a")
            b = self.get_input("b")

            if a is None or b is None:
                return

            self._output_ports["output"].value = a + b

            self.dirty = False

    class NodeMultiply(PortNode):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.description = (
                "Perform the multiplication of the two input port values."
            )

            self.add_input_port("a")
            self.add_input_port("b")
            self.add_output_port("output")

        def process(self):
            a = self.get_input("a")
            b = self.get_input("b")

            if a is None or b is None:
                return

            self._output_ports["output"].value = a * b

            self.dirty = False

    node_add = NodeAdd()
    node_add.set_input("a", 1)
    node_add.set_input("b", 1)
    node_multiply = NodeMultiply()
    node_multiply.set_input("b", 2)

    graph = PortGraph()

    graph.add_node(node_add)
    graph.add_node(node_multiply)

    graph.connect(node_add, "output", node_multiply, "a")

    graph.process()

    print(node_multiply.get_output("output"))

Please take a look at the `releases <https://github.com/colour-science/colour/releases/tag/v0.4.5>`__
page more information.
