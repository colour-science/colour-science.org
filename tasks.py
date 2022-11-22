"""
Invoke - Tasks
==============
"""

from __future__ import annotations

import inspect

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

from invoke import Context, task

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = ["clean", "upgrade", "formatting", "quality", "build"]


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
def upgrade(
    ctx: Context,
    pyupgrade: bool = True,
    flynt: bool = True,
):
    """
    Upgrade the codebase with *pyupgrade* and *flynt*.

    Parameters
    ----------
    ctx
        Context.
    pyupgrade
        Whether to upgrade the codebase with *pyupgrade*.
    flynt
        Whether to upgrade the codebase with *flynt*.
    """

    if pyupgrade:
        print('Upgrading codebase with "pyupgrade"...')
        ctx.run("pre-commit run pyupgrade --all-files")

    if flynt:
        print('Upgrading codebase with "flynt"...')
        ctx.run("flynt .")


@task
def formatting(
    ctx: Context,
    black: bool = True,
):
    """
    Format the codebase with *Black*.

    Parameters
    ----------
    ctx
        Context.
    black
        Whether to format the codebase with *Black*.
    """

    if black:
        print('Formatting codebase with "Black"...')
        ctx.run("black .")


@task
def quality(ctx, flake8: bool = True):
    """
    Check the codebase with *Flake8* and lint various *restructuredText*
    files with *rst-lint*.

    Parameters
    ----------
    ctx
        Context.
    flake8
        Whether to check the codebase with *Flake8*.
    """

    if flake8:
        print('Checking codebase with "Flake8"...')
        ctx.run("flake8 .")


@task(upgrade, formatting, quality)
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
