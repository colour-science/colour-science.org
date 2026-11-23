"""Keep the homepage examples in sync with the notebook fragment."""

from pathlib import Path

from blinker import signal
from nikola.plugin_categories import SignalHandler


class HomeExamples(SignalHandler):
    """Build the notebook fragment before the homepage that includes it."""

    name = "home_examples"

    def set_site(self, site):
        super().set_site(site)
        signal("scanned").connect(self.register_dependencies, sender=site)

    def register_dependencies(self, site):
        if site.config["THEME"] != "colour-science":
            return

        pages = {Path(post.source_path): post for post in site.timeline}
        home = pages[Path("pages/index.rst")]
        examples = pages[Path("pages/colour-science-for-python.ipynb")]

        for lang in site.config["TRANSLATIONS"]:
            home.add_dependency(examples.translated_base_path(lang), "fragment", lang)
