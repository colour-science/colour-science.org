"""
Invoke - Tasks
==============
"""

from __future__ import annotations

import inspect

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
    Clean the project.

    Parameters
    ----------
    ctx
        Context.
    """

    print("Cleaning project...")

    patterns = ["output", ".doit.db"]

    for pattern in patterns:
        ctx.run(f"rm -rf {pattern}")


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
