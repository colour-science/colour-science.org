"""
Invoke - Tasks
==============
"""

from __future__ import annotations

import inspect
from pathlib import Path
from shutil import rmtree

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

from invoke.context import Context
from invoke.tasks import task

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = ["clean", "precommit", "build"]


@task
def clean(
    ctx: Context,
):
    """
    Clear Nikola's build cache while keeping the deployed site.

    Parameters
    ----------
    ctx
        Context.
    """

    print("Cleaning project...")

    cache = Path("cache")
    if cache.is_dir():
        rmtree(cache)

    for database in (Path(".doit.db"), *Path().glob(".doit.db.*")):
        database.unlink(missing_ok=True)


@task
def precommit(ctx: Context):
    """
    Run the "pre-commit" hooks on the codebase.

    Parameters
    ----------
    ctx
        Context.
    """

    print('Running "pre-commit" hooks on the codebase...')
    ctx.run("pre-commit run --all-files")


@task(precommit)
def build(ctx):
    """
    Build the project.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    """

    print("Building...")
    ctx.run("nikola build")
