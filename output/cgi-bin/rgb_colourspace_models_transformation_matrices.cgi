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


    def RGB_to_RGB(c_i, c_o, transform):
        cat = colour.chromatic_adaptation_matrix_VonKries(
            colour.xy_to_XYZ(c_i.whitepoint),
            colour.xy_to_XYZ(c_o.whitepoint),
            transform)

        return (np.dot(c_o.XYZ_to_RGB_matrix,
                       np.dot(cat, c_i.RGB_to_XYZ_matrix)))


    form = cgi.FieldStorage()

    C_I_SELECT_VALUE = form.getvalue('c_i_select') or 0
    C_I_SELECT_VALUE = int(C_I_SELECT_VALUE)
    C_O_SELECT_VALUE = form.getvalue('c_o_select') or 0
    C_O_SELECT_VALUE = int(C_O_SELECT_VALUE)
    CAT_SELECT_VALUE = form.getvalue('cat_select') or 0
    CAT_SELECT_VALUE = int(CAT_SELECT_VALUE)

    COLOURSPACES = OrderedDict(
        (k, v) for k, v in sorted(colour.RGB_COLOURSPACES.items()))
    CAT = OrderedDict((k, v) for k, v in
                      sorted(colour.CHROMATIC_ADAPTATION_TRANSFORMS.items()))

    html = """
        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/html">
        <head>
            <meta charset="utf-8">
            <title>RGB Colourspace Models Transformation Matrices</title>
            <link rel="stylesheet" type="text/css" href="/assets/css/cgi-form.css">
            <link href="http://fonts.googleapis.com/css?family=Lato" id="google-font-selector" rel="stylesheet" type="text/css">
        </head>
        <body>
        {0}
        {1}
        </body>
        </html>"""

    form = """
        <form id="form" class="form" style="height: 512px;width: 416px" action="/cgi-bin/rgb_colourspace_models_transformation_matrices.cgi" method="post">
            <h1>RGB Colourspace Models Transformations Matrices</h1>
            <p>
                <a href="http://colour-science.org/">colour-science.org</a>
            </p>
            <div class="content">
                <div class="introduction">
                    <p>This form computes the colour transformation matrix from the <em>Input RGB Colourspace</em> to the <em>Output RGB Colourspace</em> using the given <em>Chromatic Adaptation Transform</em>.</p>
                </div>
                <div id="section0" >
                    <div class="field">
                        <label>Input RGB Colourspace</label>
                        {0}
                    </div>
                    <div class="field">
                        <label>Output RGB Colourspace</label>
                        {1}
                    </div>
                    <div class="field">
                        <label>Chromatic Adaptation Transform</label>
                        {2}
                    </div>
                    <div class="field">
                        <label>RGB Transformation Matrix</label>
                        {3}
                    </div>
                </div>
            </div>
        </form>""".format(
        html_select('c_i_select', COLOURSPACES.keys(), C_I_SELECT_VALUE),
        html_select('c_o_select', COLOURSPACES.keys(), C_O_SELECT_VALUE),
        html_select('cat_select', CAT.keys(), CAT_SELECT_VALUE),
        html_format_matrix(
            RGB_to_RGB(COLOURSPACES[COLOURSPACES.keys()[C_I_SELECT_VALUE]],
                       COLOURSPACES[COLOURSPACES.keys()[C_O_SELECT_VALUE]],
                       CAT.keys()[CAT_SELECT_VALUE])))

    print(html.format(ANALYTICS_TRACKING, form))

except:
    cgi.print_exception()
