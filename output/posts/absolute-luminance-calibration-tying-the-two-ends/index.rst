.. title: Absolute Luminance Calibration: Tying the Two Ends
.. slug: absolute-luminance-calibration-tying-the-two-ends
.. date: 2020-03-16 07:28:05 UTC
.. tags: absolute luminance calibration, colour science, digital still camera exposure model, physical quantities
.. category: 
.. link: 
.. description: 
.. type: text
.. has_math: true

Validation against ground truth data is an important step when implementing
support for physical quantities in a realtime or offline renderer.

In this post, a simple but effective methodology to verify that the physical
camera model behaves as expected will be presented.

.. TEASER_END

Digital Still Camera Exposure Model
-----------------------------------

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
        Standard.

Lagarde and de Rousiers (2013) describe a plausible Digital Still Camera (DSC)
Exposure Model based on the Saturation-Based Speed (SBS) method.

The saturation based speed :math:`S_{sat}` of an electronic still picture
camera is defined as:

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
        photography and optics, of interest for the discussed topic are:
        `Average Scene Reflectance in Photographic Exposure Metering <http://dougkerr.net/Pumpkin/articles/Scene_Reflectance.pdf>`__
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
--------------------------

With a plausible DSC Exposure Model implemented, calibrated ground truth data
can (should) be imaged for verification purposes.

`An Artist-Friendly Workflow for Panoramic HDRI <http://blog.selfshadow.com/publications/s2016-shading-course/unity/s2016_pbs_unity_hdri_notes.pdf>`__
by Lagarde, Lachambre and Jover (2016) describes a simple but effective process
to calibrate a Panoramic HDRI for absolute luminance. The only requirement is
to measuring the scene illuminance with a light meter during the HDRI capture.

The major advantage of this approach is that it is independent of the imaging
device and thus does not require knowledge of its calibration constant :math:`K`.

The multiplying factor :math:`S_L` used to convert the Panoramic HDRI relative
luminance values to absolute luminance values is obtained as follows:

    :math:`S_L=\cfrac{E_{vm}}{E_{vi}}`

where :math:`E_{vm}` is the metered scene upper hemisphere illuminance in
lux (:math:`lx`) and :math:`E_{vi}` is the upper hemisphere illuminance of the
Panoramic HDRI in lux, i.e. the upper hemisphere integral of the relative
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
