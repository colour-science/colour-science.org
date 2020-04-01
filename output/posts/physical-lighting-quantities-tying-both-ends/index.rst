.. title: Physical Lighting Quantities: Tying Both Ends
.. slug: physical-lighting-quantities-tying-both-ends
.. date: 2020-03-16 07:28:05 UTC
.. tags: absolute luminance calibration, colour science, digital still camera exposure model, physical quantities
.. category: 
.. link: 
.. description: 
.. type: text
.. has_math: true

Validation against ground truth data is an important step when implementing
support for physical lighting quantities in a realtime or offline renderer.

In this post, a simple but effective method to assess that the physical camera
model behaves as expected against ground truth data will be presented.

.. TEASER_END

Digital Still Camera Exposure Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Epic Games <https://www.epicgames.com/site/en-US/about>`__ recently published
a `comprehensive blog post <https://www.unrealengine.com/en-US/tech-blog/how-epic-games-is-handling-auto-exposure-in-4-25>`__
about auto-exposure handling in Unreal Engine 4.25. The part of most significance
for this post is the mention of
`ISO Standard: 12232:2019 <https://www.iso.org/standard/73758.html>`__.

.. class:: alert alert-dismissible alert-info

    | *Note*
    |
    | It is unfortunate that no reference is made to
        `Moving Frostbite to Physically Based Rendering 3.0 <https://seblagarde.files.wordpress.com/2015/07/course_notes_moving_frostbite_to_pbr_v32.pdf>`__
        by Lagarde and de Rousiers (2013). 7 years ago, they analytically
        derived the 1.2 scaling factor while citing the aforementioned ISO
        Standard: 12232:2006. They describe a plausible Digital Still Camera
        (DSC) Exposure Model based on the Saturation-Based Speed (SBS) method.

The saturation based speed :math:`S_{sat}` of an electronic still picture
camera as given in ISO Standard: 12232:2019 is defined as:

    :math:`S_{sat}=\cfrac{78}{H_{sat}}`

where :math:`H_{sat}` is the minimum focal plane exposure, expressed in
lux-seconds (:math:`lx.s`), that produces the maximum valid (not clipped or
bloomed) camera output signal. This provides :math:`1/2` "stop" of headroom
(41% additional headroom) for specular highlights above the signal level that
would be obtained from a theoretical 100% reflectance object in the scene,
so that a theoretical 141% reflectance object in the scene would produce a
focal plane exposure of :math:`H_{sat}`.

The focal plane exposure :math:`H` in lux-seconds is given by the following
equation:

    :math:`H=\cfrac{q L t F^2}{A^2 i^2} + H_f`

where

-   :math:`L` is the scene luminance expressed in :math:`cd/m^2`
-   :math:`A` is the lens F-Number
-   :math:`t` is the exposure time expressed in seconds
-   :math:`F` is the lens focal length expressed in meters
-   :math:`I` is the image distance expressed in meters
-   :math:`H_f` is the focal plane flare exposure expressed in lux-seconds
-   :math:`q` is the factor modeling the total lens vignetting and transmission
    attenuation:

    :math:`q=\cfrac{\pi T f_v \cos^4\theta}{4}`

    with :math:`T` the transmission factor of the lens, :math:`f_v` the
    vignetting factor and :math:`theta` the angle of image point off axis.
    For a camera focused on infinity, :math:`Hf<<H`, :math:`T=9/10`,
    :math:`\theta=10^{\circ}`, :math:`\cos^4\theta=94/100`, and
    :math:`fv=98/100`, :math:`q` is equal to 65/100.

.. class:: alert alert-dismissible alert-info

    | *Note*
    |
    | `Doug A. Kerr <http://dougkerr.net/>`__ hosts a
        `series of articles <http://dougkerr.net/Pumpkin/index.htm>`__ on
        photography and optics. The following article are of interest for the
        discussed topic: `Average Scene Reflectance in Photographic Exposure Metering <http://dougkerr.net/Pumpkin/articles/Scene_Reflectance.pdf>`__
        and `Derivation of the "Cosine Fourth" Law for Falloff of Illuminance Across a Camera Image <http://dougkerr.net/Pumpkin/articles/Cosine_Fourth_Falloff.pdf>`__

The adjusted focal plane exposure :math:`H_{SBS}` is obtained by scaling
the focal plane exposure :math:`H` according to the SBS method and, optionally,
scaling by the ISO arithmetic speed :math:`S`:

    :math:`H_{SBS}=H\cfrac{S}{100}\cfrac{100}{78}=H\cfrac{S}{78}`

`Colour - HDRI <https://github.com/colour-science/colour-hdri/blob/develop/colour_hdri/exposure/dsc.py>`__
implements the aforementioned model with Python:

.. code:: python

    >>> import colour_hdri
    >>> colour_hdri.saturation_based_speed_focal_plane_exposure(18, 5.6, 0.25, 400)
    0.46993364546604555

`Colour - Nuke <https://github.com/colour-science/colour-nuke/blob/master/colour_nuke/scripts/digital_still_camera_exposure.nk>`__
offers a Gizmo/Group implementation also available on
`Nukepedia <http://www.nukepedia.com/gizmos/image/digital_still_camera_exposure>`__.

.. image:: /images/Blog_Saturation_Based_Speed_Focal_Plane_Exposure_in_Nuke.png

Panoramic HDRI Calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^

With a plausible DSC Exposure Model implemented, calibrated ground truth data
can be imaged for verification purposes.

`An Artist-Friendly Workflow for Panoramic HDRI <http://blog.selfshadow.com/publications/s2016-shading-course/unity/s2016_pbs_unity_hdri_notes.pdf>`__
by Lagarde, Lachambre and Jover (2016) describes a simple but effective process
to calibrate a panoramic HDRI for absolute luminance. The only requirement is
to measuring the scene illuminance with a light meter during the HDRI capture.

The major advantage of this approach is that it is independent of the imaging
device and thus does not require knowledge of its calibration constant :math:`K`.

The multiplying factor :math:`S_L` used to convert the panoramic HDRI relative
luminance values to absolute luminance values is obtained as follows:

    :math:`S_L=\cfrac{E_{vm}}{E_{vi}}`

where :math:`E_{vm}` is the metered scene upper hemisphere illuminance in
lux (:math:`lx`) and :math:`E_{vi}` is the upper hemisphere illuminance of the
panoramic HDRI in lux, i.e. the upper hemisphere integral of the relative
luminance values:

    :math:`\int_{\Omega}{L\ cos(\theta)\omega}`

For an equirectangular image, the solid angle :math:`\omega` of a pixel is given
as follows:

    :math:`\omega=sin(\theta)\cfrac{2\pi}{w}\cfrac{\pi}{h}`

where :math:`w` and :math:`h` are the width and height of the image,
respectively.

`Colour - HDRI <https://github.com/colour-science/colour-hdri/blob/develop/colour_hdri/calibration/absolute_luminance.py>`__
implements support for absolute luminance calibration with Python:

.. code:: python

    >>> import colour_hdri
    >>> import numpy as np
    >>> RGB = np.ones([2048, 1024, 3])
    >>> colour_hdri.upper_hemisphere_illuminance_Lagarde2016(RGB)
    >>> colour_hdri.absolute_luminance_calibration_Lagarde2016(RGB, 120000)[0, 0]
    array([ 38215.85392444,  38215.85392444,  38215.85392444])
    >>> colour_hdri.calibration.absolute_luminance.upper_hemisphere_illuminance_Lagarde2016(RGB)
    3.1400580564615663

.. class:: alert alert-dismissible alert-info

    | *Note*
    |
    | Careful readers will have noticed that the last call to the
        `colour_hdri.calibration.absolute_luminance.upper_hemisphere_illuminance_Lagarde2016`
        definition does not return :math:`\pi`. This is induced by the
        numerical discretization to raster space, however, as image dimensions
        increase toward infinity, the computed value converges toward
        :math:`\pi`, e.g. 3.1414009 and 3.1414968 for 16384x8192 and 32768x16384
        sized images respectively.

Likewise, `Colour - Nuke <https://github.com/colour-science/colour-nuke/blob/master/colour_nuke/scripts/panoramic_hdri_absolute_luminance_calibration.nk>`__
offers a Gizmo/Group implementation also available on
`Nukepedia <http://www.nukepedia.com/gizmos/colour/panoramic-hdri-absolute-luminance-calibration>`__.

.. image:: /images/Blog_Absolute_Luminance_Calibration_in_Nuke.png

Imaging the Panoramic HDRI with the Digital Still Camera Exposure Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A free panoramic HDRI processed accurately is a rarity online. Most vendors
sell either non-linear or clipped imagery, and when it is not clipped,
photometric and colorimetric information is missing and because the creation
process is unknown, the data cannot be trusted for scientific applications
requiring physical lighting quantities.

Fortunately, Lagarde, Lachambre and Jover (2016) have published `a trustworthy
panoramic HDRI <https://blog.selfshadow.com/publications/s2016-shading-course/unity/supplemental/index.html>`__
that will be used in this section.

.. figure:: /images/Blog_Unity_Treasure_Island_ReStitched.png

    Final Treasure Island panoramic HDRI merged and stitched from the original
    .CR2 files.

The authors have been kindly enough to send me the original .CR2 files so that
I could merge and stitch them.

Merging was performed with `Colour - HDRI <https://github.com/colour-science/colour-hdri/blob/develop/colour_hdri/generation/radiance.py>`__,
specifically, by using a modified version of the
`Merge from Raw Files <https://github.com/colour-science/colour-hdri/blob/develop/colour_hdri/examples/examples_merge_from_raw_files.ipynb>`__
example.

.. class:: alert alert-dismissible alert-warning

    | *Warning*
    |
    | The aforementioned Jupyter Notebook is an example, typical production
        usage would require multi-processing and use
        `rawpy <https://pypi.org/project/rawpy/>`__ or
        `rawtoaces <https://github.com/ampas/rawtoaces>`__.

.. figure:: /images/Blog_Unity_Treasure_Island_ReStitched_Angles.png

    .CR2 file batches merged to HDRI. Note that the bottom row was captured
    with neutral density filters.

With the various .CR2 file batches merged, the validation process involves
comparing a cherry picked .CR2 file from one of the exposure batches with the
corresponding HDRI scaled to absolute luminance and imaged via the DSC Exposure
Model using the camera settings of the .CR2 file.

.. figure:: /images/Blog_Unity_Treasure_Island_Angle_Imaged.png

    From left to right: The HDRI scaled to absolute luminance using 51000 lux,
    the cherry picked .CR2 file, the HDRI scaled to absolute luminance and
    imaged with the DSC Exposure Model.

Conclusion
^^^^^^^^^^

With Treasure Island, the HDRI scaled to absolute luminance is about 14%
brighter than the .CR2 file. This is not perfect but considering the scaling
factors involved, it is reasonably satisfactory.

Some potential source of discrepancies are:

-   Lack of flat-fields to correct the neutral density filter attenuation and
    thus some manual correction was introduced.
-   Illuminance measurement precision.
-   Sun pixel coverage is small and might introduce significant error.
-   Unknown parameters for the focal plane exposure equation that were left at
    their default values, e.g. lens attenuation values.

Other tests performed with various non-public HDRI imaged similarly have
yielded better results with less error. Importantly though, the technique is
dependent on good metering of the scene upper hemisphere illuminance and the
non-clipped capture and correct processing of HDR imagery.

Finally, I would like to thanks Sebastien Lagarde, Sebastien Lachambre and
Cyril Jover for the recurring conversations on that topic the past few years.
