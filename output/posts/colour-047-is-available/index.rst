.. title: Colour 0.4.7 is available!
.. slug: colour-047-is-available
.. date: 2025-12-06 08:37:03 UTC
.. tags: colour, colour science, release
.. category:
.. link:
.. description:
.. type: text

The colour-science Developers are pleased to announce the release of
`Colour 0.4.7 <https://github.com/colour-science/colour/releases/tag/v0.4.7>`__!

.. TEASER_END

This release introduces new chromatic adaptation transform, colour appearance model and colourspaces, thin film optics via the *Transfer Matrix Method*, and significant performance optimisations. It also marks the adoption of `Claude Code <https://docs.anthropic.com/en/docs/claude-code>`__ for development assistance.

The highlights are as follows:

**Dependencies & Compatibility**

- Support for `Python 3.14 <https://docs.python.org/3.14/whatsnew/3.14.html>`__
- `scipy <https://scipy.org>`__ and `imageio <https://imageio.readthedocs.io>`__ are now optional dependencies
- Dropped `typing-extensions <https://github.com/python/typing_extensions>`__ requirement
- Updated minimum versions: numpy >=2.0.0, scipy >=1.13.0, matplotlib >=3.9, networkx >=3.3, pandas >=2.2

**Colour Adaptation & Appearance**

- Implemented *Li (2025)* chromatic adaptation transform
- Added *sCAM* colour appearance model with conversion definitions

**Colour Models**

- Introduced *sUCS* colour space with multiple conversion functions
- Added 12 new *RGB* colourspaces from the `Color Interop Forum <https://github.com/AcademySoftwareFoundation/ColorInterop>`__ recommendation for `ColorSpace Encodings for Texture Assets and CG Rendering <https://docs.google.com/document/d/1IV3e_9gpTOS_EFYRv2YGDuhExa4wTaPYHW1HyV36qUU>`__
- Implemented *Filmlight E-Gamut 2* and *Fujifilm F-Gamut C* colourspaces
- Added *Xiaomi Mi-Log Profile* encoding/decoding definitions
- Enhanced *OSA-UCS* conversion with improved accuracy and 28.5x performance gain

**Optical Phenomena**

- Implemented *Transfer Matrix Method* for thin film structures
- Added *Snell's law* and polarised light calculations
- Introduced comprehensive plotting definitions for thin film analysis

.. image:: https://github.com/user-attachments/assets/a7cfa4ae-6a4c-4c2f-9527-c2706ad8ab74

.. image:: https://github.com/user-attachments/assets/feb5c964-bcf3-468b-a23f-7f06dbee32c3

**Quality Metrics**

- Added Japanese skin complexion spectral data
- Extended spectral similarity index to support ``MultiSpectralDistributions``

**Documentation**

- Each documented object has been `verified and processed with a LLM <https://github.com/colour-science/colour-science.meta/blob/master/.claude/scripts/docstring_processor.py>`__ to improve consistency and correct typos and mistakes

**Utilities**

- Introduced metadata system for documenting input/output value ranges via type annotations

**Performance Improvements**

- Trilinear and tetrahedral interpolation: 1.3x faster
- *Robertson (1968)* colour temperature conversions: 30-90x faster
- *scipy* import optimisation for reduced load times

Please take a look at the `releases <https://github.com/colour-science/colour/releases/tag/v0.4.7>`__
page more information.
