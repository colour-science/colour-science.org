"""Compile the Colour Science theme as part of a Nikola build."""

from pathlib import Path
from shutil import which
from subprocess import run

from doit.exceptions import TaskFailed
from nikola.plugin_categories import Task


class BuildTailwind(Task):
    """Build and track the stylesheet used by the site templates."""

    name = "build_tailwind"

    def gen_tasks(self):
        yield self.group_task()
        if self.site.config["THEME"] != "colour-science":
            return

        theme = Path("themes/colour-science")
        stylesheet = theme / "tailwind/site.css"
        output = Path(self.site.config["OUTPUT_FOLDER"]) / "assets/css/site.css"
        cli = Path("node_modules/@tailwindcss/cli/dist/index.mjs")
        dependencies = [
            stylesheet,
            Path("package.json"),
            Path("package-lock.json"),
            Path(__file__),
            *sorted((theme / "templates").glob("*.tmpl")),
        ]
        if cli.is_file():
            dependencies.append(cli)

        def compile_stylesheet():
            node = which("node")
            if node is None or not cli.is_file():
                return TaskFailed(
                    "Building the Colour Science theme requires Node.js and npm ci."
                )

            output.parent.mkdir(parents=True, exist_ok=True)
            run(
                [
                    node,
                    str(cli),
                    "--input",
                    str(stylesheet),
                    "--output",
                    str(output),
                    "--minify",
                ],
                check=True,
            )

        yield {
            "basename": self.name,
            "name": str(output),
            "file_dep": [str(path) for path in dependencies],
            "targets": [str(output)],
            "actions": [compile_stylesheet],
            "clean": True,
        }
