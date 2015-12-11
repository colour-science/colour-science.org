#!/home/colour/development/environments/colour2.7/bin/python

# Vagrant:
#!/usr/bin/env python

import cgi

print("Content-Type: text/html\n\n")

try:
    # Vagrant:
    #
    # import sys
    #
    # sys.path.append(
    #     '/home/vagrant/anaconda3/envs/python2.7/lib/python2.7/site-packages')
    # sys.path.append('/colour-science/colour')

    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict

    import numpy as np

    import colour
    from common import ANALYTICS_TRACKING, html_format_matrix, html_select


    form = cgi.FieldStorage()

    C_SELECT_VALUE = form.getvalue('c_select') or 0
    C_SELECT_VALUE = int(C_SELECT_VALUE)
    W_SELECT_VALUE = form.getvalue('w_select') or 0
    W_SELECT_VALUE = int(W_SELECT_VALUE)
    CAT_SELECT_VALUE = form.getvalue('cat_select') or 0
    CAT_SELECT_VALUE = int(CAT_SELECT_VALUE)

    COLOURSPACES = OrderedDict(
        (k, v) for k, v in sorted(colour.RGB_COLOURSPACES.items()))
    ILLUMINANTS = OrderedDict((k, v) for k, v in
                              sorted(colour.ILLUMINANTS[
                                         'CIE 1931 2 Degree Standard Observer'].items()))
    CAT = OrderedDict((k, v) for k, v in
                      sorted(colour.CHROMATIC_ADAPTATION_TRANSFORMS.items()))

    html = """
        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/html">
        <head>
            <meta charset="utf-8">
            <title>RGB Colourspace Models Chromatically Adapted Derivation</title>
            <link rel="stylesheet" type="text/css" href="/assets/css/cgi-form.css">
            <link href="http://fonts.googleapis.com/css?family=Lato" id="google-font-selector" rel="stylesheet" type="text/css">
        </head>
        <body>
        {0}
        {1}
        </body>
        </html>"""

    form = """
        <form id="form" class="form" style="height: 555px;width: 416px" action="/cgi-bin/rgb_colourspace_models_chromatically_adapted_derivation.cgi" method="post">
            <h1>RGB Colourspace Models Chromatically Adapted Derivation</h1>
            <p>
                <a href="http://colour-science.org/">colour-science.org</a>
            </p>
            <div class="content">
                <div class="introduction">
                    This form computes the <em>chromatically adapted</em> <em>Normalised Primary Matrix</em> from the <em>Input Colourspace</em> to the given <em>Illuminant</em> using the given <em>Chromatic Adaptation Transform</em>.
                </div>
                <div id="section0" >
                    <div class="field">
                        <label>Input Colourspace</label>
                        {0}
                    </div>
                    <div class="field">
                        <label>Illuminant</label>
                        {1}
                    </div>
                    <div class="field">
                        <label>Chromatic Adaptation Transform</label>
                        {2}
                    </div>
                    <div class="field">
                        <label>RGB to XYZ Matrix</label>
                        {3}
                    </div>
                </div>
            </div>
        </form>""".format(
        html_select('c_select', COLOURSPACES.keys(), C_SELECT_VALUE),
        html_select('w_select', ILLUMINANTS.keys(), W_SELECT_VALUE),
        html_select('cat_select', CAT.keys(), CAT_SELECT_VALUE),
        html_format_matrix(colour.normalised_primary_matrix(
            colour.chromatically_adapted_primaries(
                COLOURSPACES[COLOURSPACES.keys()[C_SELECT_VALUE]].primaries,
                COLOURSPACES[COLOURSPACES.keys()[C_SELECT_VALUE]].whitepoint,
                ILLUMINANTS[ILLUMINANTS.keys()[W_SELECT_VALUE]],
                CAT.keys()[CAT_SELECT_VALUE]),
                         ILLUMINANTS[ILLUMINANTS.keys()[W_SELECT_VALUE]])))

    print(html.format(ANALYTICS_TRACKING, form))

except:
    cgi.print_exception()
