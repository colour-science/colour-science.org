# -*- coding: utf-8 -*-

import numpy as np


ANALYTICS_TRACKING = """
<!-- >>> Google Analytics -->
<script>
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-53791280-1', 'auto');
    ga('send', 'pageview');

</script>
<!-- <<< Google Analytics -->"""


def html_format_matrix(M, precision=np.finfo(np.float_).precision):
    # Handling whitepoint tuples.
    if isinstance(M, tuple):
        M = np.array(M).reshape(1, 2)

    html = '<table class="matrix-table">'
    shape = M.shape
    for i in range(shape[0]):
        html += '<tr class="matrix-row">'
        for j in range(shape[1]):
            v = M[i][j]
            pretty = '{{: 0.{}f}}'.format(precision).format(
                v) if precision is not None else v
            html += '<td class="matrix-column">{0}</td>'.format(pretty)
        html += '</tr>'
    html += '</table>'
    return html


def html_select(name, items, selected):
    html = '<select name="{0}" onchange="this.form.submit()">'.format(name)
    for i, item in enumerate(items):
        if selected == i:
            html += '<option value="{0}" selected>{1}</option>'.format(
                i, item)
        else:
            html += '<option value="{0}">{1}</option>'.format(i, item)
    html += '</select>'
    return html
