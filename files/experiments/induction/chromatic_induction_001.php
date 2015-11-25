<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chromatic Induction - Experiment 001</title>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/snap.svg/0.3.0/snap.svg-min.js"></script>
    <style>
        @import url("http://fonts.googleapis.com/css?family=Open+Sans:400,700");

        * {
            margin: 0;
            padding: 0;
        }

        body {
            background: black;
            font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 12px;
            height: 100%;
            overflow: hidden;
        }

        a {
            color: rgba(255, 255, 255, 0.85);
        }

        h1, h2, h3, h4, h5, h6 {
            padding-bottom: 5px;
            padding-top: 5px;
        }

        ul {
            padding-left: 15px;
        }

        #guide {
            color: rgba(255, 255, 255, 0.85);
            background-color: rgba(0, 0, 0, 0.85);
            bottom: 10%;
            padding: 10px;
            position: absolute;
            right: 10%;
            width: 400px;
            z-index: 1;
        }

        #title {
            font-size: 1.75em;
        }

        .center {
            text-align: center;
        }

    </style>
    <script>
        P0 = [];
        $(window).on('mousedown', function (e) {
            P0 = {x: e.pageX, y: e.pageY};
        }).on('mousemove', function (e) {
            var p1 = {x: e.pageX, y: e.pageY};
            var distance = Math.sqrt(Math.pow(p1.x - P0.x, 2) +
                    Math.pow(p1.y - P0.y, 2));
            if (distance > 16) {
                $("#guide").animate({
                    opacity: 0
                }, 500);
            }
        });
    </script>
    <script>
        window.onload = function () {
            WIDTH = $(window).width();
            HEIGHT = $(window).height();
            THICKNESS = 4;

            CANVAS = Snap(WIDTH, HEIGHT);

            BLACK_LINES = [];
            BLACK_LINES_DX = 0, BLACK_LINES_DY = 0, LAST_DX = 0, LAST_DY = 0;

            function linspace(a, b, n) {
                if (typeof n === "undefined") {
                    n = Math.max(Math.round(b - a) + 1, 1);
                }

                if (n < 2) {
                    return n === 1 ? [a] : [];
                }

                var i, ret = Array(n);
                n--;

                for (i = n; i >= 0; i--) {
                    ret[i] = (i * b + (n - i) * a) / n;
                }
                return ret;
            }

            function black_lines_on_drag(dx, dy) {
                var dx = dx + LAST_DX;
                var dy = dy + LAST_DY;
                var k = 35;
                for (var i = 0; i < BLACK_LINES.length; i++) {
                    BLACK_LINES[i].transform(
                            Snap.format("r{x}", {x: dx / k + dy / k}));
                }
                BLACK_LINES_DX = dx;
                BLACK_LINES_DY = dy;

            };

            function black_lines_on_drag_start(x, y, e) {

            };

            function black_lines_on_drag_end(e) {
                LAST_DX = BLACK_LINES_DX;
                LAST_DY = BLACK_LINES_DY;

            };

            function vertical_lines_pattern(width, height, colour, thickness) {
                var vertical_line = CANVAS.path(
                        Snap.format('M{x},0L{x},{y}', {
                            x: thickness / 2,
                            y: height
                        })).attr({
                            stroke: colour,
                            strokeWidth: thickness
                        });
                return vertical_line.pattern(0, 0, width, height);
            }

            function vertical_lines_interactive(count, x0, y0, x1, y1, colour, thickness) {
                var lines = []
                samples = linspace(x0, x1, count);
                for (var i = 0; i < samples.length; i++) {
                    var line = CANVAS.line(
                            samples[i], y0, samples[i], y1).attr({
                                stroke: colour,
                                strokeWidth: thickness
                            });
                    lines.push(line);
                }
                return lines
            }

            var red_lines = CANVAS.rect(0, 0, WIDTH, HEIGHT);
            var red_vertical_lines = vertical_lines_pattern(
                            THICKNESS * 3, HEIGHT, '#DD0000', THICKNESS);
            red_lines.attr({
                fill: red_vertical_lines
            });

            var green_lines = CANVAS.rect(0, 0, WIDTH, HEIGHT);
            var green_vertical_lines = vertical_lines_pattern(
                            THICKNESS * 3, HEIGHT, '#00DD00', THICKNESS);
            green_lines.attr({
                fill: green_vertical_lines
            });

            green_lines.transform(
                    Snap.format("t{x},{y}", {x: THICKNESS, y: 0}));

            var blue_lines = CANVAS.rect(0, 0, WIDTH, HEIGHT);
            var blue_vertical_lines = vertical_lines_pattern(
                            THICKNESS * 3, HEIGHT, '#0000DD', THICKNESS);
            blue_lines.attr({
                fill: blue_vertical_lines
            });

            blue_lines.transform(
                    Snap.format("t{x},{y}", {x: THICKNESS * 2, y: 0}));

            var black_lines = CANVAS.rect(0, 0, WIDTH, HEIGHT);
            black_lines.attr({
                fill: 'transparent'
            });

            var horizontal_margin = WIDTH * 0.1
            var vertical_margin = HEIGHT * 0.25

            BLACK_LINES = vertical_lines_interactive(
                    10,
                    horizontal_margin,
                    vertical_margin,
                            WIDTH - horizontal_margin,
                            HEIGHT - vertical_margin,
                    '#000000',
                            THICKNESS * 2)

            black_lines.drag(
                    black_lines_on_drag,
                    black_lines_on_drag_start,
                    black_lines_on_drag_end);
        };
    </script>
</head>
<body>
<?php include_once("../../analytics_tracking.php") ?>

<div id="data"></div>

<div id="guide">
    <h2 id="title" class="center">Chromatic Induction - Experiment 001</h2>

    <h3>Usage</h3>
    <ul>
        <li>
            Slightly squint your eyes.
        </li>
        <li>
            Drag to rotate the black lines.
        </li>
    </ul>
    <h3>Definition</h3>

    <p>
        Chromatic induction is the modification of the visual response that
        occurs when 2 colour stimuli (of any spectral irradiance distribution)
        are viewed side-by-side in which each stimulus alters the appearance of
        the other.
    </p>

    <h3 class="center">
        <a href="http://colour-science.org">colour-science.org</a>
    </h3>
</div>
</body>
</html>