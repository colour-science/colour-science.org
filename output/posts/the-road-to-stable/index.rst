.. title: The Road to Stable
.. slug: the-road-to-stable
.. date: 2017-08-09 03:23:09 UTC+01:00
.. tags: colour, colour science
.. category:
.. link:
.. description:
.. type: text

Colour has been in public development for over 3 years. The package has grown in various directions since the initial release and offers a significant amount of `features <https://www.colour-science.org/features>`__.

It is used in research groups such as the `St Andrews HCI Research Group <https://sachi.cs.st-andrews.ac.uk>`__ or companies like `Google <https://www.google.com>`__, `Merck KGaA <https://en.wikipedia.org/wiki/Merck_Group>`__ or `The Moving Picture Company <http://www.moving-picture.com>`__. Even though it has reached a certain stability and maturity, it is still in alpha development status.

Two important features are missing for a first feature complete stable release:

- The first one is that our current dictionary based spectral implementation has reached its limits when building support for Machado et al. (2010): attempting to alter the domain or range of a ``SpectralPowerDistribution`` is difficult. With that in mind, we have started to work on a new alternative implementation where data is exposed as a continuous function modeled using an interpolating function encapsulated within an extrapolating function: `#335 <https://github.com/colour-science/colour/issues/335>`__.
- The second is support for metadata inside the API. Most of the codebase adopts definitions/functions over classes to stay clean and lean, the aforementioned spectral implementation being a notable exception. As a consequence, it is hard to implement a non-intrusive classifying mechanism, provide usable hints on functions domain/range or create an auto-conversion layer. We have considered multiple ways of providing the necessary metadata, e.g. `experimental/medatada* branches <https://github.com/colour-science/colour/branches/all>`__, and decided that the true elegant solution was through docstrings.

The following example showcases the current implementation, defining metadata for *parameters*, *returns* and the definition by using the *notes* section:

.. code:: python

    def luminance_Newhall1943(V):
        """
        Returns the *luminance* :math:`R_Y` of given *Munsell* value :math:`V`
        using *Newhall et al. (1943)* method.

        Parameters
        ----------
        V : numeric or array_like
            metadata : {'type': 'Munsell Value', 'symbol': 'V', 'extent': (0, 10)}
            *Munsell* value :math:`V`.

        Returns
        -------
        numeric or array_like
            metadata : {'type': 'Luminance', 'symbol': 'R_Y', 'extent': (0, 100)}
            *luminance* :math:`R_Y`.

        Notes
        -----
        metadata : {'classifier': 'Luminance Conversion Function', 'method_name':
            'Newhall 1943', 'method_strict_name': 'Newhall et al. (1943)'}

        References
        ----------
        .. [1]  Newhall, S. M., Nickerson, D., & Judd, D. B. (1943). Final report
                of the OSA subcommittee on the spacing of the munsell colors. JOSA,
                33(7), 385. doi:10.1364/JOSA.33.000385

        Examples
        --------
        >>> luminance_Newhall1943(3.74629715382)  # doctest: +ELLIPSIS
        10.4089874...
        """

        V = np.asarray(V)

        R_Y = (
            1.2219 * V
            - 0.23111 * (V * V)
            + 0.23951 * (V**3)
            - 0.021009 * (V**4)
            + 0.0008404 * (V**5)
        )

        return R_Y

There is one caveat though: running Python with ``-OO`` argument will optimize the bytecode and trim the docstrings and as a result preventing metadata usage. This is an edge case we are aware of and it will be advertised.

These two features are consequential and taking a fair amount of time to implement and test. They will also introduce backward incompatible changes.

Stay tuned!
